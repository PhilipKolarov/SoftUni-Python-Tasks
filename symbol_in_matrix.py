n = int(input())
matrix = []

for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

# matrix = [list(input()) for _ in range(n)]

wanted_ch = input()
found_position = []
found = False

for row in range(n):
    for column in range(n):
        if matrix[row][column] == wanted_ch:
            found = True
            found_position.append(row)
            found_position.append(column)
            break

if found:
    print(f"({found_position[0]}, {found_position[1]})")
else:
    print(f"{wanted_ch} does not occur in the matrix")
