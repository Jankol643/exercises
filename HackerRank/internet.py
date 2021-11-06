import os
from datetime import datetime as DateTime, timedelta as TimeDelta  # for setting timeout
import time
import mechanize  # for opening browser
# for random user agent when scraping website
from random_user_agent.user_agent import UserAgent
from bs4 import BeautifulSoup  # for getting HTML elements of website
import re  # for pattern matching of Selenium driver
# for logging into website
from selenium import webdriver

from global_vars import FOLDER

PATH = FOLDER + '/' + 'access_time.txt'
TIMEOUT = 5  # in seconds
# regular expression for Selenium webdriver
WEBDRIVER_REGEX = '\/webdriver\/.*\/chromedriver.exe'


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


def open_browser(link):
    """
    Open a browser and returns the HTML
    :string link: link to return HTML from
    :returns: HTML of given link
    """
    br = mechanize.Browser()
    # br.set_handle_robots(False)
    # br.set_handle_equiv(False)
    br.addheaders = [set_random_user_agent()]
    handle_timeout()
    response = br.open(link)

    now = DateTime.now()
    with open(PATH, 'w') as file:
        file.write(now)

    soup = BeautifulSoup(response.get_data())
    return soup


def get_webdriver_path():
    """
    Gets the path to the web driver required by Selenium
    :returns 
    """
    driver_folder = FOLDER.replace("\\", '/') + '/webdriver/'
    regex = re.compile(WEBDRIVER_REGEX)
    for root, _, files in os.walk(driver_folder):
        for entry in files:
            entry = os.path.join(root, entry)
            entry = entry.replace("\\", '/')
            if regex.search(entry) is not None:
                return entry
    raise FileNotFoundError


def login():
    """
    Logs into Hackerrank.com
    """
    print("Logging into hackerrank.com...")
    url = "https://www.hackerrank.com/auth/login"
    result = list()

    # get credentials from file
    with open('.credentials.txt', 'r') as file:
        for line in file:
            result.append(line)
    username_string = result[0]
    username_string = username_string[8:]
    password_string = result[1]
    password_string = password_string[8:]

    path = get_webdriver_path()
    browser = webdriver.Chrome(path)
    browser.get((url))
    time.sleep(3)
    username = browser.find_element_by_id('input-6')  # username field
    username.send_keys(username_string)
    password = browser.find_element_by_id('input-7')  # password field
    password.send_keys(password_string)
    login_button = browser.find_element_by_css_selector(
        "button[data-analytics='LoginPassword']")
    login_button.click()


def logout():
    """
    Logs out of HackerRank
    """
    print("Logging out of hackerrank.com...")
    path = get_webdriver_path()
    browser = webdriver.Chrome(path)
    url = 'https://www.hackerrank.com/dashboard'
    browser.get((url))
    profile_dropdown = browser.find_element_by_css_selector(
        "div[data-analytics='NavBarProfileDropdown']")
    profile_dropdown.click()
    logout_button = browser.find_element_by_css_selector(
        "button[data-analytics='NavBarProfileDropdownLogout']")
    logout_button.click()


def get_problem_link_URL(index):
    """
    Gets the problem link for a given file
    """
    print("Get link from URL for file" + str(index) + "...")
    url = 'https://www.hackerrank.com/domains/tutorials/30-days-of-code'
    browser = navigate_overview()
    browser.get(url)
    divs = browser.find_element_by_class_name('challenges-list')
    for div in divs:
        if divs.index(div) == index:
            div.click()
            time.sleep(4)
            link = browser.current_url
            head, _, _ = link.partition('?')
            link = head
            success = True
            return link, success
    link = None
    success = False
    return link, success


def navigate_overview():
    folder = FOLDER.replace("\\", '/') + '/problems/'
    list_subfolders_with_paths = [
        f.name for f in os.scandir(folder) if f.is_dir()]
    for dir in list_subfolders_with_paths:
        if dir == '30 days of Code':
            path = get_webdriver_path()
            browser = webdriver.Chrome(path)
            return browser
