import os
from bs4 import BeautifulSoup  # for getting HTML elements of website

from global_vars import FOLDER

def get_HTML_path(code_folder):
    # get correct HTML file
    html_file_name = code_folder + ".html"
    subfolder = ['HTML']
    subfolder = os.path.join(*subfolder)
    folder = FOLDER + os.path.sep + subfolder
    html_file_path = None
    for path in os.listdir(folder):
        full_path = os.path.join(folder, path)
        if os.path.isfile(full_path):
            if path.endswith('.html'):
                if path == html_file_name:
                    html_file_path = full_path
                    return html_file_path
    return html_file_path


def get_problem_link_HTML(index, file_path):
    """
    Gets the problem link for a given file
    """
    print("Get link for file " + str(index) + "(" + str(file_path) + ")" + " ...")
    splitted_path = file_path.split(os.path.sep)
    code_folder = splitted_path[len(splitted_path) - 2] # penultimate element in file path
    html_file_path = get_HTML_path(code_folder)
    link = None
    if html_file_path is not None:
        # search for link
        open_html_file = open(html_file_path, 'r')
        soup = BeautifulSoup(open_html_file, 'html.parser')
        if code_folder == '30 days of Code':
            challenge_list_items = soup.find_all('a', attrs={'class': 'challenge-list-item'})
            for item in challenge_list_items:
                item_index = challenge_list_items.index(item)
                if index == item_index:
                    link = challenge_list_items[item_index]['href']
                    break
        else:
            open_html_file.close()
            raise NotImplementedError("Support for " + code_folder + " hasn´t been implemented yet.")

        open_html_file.close()
        if link is not None:
            link = link.split('?')[0]
            success = True
            return link, success
        else:
            success = False
            return link, success
    else: # HTML file not found
        raise FileNotFoundError("Corresponding HTML file for " + code_folder + " wasn´t found.")

def get_domains(file, soup):
    """
    Gets the domain hierarchy of a HackerRank problem (maximum depth = 3)
    :returns: domain, subdomain, subsubdomain
    """
    print("Get domains for file " + file + "...")
    domain_list = list()
    spans = soup.find_all(
        'span', attrs={'class': 'breadcrumb-item-text'})
    for span in spans:
        domain_list.append(span.get_text(strip=True))
    domain = domain_list[0]
    if len(domain_list) > 1:
        subdomain = domain_list[1]
        if len(domain_list) > 2:
            subsubdomain = domain_list[2]
        else: # only domain and subdomain present
            subsubdomain = None
    else: # only domain present
        subdomain = None
        subsubdomain = None
    return domain, subdomain, subsubdomain