"""Converts a csv to different formats."""

import os
import sqlalchemy
import pandas as pd
import csv

folder_name = 'converted'
csv_filename = 'items.csv'
html_filename = 'problem_list.html'
db_filename = 'problems.db'
db_tablename = 'problems'

dirname = os.getcwd() + os.path.sep + 'HackerRank'
os.chdir(dirname)
folder_path = dirname + os.path.sep + folder_name
# creates the directory if it does not exist
os.makedirs(folder_path, exist_ok=True)
db_path = folder_path + os.path.sep + db_filename
print(db_path)

df = pd.read_csv(csv_filename, delimiter=',')
key_list = df.keys().tolist()
# creating html file
html_file = open(html_filename, 'w')
html_file.close()

df.to_html(html_filename, index=False)


def to_sqlite_db(df, db_tablename, key_list):
    db_name = db_tablename
    engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user="root",
                                pw="your_password",
                                db=db_name))
    df.to_sql(con=engine, name='table_name', if_exists='replace')

    sql_set_primary = 'ALTER TABLE ' + db_tablename + \
        ' ADD PRIMARY KEY (' + key_list[0] + ');'
    mycursor.execute(sql_set_primary)

    mycursor.close()

to_sqlite_db(df, db_tablename, key_list)
