import os
import csv
path = r"C:/Users/Colin Janowicz/Documents/GitHub/ParseLoadTimesPython/Bitbar Using Filter Logs/3fd75eb26459706c-logs/"
os.chdir(path)
target_string = "<color=#FB7345>[LA-STOPWATCH]"

for file in os.listdir():
    if file.endswith('.log'):
        with open(f'{file.}.csv', 'w', newline='') as csvfile:
            # Ok. Function: Seconds:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
        file_path = f"{path}/{file}"
        with open(file_path, 'r') as file:
            # print(file.read())
            # print(file.name)
            for line in file:
                if target_string in line:
                    # print(line)


