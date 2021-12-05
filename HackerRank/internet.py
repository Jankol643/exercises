import os
from bs4 import BeautifulSoup  # for getting HTML elements of website

from global_vars import HTML_FOLDER

def get_HTML_path(file_path):
    # get correct HTML file
    splitted_path = file_path.split(os.path.sep)
    domain = splitted_path[-3]
    subdomain = splitted_path[-2] # penultimate element in file path
    if domain == 'Tutorials' and subdomain == '30 days of Code':
        html_file_path = os.path.join(HTML_FOLDER, domain, subdomain + ".html")
    else:
        html_file_path = os.path.join(HTML_FOLDER, domain + ".html")
    for path in os.listdir(HTML_FOLDER):
        full_path = os.path.join(HTML_FOLDER, path)
        if os.path.isfile(full_path):
            if path.endswith('.html'):
                if path == html_file_path:
                    html_file_path = full_path
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
        for item in challenge_list_items:
            item_index = challenge_list_items.index(item)
            file_name_html = challenge_titles[item_index].string
            if filename.lower() in file_name_html.lower():
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