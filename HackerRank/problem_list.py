import os
import global_vars
import problem_fileUtil
from internet import get_HTML_path, get_domains, get_difficulty_HTML
import git  # for checking if there are uncommitted files
from bs4 import BeautifulSoup
import time  # for calculating execution time
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
    def __init__(self, problem_id, link, domain, subdomain, difficulty, solved_date, instruction):
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
        self.difficulty = difficulty
        self.solved_date = solved_date
        self.instruction = instruction


def process_problems():
    """
    Converts all problems to objects
    """
    problem_fileUtil.clean_HTML_folder()
    errors = list()
    problem_list = list()
    file_paths = problem_fileUtil.get_code_files()
    running_id = 0
    length = len(file_paths)
    for file in file_paths:
        index = file_paths.index(file)
        print("Converting file " + str(index + 1) + " of " + str(length))
        get_write_problem_link_time_start = time.perf_counter_ns()
        link, success = problem_fileUtil.get_write_problem_link(file, index)
        get_write_problem_link_time_end = time.perf_counter_ns()
        total_time = get_write_problem_link_time_end - get_write_problem_link_time_start
        global_vars.GET_WRITE_PROBLEM_LINK_TIMES.append(total_time)
        if success is False:
            errors.append(file)
        get_domains_times_start = time.perf_counter_ns()
        domain, subdomain = get_domains(file)
        get_domains_times_end = time.perf_counter_ns()
        time_spent = get_domains_times_end - get_domains_times_start
        global_vars.GET_DOMAINS_TIMES.append(time_spent)
        #solved_date = problem_fileUtil.get_solved_date(file)
        solved_date = None
        instruction = get_instructions(file)
        if instruction is not None:
            instruction = '\"' + instruction + '\"'
        difficulty = get_difficulty(file, domain, subdomain)
        problem = HackerRankProblem(
            running_id, link, domain, subdomain, difficulty, solved_date, instruction)
        problem_list.append(problem)
        running_id += 1
        print('----------------------------------------------')
    if len(errors) > 0:
        print("Errors occured in following files: ")
        for item in errors:
            print(item)
    return problem_list


def get_difficulty(file, domain, subdomain):
    """
    Gets the difficulty of a HackerRank problem
    :returns: difficulty (string)
    """
    get_difficulty_start = time.perf_counter_ns()
    print("Get difficulty for " + file + "...")
    file_difficulty = problem_fileUtil.get_file_difficulty(file)
    html_file_path = get_HTML_path(domain, subdomain)
    if html_file_path is not None:
        open_html_file = open(html_file_path, 'r')
        soup = BeautifulSoup(open_html_file, 'html.parser')
        # search for difficulty in HTML file
        html_difficulty = get_difficulty_HTML(file, soup)
        if file_difficulty is not None:
            if html_difficulty is None:
                get_difficulty_end = time.perf_counter_ns()
                time_spent = get_difficulty_end - get_difficulty_start
                global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
                return file_difficulty
            else:
                if html_difficulty != file_difficulty:
                    problem_fileUtil.correct_file_difficulty(file, html_difficulty)
                get_difficulty_end = time.perf_counter_ns()
                time_spent = get_difficulty_end - get_difficulty_start
                global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
                return html_difficulty
        else:
            # difficulty not found in file
            html_difficulty = get_difficulty_HTML(file, soup)
            get_difficulty_end = time.perf_counter_ns()
            time_spent = get_difficulty_end - get_difficulty_start
            global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
            return html_difficulty
    else:  # HTML not found
        # get difficulty from file only
        if file_difficulty is not None:
            get_difficulty_end = time.perf_counter_ns()
            time_spent = get_difficulty_end - get_difficulty_start
            global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
            return file_difficulty
        else:
            # html and file difficulty not found
            get_difficulty_end = time.perf_counter_ns()
            time_spent = get_difficulty_end - get_difficulty_start
            global_vars.GET_DIFFICULTY_TIMES.append(time_spent)
            return None


def get_instructions(file):
    """
    Gets the instructions for a HackerRank problem if not present
    :string file: path to problem file
    :returns: path to instruction file
    """
    get_instructions_start = time.perf_counter_ns()
    print("Get instruction file for " + file + "...")
    filename_with_ext = file.split(os.path.sep)[-1]
    filename_no_ext = filename_with_ext.split('.')[0].replace('\'', '').replace('!', '')
    pattern = 'Day [0-9]+'
    pattern2 = '[A-Za-z]+-[A-Za-z]+'
    if re.search(pattern, filename_no_ext) is None and re.search(pattern2, filename_no_ext) is not None:
        filename_no_ext = filename_no_ext.replace('-', ' ')
    filename_no_ext = ' '.join(filename_no_ext.split()) # delete unneccessary spaces
    full_path = os.path.dirname(file) + os.path.sep + "instructions" + os.path.sep
    if os.path.isdir(full_path):
        for item in os.listdir(full_path):
            path = os.path.join(full_path, item)
            if os.path.isfile(path):
                item = item.replace('-English', '')
                if re.search(pattern, item) is None and re.search(pattern2, item) is not None:
                    item = item.replace('-', ' ')
                item = ' '.join(item.split()) # delete unneccessary spaces
                item_no_ext = item.split('.')[0]
                if filename_no_ext.lower() in item_no_ext.lower() and item.endswith('.pdf'):
                    get_instructions_end = time.perf_counter_ns()
                    time_spent = get_instructions_end - get_instructions_start
                    global_vars.GET_INSTRUCTIONS_TIMES.append(time_spent)
                    return path
        get_instructions_end = time.perf_counter_ns()
        time_spent = get_instructions_end - get_instructions_start
        global_vars.GET_INSTRUCTIONS_TIMES.append(time_spent)
        return None
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
                0, 'http', 'domain', 'subdomain', 'Easy', '14.3.21', 'link')
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


def print_statistics(total_time):
    nano = 1000000000
    precision = 3
    print('--------------------------------------------------------------------------------')
    execution_time_script = round(total_time / nano, precision)
    print("Execution time of script:", execution_time_script, "s")
    file_list = problem_fileUtil.get_code_files()
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


if __name__ == '__main__':
    total_time_start = time.perf_counter_ns()
    # files_to_push()
    problem_list = process_problems()
    write_to_csv(problem_list)
    total_time_end = time.perf_counter_ns()
    total_time = total_time_end - total_time_start
    print_statistics(total_time)
