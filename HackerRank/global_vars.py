import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = FOLDER + os.path.sep + 'problems' + os.path.sep
DATAPATH = FOLDER + os.path.sep + 'items.csv'
FILE_LIST = FOLDER + os.path.sep + 'file_list.txt'
# what date should be set as solved date
DATE = 'first commit'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DIFFICULTY_PROMPT = '# Difficulty: '

GET_WRITE_PROBLEM_LINK_TIMES = [2, 3, 7, 8]
GET_DOMAINS_TIMES = [2, 3, 7, 8]
GET_DIFFICULTY_TIMES = [2, 3, 7, 8]
GET_SOLVED_DATE_TIMES = [2, 3, 7, 8]
GET_INSTRUCTIONS_TIMES = [2, 3, 7, 8]