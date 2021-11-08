import os
import re  # for sorting files
import subprocess
import sys
import time

from global_vars import FOLDER, PROBLEMS, DIFFICULTY_PROMPT
from internet import get_problem_link_HTML
from problem_list import GET_CODE_FILES_TIMES

FILE_LIST = FOLDER + '/' + 'file_list.txt'
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


def get_code_files():
    """
    Gets file paths of code files in all subdirectories
    :returns: list of file paths
    """
    get_code_files_time_start = time.perf_counter()
    print("Get file paths...")
    process = subprocess.Popen("git pull", stdout=subprocess.PIPE)
    result = list()
    no_files = 0
    file_extensions = ['.java', '.py']

    for _, _, files in os.walk(PROBLEMS):
        for entry in files:
            for ext in file_extensions:
                if entry.endswith(ext):
                    no_files += 1

    import_module(MISC_PATH)
    import fileUtil
    if (os.path.exists(FILE_LIST) and fileUtil.file_lines(FILE_LIST) == no_files):
        # file list exists and contains correct number of lines
        with open(FILE_LIST, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                result.append(line)
    else:
        for root, _, files in os.walk(PROBLEMS):
            for entry in files:
                for ext in file_extensions:
                    if entry.endswith(ext):
                        entry = os.path.join(root, entry)
                        result.append(entry)
        import masterUtil
        result = masterUtil.sort_logically(result)
        with open(FILE_LIST, 'w') as f:
            for res in result:
                f.write(res)
    get_code_files_time_end = time.perf_counter()
    GET_CODE_FILES_TIMES = get_code_files_time_end - get_code_files_time_start
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
        first_line = lines[0]
        if first_line == '#!/usr/bin/env python3':
            if not lines[1].startswith('#https://www.hackerrank.com/'):
                link, success = get_problem_link_HTML(index, file_path)
                if success is True:
                    write_link = '#' + link
                    write_string_to_file(
                        file_path, write_link, LINK_LINE_NUMBER)
                return link, success
            else:  # first line is shebang, second line is link
                link = lines[1]
                success = True
                return link, success
        else:  # first line is not a shebang
            import_module(MISC_PATH)
            import fileUtil
            fileUtil.write_shebang(file_path, 3)
            # second line is a link
            if lines[1].startswith('#https://www.hackerrank.com/'):
                link = lines[1]
                link = link[1:]  # remove comment sign ('#') from link
                success = True
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
    :returns: difficulty (string) or None
    """
    file_lines = list()
    found = False
    # search for difficulty in file
    try:
        with open(file, 'r') as f:
            for line in f:
                file_lines.append(line)
    except IOError:
        return None
    difficulty = file_lines[DIFFICULTY_LINE_NUMBER - 1]
    if difficulty.startswith(DIFFICULTY_PROMPT):
        found = True
        difficulty = difficulty.rstrip('\n')
        file_difficulty = difficulty[14:]
        return file_difficulty
    return None