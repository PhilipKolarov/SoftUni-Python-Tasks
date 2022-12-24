rows, columns = [int(x) for x in input().split(' ')]
snake_string = input()
index = 0

matrix = []
for r in range(rows):
    matrix.append([])
    for c in range(columns):
        matrix[r].append(None)

for row in range(rows):
    if row % 2 == 0:
        for column in range(columns):
            matrix[row][column] = snake_string[index % len(snake_string)]
            index += 1
    else:
        for column in range(columns - 1, -1, -1):
            matrix[row][column] = snake_string[(index % len(snake_string))]
            index += 1

for row in matrix:
    print(''.join(row))
