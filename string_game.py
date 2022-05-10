input_string = input()
command = input()

while command != 'Done':
    if command == 'Uppercase':
        input_string = input_string.upper()
        print(input_string)
    else:
        data = command.split(' ')
        action = data[0]
        if action == 'Change':
            char = data[1]
            replacement = data[2]
            input_string = input_string.replace(char, replacement)
            print(input_string)
        elif action == 'Includes':
            substring = data[1]
            if input_string.find(substring) == -1:
                print('False')
            else:
                print('True')
        elif action == 'End':
            substring = data[1]
            length = int(len(substring))
            starting_index = int(0 - length)
            if input_string[starting_index:] == substring:
                print('True')
            else:
                print('False')
        elif action == 'FindIndex':
            char = data[1]
            for ch in input_string:
                if ch == char:
                    index = input_string.index(ch)
                    print(index)
                    break
        elif action == 'Cut':
            starting_index = int(data[1])
            count = int(data[2])
            end_index = starting_index + count
            input_string = input_string[starting_index:end_index]
            print(input_string)

    command = input()
