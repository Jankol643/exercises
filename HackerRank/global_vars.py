import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = FOLDER + os.path.sep + 'problems' + os.path.sep
DATAPATH = FOLDER + os.path.sep + 'items.csv'
FILE_LIST = FOLDER + os.path.sep + 'file_list.txt'
SHEBANG = '#!/usr/bin/env python3'
# what date should be set as solved date
DATE = 'first commit'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DIFFICULTY_PROMPT = '# Difficulty: '
FILE_LINK_BEGINNING = '#https://www.hackerrank.com/'

GET_WRITE_PROBLEM_LINK_TIMES = list()
GET_DOMAINS_TIMES = list()
GET_DIFFICULTY_TIMES = list()
GET_SOLVED_DATE_TIMES = list()
GET_INSTRUCTIONS_TIMES = list()