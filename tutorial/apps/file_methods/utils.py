import os
import json
from datetime import datetime, timedelta


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


# WRITE AND UPDATE JSON FILE
def write_json():
    # with open(file + '.json', '+a') as outfile:
    #  +a -> - Append - Opens a file for appending, creates the file if it does not exist
    count_json = 'apps/file_methods/count.json'
    with open(count_json, 'r') as f:
        data = json.loads(f.read())
        counter = data['count_token']
    file_json = 'apps/file_methods/count'
    with open(file_json + '.json', 'w') as o:
        count = {"count_token": counter + 1}
        json.dump(count, o)

    file_json = 'apps/file_methods/auth_data'
    start_time = datetime.now().time().strftime('%H:%M:%S')
    end_date = datetime.now() + timedelta(seconds=55) - timedelta(seconds=5)
    expires_in = timedelta(seconds=55) - timedelta(seconds=5)
    payload = {
        "access_token": "Some-TOKEN-@@@333444",
        "start_time": str(start_time),
        "end_time": str(end_date.strftime('%H:%M:%S')),
        "expires_in": str(expires_in),
        "token_type": "Application Access Token"
    }
    with open(file_json + '.json', 'w') as outfile:
        json.dump(payload, outfile)


def calculate_time():
    file_json = 'apps/file_methods/auth_data.json'
    with open(file_json, 'r') as f:
        data = json.loads(f.read())
        end_time = datetime.strptime(data['end_time'], '%H:%M:%S')
        # difference = (t_4 - t_3)
        # difference_time = difference.seconds + difference.seconds // 3600
        current_time = datetime.strptime(datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
        # print("current_time...", current_time.time(), type(current_time.time()))
        # print("end_time...", end_time.time(), type(end_time.time()))
        if current_time.time() > end_time.time():
            # print("Need to be updated .......")
            write_json()
            return True
        else:
            # print("No need to update......")
            return False
