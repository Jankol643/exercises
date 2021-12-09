import os  # for checking if path exists
import re  # for importing module
import subprocess  # for getting newest files
import sys  # for appending to path
import platform  # for detecting os
from datetime import datetime  # for converting to datetime
from global_vars import HTML_FOLDER, FILE_BEFORE_SPECIAL, SPECIAL_FILE
import time # for measuring execution time

import global_vars  # for global variables
from internet import get_problem_link_HTML  # for getting problem link from HTML

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
    file_extensions = ['.java', '.py', '.sql']
    for root, _, files in os.walk(global_vars.PROBLEMS):
        for entry in files:
            for ext in file_extensions:
                if entry.endswith(ext):
                    path = os.path.join(root, entry)
                    result.append(path)
    # ensure that java file with no index in filename is correctly inserted
    import_module(MISC_PATH)
    import masterUtil
    result = masterUtil.sort_logically(result)
    indices = [i for i, s in enumerate(result) if FILE_BEFORE_SPECIAL in s]
    if len(indices) > 0:
        result2 = result.copy()
        folder_path = result2[indices[0]].split(os.path.sep)[0:-1]
        separator = os.path.sep
        folder_path = separator.join(folder_path)
        java_file_path = folder_path + os.path.sep + SPECIAL_FILE
        result2.insert(int(indices[0]) + 1, java_file_path)
        indices2 = [i for i, s in enumerate(result2) if SPECIAL_FILE in s]
        result2.pop(int(indices2[-1]))
        return result2
    else:
        return result


def get_code_files():
    """
    Gets file paths of code files in all subdirectories

    :returns: list of file paths
    """
    args = ['git', 'pull']
    subprocess.Popen(args, stdout=subprocess.PIPE)
    result = list()
    result = append_files_to_filelist()

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
    """
    Correct the problem link in a file and replace it with the HTML link

    :param file_path: path to problem file
    :type file_path: string
    :param html_link: url to problem
    :type html_link: string
    """
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
    else:  # could not get link from HTML file
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
    print(file_path)
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

def get_solved_date(file):
    """
    Get the solved date of the given file

    :param file: path to problem file
    :type file: string
    :raises ValueError: when wrong datetype is specified (in global constant)
    :return: solved date of problem file
    :rtype: datetime
    """
    get_solved_date_start = time.perf_counter_ns()
    print("Get solved date for file " + file)
    if global_vars.DATE not in ['creation', 'last modification', 'first commit']:
        raise ValueError()
    if global_vars.DATE == 'creation':
        date = get_creation_date(file)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        global_vars.GET_SOLVED_DATE_TIMES.append(time_spent)
        return date
    elif global_vars.DATE == 'last modified':
        args = ['git', 'pull']
        subprocess.Popen(args, stdout=subprocess.PIPE)

        args = ['git', 'log', '--follow', '-- ' + "\"" + file + "\""]
        p = subprocess.check_output(args, cwd=global_vars.PROBLEMS)

        p = p.decode('utf-8')
        p = p.split('\n')[2]
        p = p[8:]
        dt = datetime.strptime(p, global_vars.DATETIME_FORMAT)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        global_vars.GET_SOLVED_DATE_TIMES.append(time_spent)
        return dt
    elif global_vars.DATE == 'first commit':
        command = 'git log --diff-filter=A --follow --format=%aI -1 -- ' + "\"" + file + "\""
        date = subprocess.check_output(command, cwd=global_vars.PROBLEMS)
        temp = date.decode('utf-8')
        temp = temp.split('\n')[0]
        length = len(temp)
        temp = temp[0:-3] + temp[-2:]  # delete colon between timezone
        length = len(temp)
        for i in range(length):
            if(temp[i] == 'T'):
                # replace T with space and cut timezone
                temp = temp[0:i] + ' ' + temp[i + 1:length-5]
                break
        date_obj = datetime.strptime(temp, global_vars.DATETIME_FORMAT)
        get_solved_date_end = time.perf_counter_ns()
        time_spent = get_solved_date_end - get_solved_date_start
        global_vars.GET_SOLVED_DATE_TIMES.append(time_spent)
        return date_obj


def clean_HTML_folder():

    def correct_html_filenames(entry):
        old_path = entry
        # clean filename and folder
        tmp = entry.replace('Solve ', '')
        tmp = tmp.replace(' _ HackerRank', '')
        new_path = tmp
        os.rename(old_path, new_path)

    file_list = []
    dir_list = []
    for root, dirs, files in os.walk(HTML_FOLDER):
        for f in files:
            if f.endswith('.html'):
                file_list.append(os.path.join(root, f))
        for dir in dirs:
            dir_list.append(os.path.join(root, dir))

    for entry in file_list:
        old_name = entry.split(os.path.sep)[-1]
        idx = file_list.index(entry)
        if '_' in old_name:
            if old_name.endswith('.html'):
                # update references
                tmp = old_name.replace('Solve ', '')
                tmp = tmp.replace(' _ HackerRank', '')
                old_without_ext = old_name.split('.')[0]
                tmp_without_ext = tmp.split('.')[0]
                updated_lines = []
                with open(entry, 'r') as f:
                    for line in f:
                        updated_lines.append(line.replace(
                            old_without_ext, tmp_without_ext))

                with open(entry, 'w') as f:
                    for line in updated_lines:
                        f.write(line)

                correct_html_filenames(entry)

    for entry in dir_list:
        old_name = entry.split(os.path.sep)[-1]
        if '_' in old_name:
            correct_html_filenames(entry)
