stack = []

queries_count = int(input())

for _ in range (queries_count):
    query_data = [int(x) for x in input().split()]
    command = query_data[0]
    if command == 1:
        number = query_data[1]
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))