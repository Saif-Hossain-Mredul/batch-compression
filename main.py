import os
from pathlib import Path

files_directory = input("Enter directory path: ")

new_directory_path = os.path.join(files_directory, "Compressed")
try:
    os.mkdir(new_directory_path)
except FileExistsError:
    print("Directory already exists, copying file in the existing directory")

files_list = os.listdir(files_directory)

for file_name in files_list:
    try:
        is_directory = os.path.isdir(files_directory + "/" + file_name)
        base_file_name = Path(file_name).stem

        input_file = os.path.join(files_directory, file_name)
        output_file = os.path.join(new_directory_path, base_file_name + ".mp4")
        command = 'ffmpeg -i ' + '"' + input_file + '"' + ' -vcodec libx265 -crf 28 ' + '"' + output_file + '"'

        print(command)

        if not is_directory:
            os.system(command)
    except FileNotFoundError:
        print('Error occurred')
