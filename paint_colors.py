from collections import deque

strings = deque(input().split())
primary_colors = {'red', 'blue', 'yellow'}
secondary_colors = {'orange', 'green', 'purple'}
formed_colors = []

while strings:
    left = strings.popleft()
    right = strings.pop() if strings else ""

    result = left + right
    if result in primary_colors or result in secondary_colors:
        formed_colors.append(result)
        continue
    result = right + left
    if result in primary_colors or result in secondary_colors:
        formed_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        strings.insert(len(strings) // 2, left)
    if right:
        strings.insert(len(strings) // 2, right)

result = []

combo_dict = {
    'orange': ['yellow', 'red'],
    'purple': ['red', 'blue'],
    'green': ['blue', 'yellow']
}

for color in formed_colors:
    if color in primary_colors:
        result.append(color)
        continue
    collected = True
    for main_color in combo_dict[color]:
        if main_color not in formed_colors:
            collected = False
            break

    if collected:
        result.append(color)

print(result)