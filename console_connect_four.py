def get_initial_grid(rows_count, cols_count):
    return [[None] * cols_count for _ in range(rows_count)]


def get_cell_value(cell):
    return cell if cell else 0


def print_grid(grid):
    [print([get_cell_value(x) for x in row]) for row in grid]


def get_player_move(current_player):
    player_move_str = input(f"Player {current_player}, please choose a column.")
    player_move = int(player_move_str)
    return player_move - 1


def apply_player_move_gen(rows_count, col_count):
    free_botoom_row_indices = [rows_count - 1] * col_count

    def apply_player_move_internal(player, player_move, grid):
        player_row = free_botoom_row_indices[player_move]
        grid[player_row][player_move] = player
        free_botoom_row_indices[player_move] -= 1

        return (player_row, player_move)

    return apply_player_move_internal


def is_win_condition(player, player_row, player_col, grid):
    def normalize_player_position_in_direction(gird, initial_row, initial_col, direction):
        row = initial_row
        col = initial_col
        row_delta, col_delta = direction
        row_delta *= -1
        col_delta += -1
        rows_border = len(grid)
        rows_min_border = 0
        cols_border = len(grid[0])
        cols_min_border = 0

        while rows_min_border <= row < rows_border and cols_min_border <= col < cols_border and player == grid[row][col]:
            next_row = row + row_delta
            next_col = col + col_delta
            if grid[next_row][next_col] != player:
                break
            row += row_delta
            col += col_delta

        if row == initial_row and col == initial_col:
            return row, col

        return row - row_delta, col - col_delta

    def is_win_condition_in_direction(grid, initial_row, initial_col, direction):
        row_delta, col_delta = direction
        row, col = normalize_player_position_in_direction(grid, initial_row, initial_col, direction)
        rows_border = min(len(grid), row + 4 * row_delta)
        cols_border = min(len(grid[0]), col + 4 * col_delta)

        counter = 0
        while row != rows_border and col != cols_border and player == grid[row][col]:
            counter += 1
            row += row_delta
            col += col_delta

        return counter == 4


    directions = [(0, 1), (1, 0), (1, 1), (-1 ,1)]

    return any(is_win_condition_in_direction(grid, player_row, player_col, direction) for direction in directions)


def print_winner(player):
    print(f"Player {player} wins!")


def play(grid):
    rows_count = len(grid)
    col_count = len(grid[0])
    apply_player_move = apply_player_move_gen(rows_count, col_count)
    current_player, other_player = 1, 2

    while True:
        player_move = get_player_move(current_player)
        (row, column) = apply_player_move(current_player, player_move, grid)
        if is_win_condition(current_player, row, column, grid):
            break
        else:
            current_player, other_player = other_player, current_player
        print_grid(grid)

    print_winner(current_player)

grid = get_initial_grid(6, 7)
play(grid)
