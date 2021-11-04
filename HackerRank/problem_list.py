import os
import subprocess

import mechanize  # for scraping website for difficulty
# for random user agent when scraping website
from random_user_agent.user_agent import UserAgent
from datetime import datetime as DateTime, timedelta as TimeDelta  # for setting timeout
from bs4 import BeautifulSoup  # for getting HTML elements of website
import requests
import time

FOLDER = os.path.dirname(os.path.abspath(__file__))
FOLDER = FOLDER.replace("\\", '/')
PATH = FOLDER + 'access_time.txt'
TIMEOUT = 5  # in seconds
DATAPATH = FOLDER + 'items.csv'
FILE_LIST = FOLDER + 'file_list.txt'


def files_to_push():
    """
    Checks if there are any uncommited files since last commit and aborts program
    """
    command = 'git status'
    p = subprocess.check_output(command, cwd=FOLDER, shell=True)
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


def set_random_user_agent():
    """
    Sets a random user agent
    :returns: random user agent
    """
    set_popularity = ['POPULARITY.POPULAR.value', 'POPULARITY.COMMON.value']
    user_agent_rotator = UserAgent(Popularity=set_popularity, limit=10000)
    random_user_agent = user_agent_rotator.get_random_user_agent()
    return {'User-Agent': random_user_agent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def handle_timeout():
    """
    Ensures that website is only scraped every TIMEOUT seconds
    """

    if os.path.exists(PATH):
        first_execution = False
        with open(PATH, 'r') as file:
            last_execution = file.readline()
    else:
        first_execution = True
        # create a file
        now = str(DateTime.now())
        with open(PATH, 'w') as file:
            file.write(now)
        last_execution = now

    def prevent_blocking(last_execution, next_execution, first_execution):
        """
        Prevent that website is scraped too often
        :datetime last_execution: date and time of last execution
        :datetime next_execution: date and time of next execution
        :boolean first_execution: True if script is executed for the first time
        """
        if (last_execution < next_execution and first_execution == False):
            print("Waiting " + str(TIMEOUT) +
                  " seconds to not scrape website too often.")
            time.sleep(TIMEOUT)

    last_execution = DateTime.strptime(last_execution, '%Y-%m-%d %H:%M:%S.%f')
    next_execution = last_execution + TimeDelta(seconds=TIMEOUT)

    prevent_blocking(last_execution, next_execution, first_execution)


def file_lines(file_path):
    """
    Counts the number of lines of a file using buffered count
    :string fname: path to file
    :return noLines: number of lines in file
    """
    if os.path.isfile(file_path):
        def _make_gen(reader):
            b = reader(2 ** 16)
            while b:
                yield b
                b = reader(2 ** 16)

        with open(file_path, "rb") as f:
            count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
        noLines = count + 1
        return noLines
    else:
        return 0


def get_code_files():
    """
    Gets file paths of code files in all subdirectories
    :returns: list of file paths
    """
    print("Get file paths...")
    process = subprocess.Popen("git pull", stdout=subprocess.PIPE)
    result = list()
    no_files = 0
    file_extensions = ['.java', '.py']

    for root, dirs, files in os.walk(FOLDER):
        for entry in files:
            for ext in file_extensions:
                if entry.endswith(ext):
                    no_files += 1

    if (os.path.exists(FILE_LIST) and file_lines(FILE_LIST) == no_files):
        with open(FILE_LIST, 'r') as f:
            for line in f:
                line = f.readline()
                result.append(line)
    else:
        for root, dirs, files in os.walk(FOLDER):
            for entry in files:
                for ext in file_extensions:
                    if entry.endswith(ext):
                        entry = os.path.join(root, entry)
                        entry = entry.replace('\\', '/')
                        result.append(entry)

        with open(FILE_LIST, 'w') as f:
            for res in result:
                f.write(res + "\n")
    return result


def check_problem_links():
    """
    Reads problem link from each code file
    :returns: list of links, errors
    """
    files = get_code_files()
    links = list()
    errors = list()

    for file in files:
        link, success = get_problem_link(file)
        if success == True:
            links.append(link)
        else:
            errors.append(file)
    return links, errors


def get_problem_link(file):
    """
    Gets the problem link from a HackerRank code file
    """
    try:
        with open(file, 'r') as f:
            first_line = f.readline()
        link = first_line
        success = True
    except IOError:
        link = None
        success = False
    return link, success


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
              "of " + str(length) + " files...")
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


def open_browser(link):
    """
    Open a browser and returns the HTML
    :string link: link to return HTML from
    """
    br = mechanize.Browser()
    # br.set_handle_robots(False)
    # br.set_handle_equiv(False)
    br.addheaders = [set_random_user_agent()]
    handle_timeout(TIMEOUT, PATH)
    response = br.open(link)

    now = DateTime.now()
    with open(PATH, 'w') as file:
        file.write(now)

    soup = BeautifulSoup(response.get_data())
    return soup


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
    process = subprocess.Popen("git pull", stdout=subprocess.PIPE)

    command = 'git log --follow -p -- ' + "\"" + file + "\""
    p = subprocess.check_output(command, cwd=FOLDER, shell=True)

    p = p.decode('utf-8')
    p = p.split('\n')[2]
    p = p[8:]
    dtz = DateTime.strptime(p, "%a %b %d %H:%M:%S %Y %z")
    return str(dtz)


def get_instructions(file):
    """
    Gets the instructions for a HackerRank problems if not present
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
