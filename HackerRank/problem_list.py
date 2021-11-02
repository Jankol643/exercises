import os

import mechanize  # for scraping website for difficulty
# for random user agent when scraping website
from random_user_agent.user_agent import UserAgent
from datetime import datetime as DateTime, timedelta as TimeDelta  # for setting timeout
from bs4 import BeautifulSoup  # for getting HTML elements of website
import csv

PATH = "access_time.txt"
TIMEOUT = 60  # in seconds
DATAPATH = 'items.csv'


class HackerRankProblem():
    def __init__(self, id, link, domain, subdomain, subsubdomain, difficulty, solved_date):
        self.id = id
        self.link = link
        self.domain = domain
        self.subdomain = subdomain
        self.subsubdomain = subsubdomain
        self.difficulty = difficulty
        self.solved_date = solved_date


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

    def raise_exception(last_execution, next_execution, first_execution):
        """
        Raises an exception if website would be scraped too often
        :datetime last_execution: date and time of last execution
        :datetime next_execution: date and time of next execution
        :boolean first_execution: True if script is executed for the first time
        :raises Exception: last execution is before next execution and first_execution is false
        """
        if (last_execution < next_execution and first_execution == False):
            duration = (next_execution - last_execution).total_seconds()
            msg = "Execution is only allowed every " + \
                str(TIMEOUT) + " seconds to not disrupt the website. Next execution: " + \
                str(next_execution) + "(in " + str(duration) + " seconds)"
            raise Exception(msg)

    last_execution = DateTime.strptime(last_execution, '%Y-%m-%d %H:%M:%S.%f')
    next_execution = last_execution + TimeDelta(seconds=TIMEOUT)

    #raise_exception(last_execution, next_execution, first_execution)


def get_code_files():
    """
    Gets file paths of code files in all subdirectories
    :returns: list of file paths
    """
    result = list()
    path = os.path.dirname(os.path.abspath(__file__))
    file_extensions = ['.java', '.py']
    with os.scandir(path) as it:
        for entry in it:
            for ext in file_extensions:
                if entry.name.endswith(ext) and entry.is_file():
                    result.append(entry.path)
    return result


def check_problem_links():
    """
    Reads problem link from each code file
    :returns: list of links, errors
    """
    files = get_code_files()
    links = dict()
    errors = dict()

    for file in files:
        try:
            with open(file, 'r') as f:
                first_line = f.readline()
            links[file] = first_line
        except IOError:
            errors[file] = IOError

    return links, errors


def process_links():
    """
    Converts all problems to objects
    """
    links, errors = check_problem_links()
    running_id = 0
    for link in links:
        soup = open_browser(link)
        domain, subdomain, subsubdomain = get_domains(soup)
        difficulty = get_difficulty(soup)

        running_id += 1

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
        file.write()

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


def get_solved_date():
    


def write_to_csv(problem_list):
    try:
        with open(DATAPATH, 'w') as f:
            writer = csv.writer(f)
            for item in problem_list:
                writer.writerow([item.id, item.name, item.category])
    except BaseException as e:
        print('BaseException:', DATAPATH)
    else:
        print('Data has been loaded successfully !')


def main():
    process_links()


main()
