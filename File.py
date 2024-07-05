import os

def list_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

directory_path = '/home/blop/Downloads/'
file_list = list_files_in_directory(directory_path)
print(file_list)