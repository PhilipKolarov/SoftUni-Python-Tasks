rows, columns = [int(x) for x in input().split()]

matrix = []
for r in range(rows):
    matrix.append([])
    for c in range(columns):
        first = 97 + r
        middle = 97 + r + c
        matrix[r].append(f'{chr(first)}{chr(middle)}{chr(first)}')

for list in matrix:
    print(' '.join(list))
