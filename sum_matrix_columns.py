rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

column_sums = [0] * columns
for row_index in range(rows):
    for column_index in range(columns):
        column_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sums]
