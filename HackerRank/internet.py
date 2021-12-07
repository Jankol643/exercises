import os
from bs4 import BeautifulSoup  # for getting HTML elements of website

from global_vars import HTML_FOLDER

def get_HTML_path(domain, subdomain):
    # get correct HTML file
    if domain == 'Tutorials':
        html_file_path = os.path.join(HTML_FOLDER, domain, subdomain + ".html")
    else:
        html_file_path = os.path.join(HTML_FOLDER, domain + ".html")
    for path in os.listdir(HTML_FOLDER):
        full_path = os.path.join(HTML_FOLDER, path)
        if os.path.isfile(full_path):
            if full_path.endswith('.html'):
                if full_path == html_file_path:
                    print("Found html", html_file_path)
                    return html_file_path
    return None


def get_problem_link_HTML(index, file_path):
    """
    Get the problem link from a HTML file

    :param index: index of file in file list
    :type index: int
    :param file_path: path to problem file
    :type file_path: string
    :raises NotImplementedError: when problem file is in a not recognized folder
    :raises FileNotFoundError: when HTML file could not be found
    :return: link to problem description on the internet or None, success
    :rtype: string, None, True/False
    """
    print("Get link for file " + str(index) + " (" + str(file_path) + ")" + " ...")
    html_file_path = get_HTML_path(file_path)
    link = None
    if html_file_path is not None:
        # search for link
        filename = file_path.split(os.path.sep)[-1]
        open_html_file = open(html_file_path, 'r')
        soup = BeautifulSoup(open_html_file, 'html.parser')
        challenge_list_items = soup.find_all('a', attrs={'class': 'challenge-list-item'})
        challenge_titles = soup.find_all(class_='challengecard-title')
        challenge_titles_list = []
        for item in challenge_titles:
            challenge_titles_list.append(item.find(text=True, recursive=False))
        filename_without_ext = filename.split('.')[0]
        for item in challenge_list_items:
            item_index = challenge_list_items.index(item)
            file_name_html = challenge_titles_list[item_index]
            chars_to_replace = [':']
            for char in chars_to_replace:
                file_name_html.replace(char, '')
            if filename_without_ext.lower() in file_name_html.lower():
                link = challenge_list_items[item_index]['href']
                break

        open_html_file.close()
        if link is not None:
            link = link.split('?')[0]
            success = True
            return link, success
        else:
            success = False
            return link, success
    else: # HTML file not found
        raise FileNotFoundError("Corresponding HTML file for " + file_path + " wasn´t found.")

def get_domains(file):
    """
    Gets the domain hierarchy of a HackerRank problem (maximum depth = 3)
    :returns: domain, subdomain
    """
    print("Get domains for file " + file + "...")
    domain_list = list()
    domain_list.append(file.split(os.path.sep))
    domain = domain_list[2]
    if len(domain_list) > 3:
        subdomain = domain_list[3]
    else: # only domain present
        subdomain = None
    return domain, subdomain

def get_html_difficulty(file, soup):
    """
    Gets the difficulty of a HackerRank problem from the corresponding HTML

    :param file: file path of problem file
    :type file: string
    :param soup: HTML
    :type soup: beautifulsoup object
    """
    # Extract problem title from filename
    title = file.split(os.path.sep)[-1].split('.')[0]
    div = soup.find_all('div', attrs={'class': 'card-details'})[index]
    first_child = next(div.children, None)
    html_difficulty = first_child.text.strip()    
    return html_difficulty