import os
import subprocess
from datetime import datetime as DateTime
from file import get_file_difficulty
from global_vars import DIFFICULTY_PROMPT  # for getting solved date
from file import get_code_files, get_write_problem_link, correct_file_difficulty, write_string_to_file, DIFFICULTY_LINE_NUMBER
from internet import get_HTML_path, get_domains
import platform  # for determinating file creation date
import git  # for checking if there are uncommitted files
from global_vars import PROBLEMS, DATE, DATETIME_FORMAT, DATAPATH
from bs4 import BeautifulSoup
import time  # for calculating execution time

PROCESS_PROBLEM_TIME = 0
GET_WRITE_PROBLEM_LINK_TIMES = list()
GET_DOMAINS_TIMES = list()
GET_DIFFICULTY_TIMES = list()
GET_SOLVED_DATE_TIMES = list()
GET_INSTRUCTIONS_TIMES = list()
WRITE_TO_CSV_TIME = 0


def files_to_push():
    """
    Checks if there are any uncommited files since last commit and aborts program
    """
    print("Check for uncommitted files...")
    result = []
    repo = git.Repo('.', search_parent_directories=True)
    changed_files = [item.a_path for item in repo.index.diff(None)]
    for file in changed_files:
        if "problems" in file:
            result.append(file)
    if len(result) > 0:
        raise RuntimeError(
            "There are uncommited files in directory. Commit all files and try again.")


class HackerRankProblem():
    def __init__(self, id, link, domain, subdomain, subsubdomain, difficulty, solved_date, instruction):
        self.id = id
        self.link = link
        self.domain = domain
        self.subdomain = subdomain
        self.subsubdomain = subsubdomain
        self.difficulty = difficulty
        self.solved_date = solved_date
        self.instruction = instruction


def process_problems():
    """
    Converts all problems to objects
    """
    process_problem_time_start = time.perf_counter_ns()
    errors = list()
    problem_list = list()
    file_paths = get_code_files()
    running_id = 0
    length = len(file_paths)
    for file in file_paths:
        index = file_paths.index(file)
        print("Converting file " + str(index) + " of " + str(length))
        get_write_problem_link_time_start = time.perf_counter_ns()
        link, success = get_write_problem_link(file, index)
        get_write_problem_link_time_end = time.perf_counter_ns()
        total_time = get_write_problem_link_time_end - get_write_problem_link_time_start
        GET_WRITE_PROBLEM_LINK_TIMES.append(total_time)
        if success is False:
            errors.append(file)
        splitted_path = file.split(os.path.sep)
        # penultimate element in file path
        code_folder = splitted_path[len(splitted_path) - 2]
        html_file_path = get_HTML_path(code_folder)
        if html_file_path is not None:
            # search for link
            open_html_file = open(html_file_path, 'r')
            soup = BeautifulSoup(open_html_file, 'html.parser')
            get_domains_times_start = time.perf_counter_ns()
            domain, subdomain, subsubdomain = get_domains(file, soup)
            get_domains_times_end = time.perf_counter_ns()
            time_spent = get_domains_times_end - get_domains_times_start
            GET_DOMAINS_TIMES.append(time_spent)
            difficulty = get_difficulty(file, index, soup)
            solved_date = get_solved_date(file)
            instruction = get_instructions(file)
            problem = HackerRankProblem(
                running_id, link, domain, subdomain, subsubdomain, difficulty, solved_date, instruction)
            problem_list.append(problem)
            running_id += 1
    if len(errors) > 0:
        print("Errors occured in following files: ")
        for item in errors:
            print(item)
    process_problem_time_end = time.perf_counter_ns()
    PROCESS_PROBLEM_TIME = process_problem_time_end - process_problem_time_start
    return problem_list


