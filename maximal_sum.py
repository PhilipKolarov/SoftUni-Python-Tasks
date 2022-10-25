m = []
rows, columns = [int(x) for x in input().split(' ')]

for _ in range(rows):
    m.append([int(x) for x in input().split()])

total_identical_squares = 0
max_sum = float('-inf')
start_row = 0
start_col = 0

for r in range(rows-2):
    for c in range(columns-2):
        current_sum = m[r][c] + m[r][c+1] + m[r][c+2] + m[r+1][c] + m[r+1][c+1] + \
                      m[r+1][c+2] + m[r+2][c] + m[r+2][c+1] + m[r+2][c+2]
        if current_sum > max_sum:
            max_sum = current_sum
            start_row = r
            start_col = c

print(f"Sum = {max_sum}")
print(f"{m[start_row][start_col]} {m[start_row][start_col+1]} {m[start_row][start_col+2]}")
print(f"{m[start_row+1][start_col]} {m[start_row+1][start_col+1]} {m[start_row+1][start_col+2]}")
print(f"{m[start_row+2][start_col]} {m[start_row+2][start_col+1]} {m[start_row+2][start_col+2]}")
