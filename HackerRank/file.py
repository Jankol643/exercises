import os
import re  # for sorting files
import subprocess
import sys
from pathlib import Path  # for sorting files

from global_vars import FOLDER, PROBLEMS
from internet import get_problem_link_URL

FILE_LIST = FOLDER + '/' + 'file_list.txt'
FILEUTIL_PATH = '.\\..\\..\\Misc\\'


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


def file_lines(file_path):
    """
    Counts the number of lines of a file using buffered count
    :string fname: path to file
    :returns: number of lines in file
    """
    if os.path.isfile(file_path):
        def _make_gen(reader):
            b = reader(2 ** 16)
            while b:
                yield b
                b = reader(2 ** 16)

        with open(file_path, "rb") as f:
            count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
        no_lines = count + 1
        return no_lines
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

    def sort_logically(result):
        """
        Sorts list like 1, 2, 10 instead of 1, 10, 2
        :list result: list to sort
        :returns: sorted list
        """
        result2 = list()
        for item in result:
            path = Path(item)
            result2.append(path)

        result = sorted(result2, key=lambda x: [
                        int(k) if k.isdigit() else k for k in re.split('([0-9]+)', x.stem)])
        for item in result:
            result[result.index(item)] = str(item)
        return result

    for _, _, files in os.walk(PROBLEMS):
        for entry in files:
            for ext in file_extensions:
                if entry.endswith(ext):
                    no_files += 1

    if (os.path.exists(FILE_LIST) and file_lines(FILE_LIST) == no_files):
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
                        entry = entry.replace('\\', '/')
                        result.append(entry)

        result = sort_logically(result)
        with open(FILE_LIST, 'w') as f:
            for res in result:
                f.write(res + '\n')

    return result


def check_problem_links():
    """
    Reads problem link from each code file
    :returns: list of links, errors
    """
    file_paths = get_code_files()
    links = list()
    errors = list()

    for file_path in file_paths:
        index = file_paths.index(file_path)
        link, success = get_problem_link(file_path, index)
        if success == True:
            links.append(link)
        else:
            errors.append(file_path)
    if len(errors) == len(file_paths):
        raise Exception("Fetching the links failed for all problems")
    return links, errors


def write_link_to_file(link, file_path):
    """
    Write link to file
    """
    file_lines = list()
    line_no = 2 # line of file to write link to (default 2)
    try:
        with open(file_path, 'w') as f:
            for line in f:
                file_lines.append(line)
            link = '#' + link
            file_lines.insert(line_no - 1, link) # insert link into second line
            for line in file_lines:
                f.write(line + "\n")
    except IOError:
        raise IOError(
            "IOError occured while writing gathered URL from website to file")


def get_problem_link(file_path, index):
    """
    Gets the problem link from a HackerRank code file
    :returns: link, success (link is None and success is false if link cannot be found)
    """
    lines = []
    file_lines = list()
    if file_lines(file_path) > 1 and open_replace_newlines() != None:
        lines = open_replace_newlines(file_path)
        first_line = lines[0]
        if first_line == '#!/bin/python3':
            if not lines[1].startswith('#https://www.hackerrank.com/'):
                link, success = get_problem_link_URL(index)
                if success is True:
                    write_link_to_file(link, file_path)
                return link, success
        else:  # first line is not a shebang
            import_module(FILEUTIL_PATH)
            import fileUtil
            fileUtil.write_shebang(file_path, 3)
            if lines[1].startswith('#https://www.hackerrank.com/'): # second line is a shebang
                link = lines[1]
                link = link[1:]  # remove comment sign ('#') from link
                success = True
                return link, success
            else:  # second line of file contains no link
                link, success = get_problem_link_URL(file_path)
                if success is True:
                    write_link_to_file(link, file_path)
                return link, success
    else:  # file has only one line
        link = None
        success = False
        return link, success


def open_replace_newlines(file_path):
    """
    Opens a file and returns list of lines
    :returns: list of lines or None if error occured
    """
    lines = list()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                lines.append(line)
        for line in lines:
            lines[lines.index(line)] = line.replace('\n', '')
    except IOError:
        return None
    return lines
