def get_positions(matrix, row, column):
    surrounding_positions = [
        [row - 1, column - 1],
        [row - 1, column],
        [row - 1, column + 1],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column - 1],
        [row + 1, column],
        [row + 1, column + 1]
    ]

    result = []
    for r, c in surrounding_positions:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] > 0:
            result.append([r, c])
    return result


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

positions = input().split(' ')
positions_matrix = []

for x in positions:
    positions_matrix.append([int(i) for i in x.split(',')])

for bomb in positions_matrix:
    row, column = bomb[0], bomb[1]
    power = matrix[row][column]

    if power <= 0:
        continue

    matrix[row][column] = 0
    damages = get_positions(matrix, row, column)
    for r, c in damages:
        matrix[r][c] -= power

alive_cells_qty = 0
alive_cells_sum = 0

for r in matrix:
    for c in r:
        if c > 0:
            alive_cells_qty += 1
            alive_cells_sum += c

print(f"Alive cells: {alive_cells_qty}")
print(f"Sum: {alive_cells_sum}")
for r in matrix:
    printable_row = [str(x) for x in r]
    print(' '.join(printable_row))
