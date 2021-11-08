import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = FOLDER + os.path.sep + 'problems' + os.path.sep
DATAPATH = FOLDER + os.path.sep + 'items.csv'
FILE_LIST = FOLDER + os.path.sep + 'file_list.txt'
# what date should be set as solved date
DATE = 'first commit'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DIFFICULTY_PROMPT = '# Difficulty: '

PROCESS_PROBLEM_TIME = 0
GET_CODE_FILES_TIMES = 0
GET_WRITE_PROBLEM_LINK_TIMES = list()
GET_DOMAINS_TIMES = list()
GET_DIFFICULTY_TIMES = list()
GET_SOLVED_DATE_TIMES = list()
GET_INSTRUCTIONS_TIMES = list()
WRITE_TO_CSV_TIME = 0