def get_difficulty(file, index, soup):
    """
    Gets the difficulty of a HackerRank problem
    :returns: difficulty (string)
    """
    get_difficulty_start = time.perf_counter_ns()
    print("Get difficulty for " + file + "...")
    found = False
    if get_file_difficulty(file) is not None:
        found = True
        file_difficulty = get_file_difficulty(file)
    # search for difficulty in HTML file
    if found is True:
        div = soup.find_all('div', attrs={'class': 'card-details'})[index]
        first_child = next(div.children, None)
        html_difficulty = first_child.text()
        difficulty_dict = {
            'Easy': 1,
            'Medium': 2,
            'Hard': 3
        }
        int_file_difficulty = difficulty_dict.get(file_difficulty)
        int_html_difficulty = difficulty_dict.get(html_difficulty)
        if int_html_difficulty != int_file_difficulty:
            correct_file_difficulty(file, int_html_difficulty)
        difficulty_dict_reversed = {y: x for x, y in difficulty_dict.items()}
        master_difficulty = difficulty_dict_reversed.get(int_html_difficulty)
        return master_difficulty
    else:  # difficulty not found in file
        # get difficulty from HTML only
        div = soup.find_all('div', attrs={'class': 'card-details'})[index]
        first_child = next(div.children, None)
        html_difficulty = first_child.text
        difficulty = DIFFICULTY_PROMPT + html_difficulty + '\n'
        write_string_to_file(file, difficulty, DIFFICULTY_LINE_NUMBER)
        get_difficulty_end = time.perf_counter_ns()
        time_spent = get_difficulty_end - get_difficulty_start
        GET_DIFFICULTY_TIMES.append(time_spent)
        return difficulty


def get_creation_date(filename):
    """Gets the last created timestamp of the file."""
    if platform.system() == 'Windows':
        ts = os.stat(filename).st_ctime
    elif platform.system() == 'Darwin':  # Mac OS
        ts = os.stat(filename).st_birthtime
    elif platform.system() == 'Linux':
        # We're probably on Linux. No easy way to get creation dates here,
        # so we'll settle for when its content was last modified.
        ts = os.stat(filename).st_mtime  # linux
    else:
        # cannot determine os
        ts = os.stat(filename).st_ctime
    ts = DateTime.fromtimestamp(ts)
    temp = DateTime.strftime(ts, DATETIME_FORMAT)
    ts = DateTime.strptime(temp, DATETIME_FORMAT)
    return ts


def get_solved_date(file):
    """
    Get the date the HackerRank problem was solved given by the last commit date
    :string file: file to calculate solved date of
    :returns: solved date (int)
    """
    get_solved_date_start = time.perf_counter_ns()
    print("Get solved date for file " + file)
    if DATE not in ['creation', 'last modification', 'first commit']:
        raise ValueError()
    if DATE == 'creation':
        date = get_creation_date(file)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        GET_SOLVED_DATE_TIMES.append(time_spent)
        return str(date)
    elif DATE == 'last modified':
        process = subprocess.Popen("git pull", stdout=subprocess.PIPE)

        command = 'git log --follow -p -- ' + "\"" + file + "\""
        p = subprocess.check_output(command, cwd=PROBLEMS, shell=True)

        p = p.decode('utf-8')
        p = p.split('\n')[2]
        p = p[8:]
        dt = DateTime.strptime(p, DATETIME_FORMAT)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        GET_SOLVED_DATE_TIMES.append(time_spent)
        return str(dt)
    elif DATE == 'first commit':
        command = 'git log --diff-filter=A --follow --format=%aI -1 -p -- ' + "\"" + file + "\""
        date = subprocess.check_output(command, cwd=PROBLEMS, shell=True)
        date = date.decode('utf-8')
        date = date.split('\n')[0]
        length = len(date)
        date = date[0:-3] + date[-2:]  # delete colon between timezone
        length = len(date)
        for i in range(length):
            if(date[i] == 'T'):
                # replace T with space and cut timezone
                date = date[0:i] + ' ' + date[i + 1:length-5]
                break
        date_obj = DateTime.strptime(date, DATETIME_FORMAT)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        GET_SOLVED_DATE_TIMES.append(time_spent)
        return str(date_obj)


