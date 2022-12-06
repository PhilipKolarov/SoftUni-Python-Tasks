first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])
n = int(input())

for i in range(n):
    command_data = input().split()
    command = command_data[0]
    target_set = command_data[1]

    if command == "Add":
        if target_set == "First":
            first_seq = first_seq.union([int(x) for x in command_data[2:]])
        else:
            second_seq = second_seq.union([int(x) for x in command_data[2:]])
    elif command == "Remove":
        if target_set == "First":
            first_seq = first_seq.difference([int(x) for x in command_data[2:]])
        else:
            second_seq = second_seq.difference([int(x) for x in command_data[2:]])
    else:
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')
