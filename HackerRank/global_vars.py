import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
FOLDER = FOLDER.replace("\\", '/')
PROBLEMS = FOLDER + '/problems/'
DATAPATH = FOLDER + '/' + 'items.csv'
FILE_LIST = FOLDER + '/' + 'file_list.txt'
# if creation or last modification ('last modified') date should be set as solved date
DATE = 'creation'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'