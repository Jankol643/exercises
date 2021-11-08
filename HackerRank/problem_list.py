import os
import subprocess
from datetime import datetime as DateTime
from file import get_file_difficulty
from global_vars import DIFFICULTY_PROMPT  # for getting solved date
from file import get_code_files, get_write_problem_link, correct_file_difficulty, write_string_to_file
from internet import get_HTML_path, get_domains
import platform  # for determinating file creation date
import git  # for checking if there are uncommitted files
from global_vars import PROBLEMS, DATE, DATETIME_FORMAT, DATAPATH
from file import DIFFICULTY_LINE_NUMBER
from bs4 import BeautifulSoup


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
    errors = list()
    problem_list = list()
    file_paths = get_code_files()
    running_id = 0
    length = len(file_paths)
    for file in file_paths:
        index = file_paths.index(file)
        print("Converting file " + str(index) + " of " + str(length))
        link, success = get_write_problem_link(file, index)
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
            domain, subdomain, subsubdomain = get_domains(file, soup)
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
    return problem_list


def get_difficulty(file, index, soup):
    """
    Gets the difficulty of a HackerRank problem
    :returns: difficulty (string)
    """
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
        difficulty_dict_reversed = {y:x for x,y in difficulty_dict.items()}
        master_difficulty = difficulty_dict_reversed.get(int_html_difficulty)
        return master_difficulty
    else: # difficulty not found in file
        # get difficulty from HTML only
        div = soup.find_all('div', attrs={'class': 'card-details'})[index]
        first_child = next(div.children, None)
        html_difficulty = first_child.text
        difficulty = DIFFICULTY_PROMPT + html_difficulty + '\n'
        write_string_to_file(file, difficulty, DIFFICULTY_LINE_NUMBER)
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
    print("Get solved date for file " + file)
    if DATE not in ['creation', 'last modification', 'first commit']:
        raise ValueError()
    if DATE == 'creation':
        date = get_creation_date(file)
        return str(date)
    elif DATE == 'last modified':
        process = subprocess.Popen("git pull", stdout=subprocess.PIPE)

        command = 'git log --follow -p -- ' + "\"" + file + "\""
        p = subprocess.check_output(command, cwd=PROBLEMS, shell=True)

        p = p.decode('utf-8')
        p = p.split('\n')[2]
        p = p[8:]
        dt = DateTime.strptime(p, DATETIME_FORMAT)
        return str(dt)
    elif DATE == 'first commit':
        command = 'git log --diff-filter=A --follow --format=%aI -1 -p -- ' + "\"" + file + "\""
        date = subprocess.check_output(command, cwd=PROBLEMS, shell=True)
        date = date.decode('utf-8')
        date = date.split('\n')[0]
        length = len(date)
        date = date[0:-3] + date[-2:] # delete colon between timezone
        length = len(date)
        for i in range(length):
            if(date[i] == 'T'):
                date = date[0:i] + ' ' + date[i + 1:length-5] # replace T with space and cut timezone
                break
        date_obj = DateTime.strptime(date, DATETIME_FORMAT)
        return str(date_obj)

def get_instructions(file):
    """
    Gets the instructions for a HackerRank problem if not present
    :string file: path to problem file
    :returns: path to instruction file
    """
    print("Get instruction file for " + file + "...")
    file_name = file.split(os.path.sep)[-1]
    file_name_no_ext = os.path.splitext(file_name)[0]
    instruction_path = "." + os.path.sep + "instructions" + \
        os.path.sep + file_name_no_ext + ".pdf"
    print(instruction_path)
    full_path = PROBLEMS + instruction_path
    if os.path.exists(full_path):
        return instruction_path
    else:
        return None


def write_to_csv(problem_list):
    """
    Writes the problem list to a csv file
    :list problem_list: list of HackerRankProblem objects
    """
    print("Writing problems to file...")
    try:
        with open(DATAPATH, 'w') as f:
            # write column names to file
            result = list()
            dummy_obj = HackerRankProblem(0, 'http', 'domain', 'test', 'test', 'Easy', '14.3.21', 'link')
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
    except IOError:
        print('IOError occured while accessing', DATAPATH)
    except Exception:
        raise Exception()


def main():
    # files_to_push()
    problem_list = process_problems()
    write_to_csv(problem_list)


main()
