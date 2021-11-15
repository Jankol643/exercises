import os # for checking if path exists
import re  # for importing module
import subprocess # for getting newest files
import sys # for appending to path
import platform # for detecting os
from datetime import datetime # for converting to datetime

import global_vars # for global variables
from internet import get_problem_link_HTML # for getting problem link from HTML

FILE_LIST = global_vars.FOLDER + '/' + 'file_list.txt'
MISC_PATH = '.\\..\\..\\Misc\\'
LINK_LINE_NUMBER = 2  # link should be written on second line of file
DIFFICULTY_LINE_NUMBER = 3  # difficulty should be written on third line of file


def import_module(file_path):
    """
    Imports the module specified in the relative path

    :string file_path: relative path to file
    """
    final_path = ''
    current_path = os.path.dirname(os.path.realpath(__file__))
    splitted = current_path.split(os.path.sep)
    no_points = file_path.count('..')
    count = len(splitted) - no_points
    splitted = splitted[:count]
    splitted_filepath = file_path.split(os.path.sep)
    filename = splitted_filepath[-1]
    regexPattern = re.compile('(?<!\.)\.(?!\.)')  # matches single dot
    no_points_filename = len(regexPattern.findall(filename))
    no_single_points = len(regexPattern.findall(file_path))
    count = no_points + no_single_points - no_points_filename
    splitted_filepath = splitted_filepath[count:]
    final_path_list = splitted + splitted_filepath
    string = ''
    for elem in final_path_list:
        if final_path_list.index(elem) == len(final_path_list)-1:
            string += elem
        else:
            string += elem + os.path.sep
    final_path = string
    sys.path.append(final_path)


def append_files_to_filelist():
    """
    Appends file to a list if they have certain extensions

    :return: list of files
    :rtype: list
    """
    result = list()
    file_extensions = ['.java', '.py']
    for root, _, files in os.walk(global_vars.PROBLEMS):
        for entry in files:
            for ext in file_extensions:
                if entry.endswith(ext):
                    result.append(entry)
    return result


