import os
import csv
import pandas as pd

import re

# regex = re.compile('([a-zA-Z]*\.[a-zA-Z]*\.[a-zA-Z]*) on (\d*\.\d*)')
regex = re.compile('([a-zA-Z]*\.[a-zA-Z]*\.[a-zA-Z]*phase) on (\d*\.\d*)', re.IGNORECASE)

# path = r"C:\Users\Colin Janowicz\Documents\GitHub\ParseLoadTimesPython\Bitbar Using Filter Logs\3fd75eb26459706c-logs/"
path = r"C:\Users\Colin Janowicz\Documents\ipad mini 5/"
os.chdir(path)

files = os.listdir()

exclusion_list = ['Lagertha.Gameplay.AcceptLegalLoadPhase']

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

                    if not any([x in log[1] for x in exclusion_list]):
                        all_logs.append(log)

with open('output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(all_logs)

df = pd.read_csv('output.csv')

report_seconds = df.groupby(['filename']).sum()

report_seconds.to_csv('total_seconds_per_log.csv')