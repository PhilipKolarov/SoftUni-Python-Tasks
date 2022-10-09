n = int(input())
grid = []

bunny_row = 0
bunny_col = 0

for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == 'B':
            bunny_row = row
            bunny_col = col
    grid.append(row_elements)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

best_sum = 0
best_direction = ''
best_path = []

for direction in directions:
    current_sum = 0
    current_path = []
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < n and 0 <= col < n and grid[row][col] != 'X':
        current_sum += int(grid[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum >= best_sum and current_path:
        best_sum = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
for el in best_path:
    print(el)
print(best_sum)
