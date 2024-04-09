import os
from datetime import datetime
import argparse


def write_user_date(file_name: str):
    try:
        create_time = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n"
        user_input_data = [create_time]
        line_counter = 1
        while 1:
            user_input = input("Enter some message: ")
            if user_input == "stop":
                break
            user_input_data.append(f"{line_counter} {user_input}\n")
            line_counter += 1

        with open(file_name, 'a') as file:
            file.writelines(user_input_data)
    except IOError:
        print("We got an error while during writing process")


def create_file(dir_path, file_path):
    try:
        if dir_path:
            path_to_dir = os.path.join(*dir_path)
            print("file directory: ", path_to_dir)
            os.makedirs(path_to_dir, exist_ok=True)
        if file_path:
            if dir_path:
                path_to_file = os.path.join(*dir_path, file_path)
                write_user_date(path_to_file)
            else:
                write_user_date(file_path)
    except (IOError, argparse.ArgumentTypeError):
        print("Oops, we got an error during the creating file process")


parser = argparse.ArgumentParser(description="Parser for args")
parser.add_argument("-f", dest="file_path")
parser.add_argument("-d", nargs="+", dest="dir_path")

try:
    args = parser.parse_args()
except (IOError, argparse.ArgumentTypeError):
    print("Cant parse provided arguments")
else:
    create_file(args.dir_path, args.file_path)