def get_code_files():
    """
    Gets file paths of code files in all subdirectories

    :returns: list of file paths
    """
    args = ['git', 'pull']
    subprocess.Popen(args, stdout=subprocess.PIPE)
    result = list()

    import_module(MISC_PATH)
    if (os.path.exists(FILE_LIST)):
        with open(FILE_LIST, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                result.append(line)
    else:
        result = append_files_to_filelist()
        import masterUtil
        result = masterUtil.sort_logically(result)
        # ensure that java file with no index in filename is correctly inserted
        java_file_path = result[-1]
        result.remove(java_file_path)
        result.insert(21, java_file_path)

        with open(FILE_LIST, 'w') as f:
            for res in result:
                f.write(res + '\n')
    return result


def write_string_to_file(file_path, string, line_no):
    """
    Write string to file
    :string file_path: file to write to
    :string string: string to write
    :int line_no: line number to write to
    """
    import_module(MISC_PATH)
    import fileUtil
    file_lines = fileUtil.read_file_to_list(file_path, True)

    if file_lines[line_no - 1] == '':
        file_lines[line_no - 1] = string
    else:
        # insert string into desired line of file
        file_lines.insert(line_no - 1, string)
    with open(file_path, 'w') as f:
        for line in file_lines:
            f.write(line + '\n')


def correct_file_link(file_path, html_link):
    import_module(MISC_PATH)
    import fileUtil
    lines = fileUtil.read_file_to_list(file_path, True)
    if lines[LINK_LINE_NUMBER - 1].startswith(global_vars.FILE_LINK_BEGINNING):
        lines[LINK_LINE_NUMBER - 1] = '#' + str(html_link)
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    

def check_links_equal(file_path, lines, index):
    """
    Check if file and HTML have identical links for a problem

    :param file_path: path to file
    :type file_path: string
    :param index: index of problem file
    :type index: int
    """
    file_link = lines[1]
    # check if file link and html link are equal
    html_link, success = get_problem_link_HTML(index, file_path)
    if success is True:
        if file_link == html_link:
            link = file_link[1:]  # remove comment sign ('#') from link
        else:
            correct_file_link(file_path, html_link)
            link = html_link
        return link, success
    else: # could not get link from HTML file
        link = file_link[1:]  # remove comment sign ('#') from link
        if link.startswith(global_vars.FILE_LINK_BEGINNING):
            success = True
        else:
            success = False
        return link, success


def get_write_problem_link(file_path, index):
    """
    Get the problem link for a HackerRank code file and writes it to it if not present
    :string file_path: file path to check
    :int index: index of code file
    :returns: link, success (link is None and success is false if link cannot be found)
    """
    import_module(MISC_PATH)
    import fileUtil
    lines = fileUtil.read_file_to_list(file_path, True)
    if len(lines) > 1:
        if lines[0] == global_vars.SHEBANG:
            if not lines[1].startswith(global_vars.FILE_LINK_BEGINNING):
                html_link, success = get_problem_link_HTML(index, file_path)
                if success is True:
                    write_link = '#' + html_link
                    write_string_to_file(
                        file_path, write_link, LINK_LINE_NUMBER)
                return html_link, success
            else:  # first line is shebang, second line is link
                link, success = check_links_equal(file_path, lines, index)
                return link, success
        else:  # first line is not a shebang
            import_module(MISC_PATH)
            import fileUtil
            fileUtil.write_shebang(file_path, 3)
            if lines[1].startswith(global_vars.FILE_LINK_BEGINNING):
                # second line is a link
                link, success = check_links_equal(file_path, lines, index)
                return link, success
            else:  # second line of file contains no link
                link, success = get_problem_link_HTML(index, file_path)
                if success is True:
                    write_link = '#' + link
                    write_string_to_file(
                        file_path, write_link, LINK_LINE_NUMBER)
                return link, success
    else:  # file has only one line
        link = None
        success = False
        return link, success


def delete_excess_metainfo(file):
    """
    Checks for duplicate metainfo in the file and removes it

    :param file_lines: lines of file
    :type file_lines: list
    :param file: path to file to check
    :type file: string
    :return: lines of file without duplicate metainfo
    :rtype: list
    """
    file_lines = list()
    metainfo = [global_vars.DIFFICULTY_PROMPT, global_vars.FILE_LINK_BEGINNING]
    found = False
    changed = False
    metainfo_tuple = tuple(metainfo)
    with open(file, 'r') as f:
        for line in f:
            file_lines.append(line)

    for line in file_lines:
        if line.startswith(metainfo_tuple):
            if found is True:
                changed = True
                file_lines.remove(line)
                continue
            found = True
            index = file_lines.index(line)
    # difficulty is on wrong line
    if not file_lines[DIFFICULTY_LINE_NUMBER - 1].startswith(global_vars.DIFFICULTY_PROMPT):
        changed = True
        file_lines[DIFFICULTY_LINE_NUMBER - 1] = file_lines[index]
        file_lines.remove(file_lines[index])
    # write changes to file
    if changed is True:
        with open(file, 'w') as f:
            for line in file_lines:
                f.write(line)
    return file_lines


def get_file_difficulty(file):
    """
    Gets the difficulty of a HackerRank problem from file

    :param file: path to problem file
    :type file: string
    :return: difficulty or None
    :rtype: string or None
    """
    file_lines = list()
    # search for difficulty in file
    try:
        with open(file, 'r') as f:
            for line in f:
                file_lines.append(line)
    except IOError:
        return None
    difficulty = file_lines[DIFFICULTY_LINE_NUMBER - 1]
    if difficulty.startswith(global_vars.DIFFICULTY_PROMPT):
        difficulty = difficulty.rstrip('\n')
        file_difficulty = difficulty[14:]
        return file_difficulty
    return None


def correct_file_difficulty(file, correct_difficulty):
    """
    Corrects the difficulty in a given file

    :string file: path to file
    :type file: string
    :string correct_difficulty: difficulty to write to file
    :type correct_difficulty: string
    """
    import_module(MISC_PATH)
    import fileUtil
    lines = fileUtil.read_file_to_list(file, True)
    if lines[DIFFICULTY_LINE_NUMBER - 1].startswith(global_vars.DIFFICULTY_PROMPT):
        lines[DIFFICULTY_LINE_NUMBER - 1] = global_vars.DIFFICULTY_PROMPT + \
            str(correct_difficulty)
    with open(file, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def get_creation_date(filename):
    """
    Gets the creation date and time of a file

    :param filename: path to file
    :type filename: string
    :return: creation time of file or on Linux last modification time
    :rtype: datetime
    """
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
    ts = datetime.fromtimestamp(ts)
    temp = datetime.strftime(ts, global_vars.DATETIME_FORMAT)
    ts = datetime.strptime(temp, global_vars.DATETIME_FORMAT)
    return ts