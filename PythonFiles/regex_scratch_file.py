import os
import re

path = r"C:/Users/Colin Janowicz/Documents/GitHub/ParseLoadTimesPython/Bitbar Using Filter Logs/3fd75eb26459706c-logs/"
os.chdir(path)
target_string = "<color=#FB7345>[LA-STOPWATCH]"

def read_files(file_path):
    with open(file_path, 'r') as file:
        # print(file.read())
        print(file.name)
        # <color=#FB7345>[LA-STOPWATCH]</color> Ended:
        for line in file:
            if target_string in line:
                print(line)
                print(f"Found {target_string}")



def iterate_over_files():
    print("File name:")
    for file in os.listdir():
        if file.endswith('.log'):
            file_path = f"{path}/{file}"
            read_files(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    iterate_over_files()