import os
import subprocess
import requests
from datetime import datetime as DateTime  # for setting timeout
from internet import open_browser  # for opening browser
from file import get_code_files, get_problem_link
import time  # for determinating file creation time

FOLDER = os.path.dirname(os.path.abspath(__file__))
FOLDER = FOLDER.replace("\\", '/')
PROBLEMS = FOLDER + '/problems/'
DATAPATH = FOLDER + '/' + 'items.csv'
FILE_LIST = FOLDER + '/' + 'file_list.txt'
# if creation or last modification ('last modified') date should be set as solved date
DATE = 'creation'


def files_to_push():
    """
    Checks if there are any uncommited files since last commit and aborts program
    """
    command = 'git status'
    p = subprocess.check_output(command, cwd=PROBLEMS, shell=True)
    p = p.decode('utf-8')
    nlines = p.count('\n')
    if nlines > 4:  # output with no uncommitted files is 4
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
    problem_list = list()
    file_paths = get_code_files()
    running_id = 0
    length = len(file_paths)
    for file in file_paths:
        index = file_paths.index(file)
        print("Converting file " + str(index) +
              " of " + str(length) + " files...")
        link, success = get_problem_link(file)
        if success is False:
            break
        soup = open_browser(file)
        domain, subdomain, subsubdomain = get_domains(soup)
        difficulty = get_difficulty(soup)
        solved_date = get_solved_date(file)
        instruction = get_instructions(file)
        problem = HackerRankProblem(
            running_id, link, domain, subdomain, subsubdomain, difficulty, solved_date, instruction)
        problem_list.append(problem)
        running_id += 1
    return problem_list


def get_domains(soup):
    """
    Gets the domain hierarchy of a HackerRank problem (maximum depth = 3)
    :returns: domain, subdomain, subsubdomain
    """
    domain_list = list()

    div = soup.find_all(
        'div', attrs={'class': 'community-header-breadcrumb-items'})[0]
    domains = div.select('div > ol > li > a > span')
    for domain in domains:
        domain_list.append(domain.get_text(strip=True))
    domain = domain_list[0]
    subdomain = domain_list[1]
    subsubdomain = domain_list[2]
    return domain, subdomain, subsubdomain


def get_difficulty(soup):
    """
    Gets the difficulty of a HackerRank problem
    :returns: difficulty (string)
    """
    div = soup.find_all('div', attrs={'class': 'difficulty-block'})[1]
    difficulty = div.select('div > p')[1].get_text(strip=True)
    return difficulty


def get_solved_date(file):
    """
    Get the date the HackerRank problem was solved given by the last commit date
    :string file: file to calculate solved date of
    :returns: solved date (int)
    """
    if DATE == 'creation':
        (mode, ino, dev, nlink, uid, gid, size,
         atime, mtime, ctime) = os.stat(file)
        return str(time.ctime(mtime))
    if DATE == 'last modified':
        process = subprocess.Popen("git pull", stdout=subprocess.PIPE)

        command = 'git log --follow -p -- ' + "\"" + file + "\""
        p = subprocess.check_output(command, cwd=PROBLEMS, shell=True)

        p = p.decode('utf-8')
        p = p.split('\n')[2]
        p = p[8:]
        dtz = DateTime.strptime(p, "%a %b %d %H:%M:%S %Y %z")
        return str(dtz)


def get_instructions(file):
    """
    Gets the instructions for a HackerRank problem if not present
    :string file: path to problem file
    :returns: path to instruction file
    """
    file_name = file.split('/')[-1]
    file_name_no_ext = os.path.splitext(file_name)[0]
    instruction_path = "./instructions/" + file_name_no_ext + ".pdf"
    if not os.path.exists(instruction_path):
        link = get_problem_link(file)
        soup = open_browser(link)
        pdf_link = soup.select('#pdf-link')
        pdf_link = pdf_link['href']
        response = requests.get(pdf_link)

        # save PDF file
        pdf = open(instruction_path, 'wb')
        pdf.write(response.content)
        pdf.close()
    return instruction_path


def write_to_csv(problem_list):
    """
    Writes the problem list to a csv file
    :list problem_list: list of HackerRankProblem objects
    """
    print("Writing problems to file...")
    try:
        with open(DATAPATH, 'w') as f:
            for item in problem_list:
                index = problem_list.index(item)
                print("Writing problem " + str(index) + " to file...")
                d = item.__dict__
                string = ""
                for key, value in d.items():
                    if key == list(d)[-1]:
                        string += str(value)
                    else:
                        string += str(value) + ","
                f.write(string)
    except IOError as error:
        print('IOError occured while accessing', DATAPATH)


def main():
    files_to_push()
    problem_list = process_problems()
    write_to_csv(problem_list)


main()