def get_instructions(file):
    """
    Gets the instructions for a HackerRank problem if not present
    :string file: path to problem file
    :returns: path to instruction file
    """
    get_instructions_start = time.perf_counter_ns()
    print("Get instruction file for " + file + "...")
    file_name = file.split(os.path.sep)[-1]
    file_name_no_ext = os.path.splitext(file_name)[0]
    instruction_path = "." + os.path.sep + "instructions" + \
        os.path.sep + file_name_no_ext + ".pdf"
    print(instruction_path)
    full_path = PROBLEMS + instruction_path
    if os.path.exists(full_path):
        get_instructions_end = time.perf_counter_ns()
        time_spent = get_instructions_end - get_instructions_start
        GET_INSTRUCTIONS_TIMES.append(time_spent)
        return instruction_path
    else:
        get_instructions_end = time.perf_counter_ns()
        time_spent = get_instructions_end - get_instructions_start
        GET_INSTRUCTIONS_TIMES.append(time_spent)
        return None


def write_to_csv(problem_list):
    """
    Writes the problem list to a csv file
    :list problem_list: list of HackerRankProblem objects
    """
    print("Writing problems to file...")
    write_to_csv_time_start = time.perf_counter_ns()
    try:
        with open(DATAPATH, 'w') as f:
            # write column names to file
            result = list()
            dummy_obj = HackerRankProblem(
                0, 'http', 'domain', 'test', 'test', 'Easy', '14.3.21', 'link')
            for key in dummy_obj.__dict__:
                result.append(key)
            string = ','.join(result)
            f.write(string + '\n')

            # write problems to file
            for item in problem_list:
                result = list()
                index = problem_list.index(item)
                print("Writing problem " + str(index) + " to file...")
                string = ''
                for key in item.__dict__:
                    result.append(str(getattr(item, key)))
                string = ','.join(result)
                f.write(string + '\n')
            write_to_csv_time_end = time.perf_counter_ns()
            WRITE_TO_CSV_TIME = write_to_csv_time_end - write_to_csv_time_start
    except IOError:
        print('IOError occured while accessing', DATAPATH)
    except Exception:
        raise Exception()


def print_statistics(total_time):
    nano = 1000000000
    print("Execution time of script:", total_time/nano, "s")
    file_list = get_code_files()
    no_files = len(file_list)
    time_per_file = total_time / no_files
    print("Execution time per file", time_per_file, "ns")
    process_problem_time_per_file = PROCESS_PROBLEM_TIME / no_files
    print("Process problem time per file:",
          process_problem_time_per_file, "ns")
    total_get_write_problem_link_time = 0
    for time in GET_WRITE_PROBLEM_LINK_TIMES:
        total_get_write_problem_link_time += time
    avg_get_write_problem_link_time = total_get_write_problem_link_time / no_files
    print("Average time to get or write problem link to file:",
          avg_get_write_problem_link_time, "ns")
    total_get_domains_time = 0
    for time in GET_DOMAINS_TIMES:
        total_get_domains_time += time
    avg_get_domains_time = total_get_domains_time / no_files
    print("Average time to get domains:", avg_get_domains_time, "ns")
    total_get_difficulty_time = 0
    for time in GET_DIFFICULTY_TIMES:
        total_get_difficulty_time += time
    avg_get_difficulty_time = total_get_difficulty_time / no_files
    print("Average time to get difficulty:", avg_get_difficulty_time, "ns")
    total_get_solved_date_time = 0
    for time in GET_SOLVED_DATE_TIMES:
        total_get_solved_date_time += time
    avg_get_solved_date_time = total_get_solved_date_time / no_files
    print("Average time to get solved date time:",
          avg_get_solved_date_time, "ns")
    total_get_instructions_time = 0
    for time in GET_INSTRUCTIONS_TIMES:
        total_get_instructions_time += time
    avg_get_instructions_time = total_get_instructions_time / no_files
    print("Average time to get instructions:", avg_get_instructions_time, "ns")
    total_csv_time = WRITE_TO_CSV_TIME
    print("Total time to write to csv file:", total_csv_time/nano, "s")
    avg_csv_time = total_csv_time / no_files
    print("Average time to write to csv file:", avg_csv_time, "ns")


def main():
    total_time_start = time.perf_counter_ns()
    # files_to_push()
    problem_list = process_problems()
    write_to_csv(problem_list)
    total_time_end = time.perf_counter_ns()
    total_time = total_time_end - total_time_start
    print_statistics(total_time)


main()
