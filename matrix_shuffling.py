rows, columns = [int(x) for x in input().split()]
matrix = []

for r in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == "END":
        break

    data = command.split(' ')

    if data[0] != 'swap':
        print("Invalid input!")
        continue

    if len(data) != 5:
        print("Invalid input!")
        continue

    ir1 = int(data[1])
    ic1 = int(data[2])
    ir2 = int(data[3])
    ic2 = int(data[4])

    if ir1 >= rows or ir2 >= rows or ic1 >= columns or ic2 >= columns:
        print("Invalid input!")
        continue

    matrix[ir1][ic1], matrix[ir2][ic2] = matrix[ir2][ic2], matrix[ir1][ic1]

    for row in matrix:
        print(' '.join(row))
