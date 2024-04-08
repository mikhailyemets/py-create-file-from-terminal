import sys
import os
from datetime import datetime


def input_data(file_path: str) -> None:
    line_number = 0
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{time} \n")
    while 1:
        line_number += 1
        text_line = input("Enter content line: ")
        if text_line.lower() == "stop":
            break
        with open(file_path, "a") as file:
            file.write(f"{line_number} {text_line} \n")


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        d_index = sys.argv.index("-d")
        dir_path = os.path.join(*sys.argv[d_index + 1:])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "file.txt")
        input_data(file_path)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        f_index = sys.argv.index("-f")
        file_path = sys.argv[f_index + 1]
        utc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "w") as file_time:
            file_time.write(utc_time + "\n")
        input_data(file_path)
    elif "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        dir_path = os.path.join(*sys.argv[d_index + 1:f_index])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, sys.argv[f_index + 1])
        input_data(file_path)
