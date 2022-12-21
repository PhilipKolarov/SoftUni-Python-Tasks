file_path = './my_first_file'

with open(file_path, 'w') as file_in:
    text = 'I just created my first file'
    file_in.write(text)