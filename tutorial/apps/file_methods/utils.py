import os
import json


def open_file_with_mode(file, mode: str = 'r'):
    if mode == 'r':  # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
        f = open(file, mode)
        return f.read()
        # return f.read(5)  Return the 5 first characters of the file:

    elif mode == 'a':  # "a" - Append - Opens a file for appending, creates the file if it does not exist
        f = open(file, mode)
        f.write("Now the file has more content!")
        return f.read()
    elif mode == 'w':  # "w" - Write - Opens a file for writing, creates the file if it does not exist
        f = open(file, mode)
        f.write("Woops! I have deleted the content!")
        return f
    elif mode == 'x':  # "x" - Create - Creates the specified file, returns an error if the file exist
        pass
    elif mode == 't':  # "t" - Text - Default value. Text mode
        pass
    elif mode == 'b':  # "b" - Binary - Binary mode (e.g. images)
        pass
    else:
        raise ValueError("Unexpected mode")


def deleting_file(file: str = ''):
    if os.path.exists(file):
        os.remove(file)
        print("File deletion completed successfully")
    else:
        print("The file does not exist")


def deleting_folder(folder: str = ''):
    if os.path.exists(folder):
        os.rmdir(folder)
        print("Folder deletion completed successfully")
    else:
        print("The Folder does not exist")


def write_json(file: str = '', payload: dict = ()):
    # with open(file + '.json', '+a') as outfile:
    #  +a -> - Append - Opens a file for appending, creates the file if it does not exist
    with open(file + '.json', 'w') as outfile:
        json.dump(payload, outfile)
