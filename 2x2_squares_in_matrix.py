matrix = []
rows, columns = [int(x) for x in input().split(' ')]

for _ in range(rows):
    matrix.append([x for x in input().split()])

total_identical_squares = 0

for r in range(rows-1):
    for c in range(columns-1):
        if matrix[r][c] == matrix[r+1][c] == matrix[r][c+1] == matrix[r+1][c+1]:
            total_identical_squares += 1

print(total_identical_squares)