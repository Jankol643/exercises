import os
import subprocess
from datetime import datetime as DateTime
from file import get_file_difficulty
import global_vars
from file import get_code_files, get_write_problem_link, correct_file_difficulty, write_string_to_file, DIFFICULTY_LINE_NUMBER
from internet import get_HTML_path, get_domains
import platform  # for determinating file creation date
import git  # for checking if there are uncommitted files
from bs4 import BeautifulSoup
import time  # for calculating execution time
import pandas
import re


def files_to_push():
    """Checks if there are any uncommited files since last commit and aborts program"""
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
    def __init__(self, problem_id, link, domain, subdomain, subsubdomain, difficulty, solved_date, instruction):
        """
        Initializes a new HackerRankProblem

        :param problem_id: id of problem
        :type problem_id: int
        :param link: link to problem on hackerrank.com
        :type link: string
        :param domain: category of problem
        :type domain: string
        :param subdomain: subcategory of problem
        :type subdomain: string or None
        :param subsubdomain: subsubcategory of problem
        :type subsubdomain: string or None
        :param difficulty: difficulty of hackerrank problem according to website
        :type difficulty: string
        :param solved_date: date when problem was solved
        :type solved_date: string
        :param instruction: relative path to instruction file
        :type instruction: string
        """
        self.problem_id = problem_id
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
        global_vars.GET_WRITE_PROBLEM_LINK_TIMES.append(total_time)
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
            global_vars.GET_DOMAINS_TIMES.append(time_spent)
            difficulty = get_difficulty(file, index, soup)
            solved_date = get_solved_date(file)
            instruction = get_instructions(file)
            instruction = '\"' + instruction + '\"'
            problem = HackerRankProblem(
                running_id, link, domain, subdomain, subsubdomain, difficulty, solved_date, instruction)
            problem_list.append(problem)
            running_id += 1
    if len(errors) > 0:
        print("Errors occured in following files: ")
        for item in errors:
            print(item)
    return problem_list


def get_difficulty(file, index, soup):
    """
    Gets the difficulty of a HackerRank problem
    :returns: difficulty (string)
    """
    get_difficulty_start = time.perf_counter_ns()
    print("Get difficulty for " + file + "...")
    found = False
    file_difficulty = get_file_difficulty(file)
    if file_difficulty is not None:
        found = True
    # search for difficulty in HTML file
    if found is True:
        div = soup.find_all('div', attrs={'class': 'card-details'})[index]
        first_child = next(div.children, None)
        html_difficulty = first_child.text.strip()
        if html_difficulty != file_difficulty:
            correct_file_difficulty(file, html_difficulty)
        get_difficulty_end = time.perf_counter_ns()
        time_spent = get_difficulty_end - get_difficulty_start
        global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
        return html_difficulty
    else:  # difficulty not found in file
        # get difficulty from HTML only
        div = soup.find_all('div', attrs={'class': 'card-details'})[index]
        first_child = next(div.children, None)
        html_difficulty = first_child.text.strip()
        write_difficulty = global_vars.DIFFICULTY_PROMPT + html_difficulty + '\n'
        write_string_to_file(file, write_difficulty, DIFFICULTY_LINE_NUMBER)
        get_difficulty_end = time.perf_counter_ns()
        time_spent = get_difficulty_end - get_difficulty_start
        global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
        return html_difficulty


def get_creation_date(filename):
    """
    Gets the creation date and time of a file

    :param filename: path to file
    :type filename: string
    :return: creation time of file or on Linux last modification time
    :rtype: datetime
    """
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
    temp = DateTime.strftime(ts, global_vars.DATETIME_FORMAT)
    ts = DateTime.strptime(temp, global_vars.DATETIME_FORMAT)
    return ts


