import os
from bs4 import BeautifulSoup  # for getting HTML elements of website
import re # for cleaning filename

from global_vars import HTML_FOLDER, SPECIAL_FILE

def get_HTML_path(domain, subdomain):
    # get correct HTML file
    if domain == 'Tutorials':
        html_file_path = os.path.join(HTML_FOLDER, domain, subdomain + ".html")
    else:
        html_file_path = os.path.join(HTML_FOLDER, domain + ".html")
    for root, _, files in os.walk(HTML_FOLDER):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(path):
                if path.endswith('.html'):
                    if path == html_file_path:
                        return html_file_path
    return None


def get_index_html(filename, soup):
    """
    Gets the index of a problem title in the HTML file

    :param filename: name of problem file
    :type filename: string
    :param soup: HTML
    :type soup: beautifulsoup item
    :return: index of file in HTML, None if index was not found
    :rtype: int, None
    """
    challenge_titles = soup.find_all(class_='challengecard-title')
    challenge_titles_list = []
    for item in challenge_titles:
        challenge_titles_list.append(item.find(text=True, recursive=False))
    filename_without_ext = filename.split('.')[0]
    if filename_without_ext.startswith("Python -"):
        filename_without_ext = filename_without_ext.replace(' -', ':', 1)
    pattern = 'Day [0-9]+'
    if re.search(pattern, filename):
        filename_without_ext = filename_without_ext.replace(' -', ':', 1)
    comma_count_filename = filename_without_ext.count(',')
    for title in challenge_titles_list:
        title_index = challenge_titles_list.index(title)
        if filename == SPECIAL_FILE:
            if filename_without_ext.lower() in title.lower():
                return title_index
        title = title.replace('.', '')
        title = ' '.join(title.split()) # delete unneccessary spaces
        comma_count_title_name = title.count(',')
        comma_diff = comma_count_title_name - comma_count_filename
        if comma_diff == -1 or comma_diff == 1:
            filename_without_ext = filename_without_ext.replace(',', '')
            title = title.replace(',', '')
        if filename_without_ext.lower() == title.lower():
            return title_index
    return None

def get_problem_link_HTML(index, file_path):
    """
    Get the problem link from a HTML file

    :param index: index of file in file list (for displaying progress)
    :type index: int
    :param file_path: path to problem file
    :type file_path: string
    :raises NotImplementedError: when problem file is in a not recognized folder
    :raises FileNotFoundError: when HTML file could not be found
    :return: link to problem description on the internet or None, success
    :rtype: string, None, boolean
    """
    domain = file_path.split(os.path.sep)[2]
    subdomain = file_path.split(os.path.sep)[3]
    html_file_path = get_HTML_path(domain, subdomain)
    link = None
    if html_file_path is not None:
        # search for link
        filename = file_path.split(os.path.sep)[-1]
        open_html_file = open(html_file_path, 'r')
        soup = BeautifulSoup(open_html_file, 'html.parser')
        challenge_list_items = soup.find_all('a', attrs={'class': 'challenge-list-item'})
        idx = get_index_html(filename, soup)
        open_html_file.close()
        if idx is not None:
            link = challenge_list_items[idx]['href']
            if link is not None:
                link = link.split('?')[0]
                success = True
                return link, success
            else:
                success = False
                return link, success
        else:
            success = False
            return link, success
    else: # HTML file not found
        raise FileNotFoundError("Corresponding HTML file for " + file_path + " wasn't found.")

def get_domains(file):
    """
    Gets the domain hierarchy of a HackerRank problem (maximum depth = 3)
    :returns: domain, subdomain
    """
    print("Get domains ...")
    domain_list = file.split(os.path.sep)
    domain = domain_list[2]
    if len(domain_list) > 3:
        subdomain = domain_list[3]
    else: # only domain present
        subdomain = None
    return domain, subdomain

def get_difficulty_HTML(file, soup):
    """
    Gets the difficulty of a HackerRank problem from the corresponding HTML

    :param file: file path of problem file
    :type file: string
    :param soup: HTML
    :type soup: beautifulsoup object
    """
    # Extract problem title from filename
    filename = file.split(os.path.sep)[-1].split('.')[0]
    idx = get_index_html(filename, soup)
    if idx is not None:
        challenge_difficulties = soup.find_all(class_='difficulty')
        challenge_difficulties_list = []
        for item in challenge_difficulties:
            challenge_difficulties_list.append(item.find(text=True, recursive=False))
        html_difficulty = challenge_difficulties_list[idx]
        return html_difficulty
    else:
        return None