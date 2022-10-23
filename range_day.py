def is_inside(r, c):
    return 0 <= r < 5 and 0 <= c < 5

def move(my_position, direction, spaces):
    if direction == 'up':
        return my_position[0] - spaces, my_position[1]
    if direction == 'down':
        return my_position[0] + spaces, my_position[1]
    if direction == 'left':
        return my_position[0], my_position[1] - spaces
    if direction == 'right':
        return my_position[0], my_position[1] + spaces


matrix = []
my_position = None
total_targets = 0
hit_targets = 0
hits_list = []

for r in range(5):
    current_row = input().split(' ')
    for c in range(5):
        if current_row[c] == 'A':
            my_position = [r, c]
        elif current_row[c] == 'x':
            total_targets += 1
    matrix.append(current_row)

n = int(input())
for i in range(n):
    command = input().split(' ')
    direction = command[1]
    if command[0] == 'move':
        spaces = int(command[2])
        new_row, new_col = move(my_position, direction, spaces)
        if is_inside(new_row, new_col) and matrix[new_row][new_col] == '.':
            matrix[my_position[0]][my_position[1]] = '.'
            matrix[new_row][new_col] = 'A'
            my_position = [new_row, new_col]
    elif command[0] == 'shoot':
        bullet_row, bullet_col = move(my_position, direction, 1)
        while is_inside(bullet_row, bullet_col):
            bullet_position = [bullet_row, bullet_col]
            if matrix[bullet_row][bullet_col] == 'x':
                matrix[bullet_row][bullet_col] = '.'
                hit_targets += 1
                hits_list.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = move(bullet_position, direction, 1)
        if hit_targets == total_targets:
            break

if hit_targets == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - hit_targets} targets left.")

for el in hits_list:
        print(el)