def get_solved_date(file):
    """
    Get the date the HackerRank problem was solved

    :string file: file to calculate solved date of
    :returns: solved date (string)
    """
    get_solved_date_start = time.perf_counter_ns()
    print("Get solved date for file " + file)
    if global_vars.DATE not in ['creation', 'last modification', 'first commit']:
        raise ValueError()
    if global_vars.DATE == 'creation':
        date = get_creation_date(file)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        global_vars.GET_SOLVED_DATE_TIMES.append(time_spent)
        return str(date)
    elif global_vars.DATE == 'last modified':
        args = ['git', 'pull']
        subprocess.Popen(args, stdout=subprocess.PIPE)

        args = ['git', 'log', '--follow', '-p', '-- ' + "\"" + file + "\""]
        p = subprocess.check_output(args, cwd=global_vars.PROBLEMS)

        p = p.decode('utf-8')
        p = p.split('\n')[2]
        p = p[8:]
        dt = DateTime.strptime(p, global_vars.DATETIME_FORMAT)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        global_vars.GET_SOLVED_DATE_TIMES.append(time_spent)
        return str(dt)
    elif global_vars.DATE == 'first commit':
        args = ['git', 'log', '--diff-filter=A', '--follow', '--format=%aI', '-1', '-p', '-- ' + "\"" + file + "\""]
        date = subprocess.check_output(args, cwd=global_vars.PROBLEMS)
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
        date_obj = DateTime.strptime(date, global_vars.DATETIME_FORMAT)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        global_vars.GET_SOLVED_DATE_TIMES.append(time_spent)
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
    # link java file to correct instruction
    if file_name == 'Generics.java':
        instruction_path = "instructions" + os.path.sep + \
            'Day 21 - ' + file_name_no_ext + ".pdf"
        get_instructions_end = time.perf_counter_ns()
        time_spent = get_instructions_end - get_instructions_start
        global_vars.GET_INSTRUCTIONS_TIMES.append(time_spent)
        return instruction_path
    instruction_path = "instructions" + os.path.sep + file_name_no_ext + ".pdf"
    full_path = global_vars.PROBLEMS + '30 days of Code' + os.path.sep + instruction_path
    if os.path.exists(full_path):
        get_instructions_end = time.perf_counter_ns()
        time_spent = get_instructions_end - get_instructions_start
        global_vars.GET_INSTRUCTIONS_TIMES.append(time_spent)
        return instruction_path
    else:
        get_instructions_end = time.perf_counter_ns()
        time_spent = get_instructions_end - get_instructions_start
        global_vars.GET_INSTRUCTIONS_TIMES.append(time_spent)
        return None


def write_to_csv(problem_list):
    """
    Writes the problem list to a csv file
    :list problem_list: list of HackerRankProblem objects
    """
    print("Writing problems to file...")
    try:
        with open(global_vars.DATAPATH, 'w') as f:
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
                string = ''
                for key in item.__dict__:
                    result.append(str(getattr(item, key)))
                string = ','.join(result)
                f.write(string + '\n')
    except IOError:
        print('IOError occured while accessing', global_vars.DATAPATH)
    except Exception:
        raise Exception()


def print_statistics(total_time):
    nano = 1000000000
    precision = 3
    print('--------------------------------------------------------------------------------')
    execution_time_script = round(total_time / nano, precision)
    print("Execution time of script:", execution_time_script, "s")
    file_list = get_code_files()
    no_files = len(file_list)
    time_per_file = round(total_time / no_files / nano, precision)
    print("Execution time per file", time_per_file, "s")
    total_get_write_problem_link_time = 0
    for exec_time1 in global_vars.GET_WRITE_PROBLEM_LINK_TIMES:
        total_get_write_problem_link_time += exec_time1
    avg_get_write_problem_link_time = round(
        total_get_write_problem_link_time / no_files / nano, precision)
    print("Average time to get or write problem link to file:",
          avg_get_write_problem_link_time, "s")
    total_get_domains_time = 0
    for exec_time2 in global_vars.GET_DOMAINS_TIMES:
        total_get_domains_time += exec_time2
    avg_get_domains_time = round(
        total_get_domains_time / no_files / nano, precision)
    print("Average time to get domains:", avg_get_domains_time, "s")
    total_get_difficulty_time = 0
    for exec_time3 in global_vars.GET_DIFFICULTY_TIMES:
        total_get_difficulty_time += exec_time3
    avg_get_difficulty_time = round(
        total_get_difficulty_time / no_files / nano, precision)
    print("Average time to get difficulty:", avg_get_difficulty_time, "s")
    total_get_solved_date_time = 0
    for exec_time4 in global_vars.GET_SOLVED_DATE_TIMES:
        total_get_solved_date_time += exec_time4
    avg_get_solved_date_time = round(
        total_get_solved_date_time / no_files / nano, precision)
    print("Average time to get solved date time:",
          avg_get_solved_date_time, "s")
    total_get_instructions_time = 0
    for exec_time5 in global_vars.GET_INSTRUCTIONS_TIMES:
        total_get_instructions_time += exec_time5
    avg_get_instructions_time = round(
        total_get_instructions_time / no_files / nano, precision)
    print("Average time to get instructions:", avg_get_instructions_time, "s")

def convert_to_html_table():
    csv_filename = 'items.csv'
    html_filename = 'problem_list2.html'
    html_file = open(html_filename, 'w')
    html_file.close()
    df = pandas.read_csv(csv_filename, index_col=0, delimiter=',')
    print(df)
    df.drop(index=[0, 1])
    df.to_html(html_filename)

def main():
    total_time_start = time.perf_counter_ns()
    # files_to_push()
    problem_list = process_problems()
    write_to_csv(problem_list)
    total_time_end = time.perf_counter_ns()
    total_time = total_time_end - total_time_start
    print_statistics(total_time)
    convert_to_html_table()

main()
