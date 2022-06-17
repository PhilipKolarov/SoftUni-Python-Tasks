def bunny_spread(lair, row, col):
    surrounding_positions = [
        [row-1, col],
        [row, col-1],
        [row, col+1],
        [row+1, col]
    ]

    result = []
    for r, c in surrounding_positions:
        if 0 <= r < len(lair) and 0 <= c < len(lair[row]) and lair[r][c] != 'B':
            result.append([r, c])
    return result


n, m = [int(x) for x in input().split(' ')]
lair = []

for _ in range(n):
    lair.append([x for x in input()])

p_c = None
b_c = []

for r in range(n):
    for c in range(m):
        if lair[r][c] == 'P':
            p_c = [r, c]
        elif lair[r][c] == 'B':
            b_c.append([r, c])

moves = input()
escaped = False
dead = False
last_postions = []

for ch in moves:
    if escaped == True or dead == True:
        break
    last_positions = [p_c[0], p_c[1]]
    lair[p_c[0]][p_c[1]] = '.'
    if ch == 'U':
        p_c[0] -= 1
    elif ch == 'D':
        p_c[0] += 1
    elif ch == 'L':
        p_c[1] -= 1
    elif ch == 'R':
        p_c[1] += 1

    if p_c[0] < 0 or p_c[0] >= n or p_c[1] < 0 or p_c[1] >= m:
        escaped = True
    elif lair[p_c[0]][p_c[1]] == 'B':
        dead = True
    else:
        lair[p_c[0]][p_c[1]] == 'P'

    new_b_c = []
    for coordinates in b_c:
        mutations = bunny_spread(lair, coordinates[0], coordinates[1])
        for r, c in mutations:
            lair[r][c] = 'B'
            new_b_c.append([r, c])
            if p_c[0] == r and p_c[1] == c:
                dead = True

    for coordinates in new_b_c:
        b_c.append([coordinates[0], coordinates[1]])

for r in lair:
    print(''.join(r))
if dead:
    print(f"dead: {p_c[0]} {p_c[1]}")
if escaped:
    print(f"won: {last_positions[0]} {last_positions[1]}")
