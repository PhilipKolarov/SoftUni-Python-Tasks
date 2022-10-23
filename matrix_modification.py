n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break
    else:
        data = command.split()
        row = int(data[1])
        col = int(data[2])
        value = int(data[3])
        if row >= len(matrix) or col >= len(matrix) or row < 0 or col < 0:
            print('Invalid coordinates')
        elif data[0] == 'Add':
            matrix[row][col] += value
        elif data[0] == 'Subtract':
            matrix[row][col] -= value

for row in matrix:
    row = [str(x) for x in row]
    print(' '.join(row))
