import sys

def out_of_bounds(pair, board):
    return pair[0] < 0 or pair[0] > 9 or pair[1] < 0 or pair[1] > 9 or board[pair[0]][pair[1]] > 9

def get_adjacent(row, column, board):
    adjacent = []
    top = [row - 1, column, (row - 1) * 10 + column]
    left = [row, column - 1, (row * 10) + column - 1]
    bottom = [row + 1, column, (row + 1) * 10 + column]
    right = [row, column + 1, (row * 10) + column + 1]
    top_left = [row - 1, column - 1]
    top_right = [row - 1, column + 1]
    bottom_left = [row + 1, column - 1]
    bottom_right = [row + 1, column + 1]
    if not out_of_bounds(top, board):
        adjacent.append(top)
    if not out_of_bounds(right, board):
        adjacent.append(right)
    if not out_of_bounds(left, board):
        adjacent.append(left)
    if not out_of_bounds(bottom, board):
        adjacent.append(bottom)
    if not out_of_bounds(top_left, board):
        adjacent.append(top_left)
    if not out_of_bounds(top_right, board):
        adjacent.append(top_right)
    if not out_of_bounds(bottom_left, board):
        adjacent.append(bottom_left)
    if not out_of_bounds(bottom_right, board):
        adjacent.append(bottom_right)
    return adjacent

def increment(board):
    for row in board:
        for index in range(10):
            row[index] += 1

def flashing(board):
    for row in board:
        if max(row) > 9:
            return True
    return False

def get_flashes(board, flashed):
    flashes = []
    for i in range(10):
        for j in range(10):
            if board[i][j] > 9 and flashed[i][j] == 0:
                flashes.append([i,j])
    return flashes

def get_new_flashes(board, flashed):
    flashes = []
    for i in range(10):
        for j in range(10):
            if board[i][j] > 9 and flashed[i][j] == 0:
                flashes.append([i,j])
    return flashes

def set_flashes_to_0(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] > 9:
                board[i][j] = 0

clear_board = []
for i in range(10):
    clear_board.append([0] * 10)

num_flashes = 0
board = []
for line in sys.stdin:
    if line[:-1] == '':
        break
    row = line[:-1]
    row_nums = []
    for i in row:
        row_nums.append(int(i))
    board.append(row_nums)

simultaneous_flashes = []
print(f"Original board:")
for row in board:
    print(row)
print("\n")
current_step = 0
for i in range(215):
    current_step += 1
    increment(board)
    if current_step > 200:
        print(f"step {current_step}: num flashes: {num_flashes}")
    flashed = []
    for j in range(10):
        flashed.append([0] * 10)
    flashes = get_new_flashes(board, flashed)
    flashes_this_turn = 0
    while(len(flashes) > 0):
        num_flashes += len(flashes)
        flashes_this_turn += len(flashes)
        if flashes_this_turn >= 100:
            print(f"Everyone flashed! this is step {current_step}")
            simultaneous_flashes.append([current_step, flashes_this_turn])
        for flash in flashes:
            flashed[flash[0]][flash[1]] += 1
            adjacent = get_adjacent(flash[0],flash[1], board)
            for point in adjacent:
                board[point[0]][point[1]] += 1
        flashes = get_new_flashes(board, flashed)
    set_flashes_to_0(board)
    #
    #while flashing(board):
    #    #print("flash!")
    #    flashes = get_flashes(board, flashed)
    #    print(f"Flashes at {flashes}")
    #    #print(f"Current board before flashing:")
    #    
    #    num_flashes += len(flashes)
    #    for flash in flashes:
    #        flashed[flash[0]][flash[1]] += 1
    #        adjacent = get_adjacent(flash[0],flash[1], board)
    #        for point in adjacent:
    #            board[point[0]][point[1]] += 1
    #        board[flash[0]][flash[1]] = 0
    if i > 200:
        print(f"board after {i + 1} step(s) of incrementing")
        for row in board:
            print(row)
print(f"final total flashes: {num_flashes}")
print(f"Steps with simultaneous flash: {simultaneous_flashes}")