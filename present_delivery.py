def get_next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size

def get_kids_nearby(r, c, matrix):
    result = []
    if is_inside(r, c-1, len(matrix)) and matrix[r][c-1] == 'V' or matrix[r][c-1] == 'X':
        result.append([r, c-1])
    if is_inside(r, c+1, len(matrix)) and matrix[r][c+1] == 'V' or matrix[r][c+1] == 'X':
        result.append([r, c+1])
    if is_inside(r-1, c, len(matrix)) and matrix[r-1][c] == 'V' or matrix[r-1][c] == 'X':
        result.append([r-1, c])
    if is_inside(r+1, c, len(matrix)) and matrix[r+1][c] == 'V' or matrix[r+1][c] == 'X':
        result.append([r+1, c])

    return result


presents = int(input())
n = int(input())

santa_row = 0
santa_col = 0
nice_kids = 0

matrix = []

for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == 'S':
            santa_row = row
            santa_col = col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)

nice_kids_with_presents = 0

while True:
    command = input()
    if command == 'Christmas morning':
        break

    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_position(santa_row, santa_col, command)

    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        nice_kids_with_presents += 1
    elif matrix[santa_row][santa_col] == 'C':
        kids_nearby = get_kids_nearby(santa_row, santa_col, matrix)
        for kid_row, kid_col in kids_nearby:
            if matrix[kid_row][kid_col] == 'V':
                nice_kids_with_presents += 1
            presents -= 1
            matrix[kid_row][kid_col] = '-'
            if presents == 0:
                break
    matrix[santa_row][santa_col] = 'S'
    if presents == 0:
        break

if nice_kids != nice_kids_with_presents and presents == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))

if nice_kids == nice_kids_with_presents:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_with_presents} nice kid/s.")
