import os
import time
import subprocess

process = subprocess.Popen("git pull", stdout=subprocess.PIPE)
output = process.communicate()[0]
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace('\\', '/')

print(path)
p = subprocess.check_output(['git ls-files -z | xargs -0 -n1 -I{} -- git log -1 --format="%ai {}" {} | sort'],cwd = "C:/Users/janko/Documents/GitHub/exercises",shell=True) 
print(p)

date_file_list = []
file_extensions = ['.java', '.py']
with os.scandir(path) as it:
    for entry in it:
        for ext in file_extensions:
            if entry.name.endswith(ext) and entry.is_file():
                stats = os.stat(entry)

                lastmod_date = time.localtime(stats[8])

                date_file_tuple = lastmod_date, entry
                date_file_list.append(date_file_tuple)

print(date_file_list)  # test