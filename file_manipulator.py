from os.path import exists
from os import remove

while True:
    line = input()
    if line == 'End':
        break

    command = line.split('-')
    action, file_name = command[0], command[1]

    if action == "Create":
        with open(f'./{file_name}', 'w') as file:
            pass
    elif action == "Add":
        content = command[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '\n')
    elif action == "Replace":
        if not exists(f'./{file_name}'):
            print('An error occured')
            continue
        old_string, new_string = command[2], command[3]
        with open(f'./{file_name}', 'r+') as file:
            file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(file_content)
    elif action == "Delete":
        if not exists(f'./{file_name}'):
            print('An error occured')
            continue
        remove(f'./{file_name}')
