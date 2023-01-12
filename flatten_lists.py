input_lists = input().split('|')
output = []

for i in range(len(input_lists) - 1, -1, -1):
    current_elements = input_lists[i].strip().split()
    output.extend(current_elements)

print(' '.join(output))
