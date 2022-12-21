from os import remove
from os.path import exists

file_path = './my_first_file'
if exists(file_path):
    remove(file_path)
    print('File deleted')
else:
    print('File already deleted')