import os
import csv

import re

regex = re.compile('([a-zA-Z]*\.[a-zA-Z]*\.[a-zA-Z]*) on (\d*\.\d*)')

path = r"/Users/walter/ParseLoadTimesPython/Bitbar Using Filter Logs/3fd75eb26459706c-logs/"
os.chdir(path)

files = os.listdir()

all_logs = [['filename', 'function', 'seconds']]

for file_name in files:
    if file_name.endswith('.log'):

        contents = None

        with open(file_name) as file:
            contents = file.read()

        file_contents = contents.split('\n')

        for line in file_contents:
            if 'second(s)' in line:
                # print(line)
                find = regex.findall(line)
                if len(find) > 0:

                    log = [file_name] + list(find[0])
                    print(log)
                    all_logs.append(log)

with open('output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(all_logs)