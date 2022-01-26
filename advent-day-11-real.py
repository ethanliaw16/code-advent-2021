import sys

def out_of_bounds(pair, board):
    return pair[0] < 0 or pair[0] > 9 or pair[1] < 0 or pair[1] > 9 or board[pair[0]][pair[1]] > 9

def get_adjacent(row, column, board):
    adjacent = []
    top = [row - 1, column, (row - 1) * 100 + column]
    left = [row, column - 1, (row * 100) + column - 1]
    bottom = [row + 1, column, (row + 1) * 100 + column]
    right = [row, column + 1, (row * 100) + column + 1]
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

def get_flashes(board):
    flashes = []
    for i in range(10):
        for j in range(10):
            if board[i][j] > 9:
                flashes.append([i,j])
    return flashes
num_flashes = 0
board = []
for line in sys.stdin:
    if line[:-1] == '':
        break
    row = line[:-1]
    row_nums = []
    for i in range(len(row)):
        row_nums.append(int(row[i]))
    board.append(row_nums)
print(f"Original board: {board}")
for i in range(100):
    increment(board)
    print(f"num flashes: {num_flashes}")
    while flashing(board):
        #print("flash!")
        flashes = get_flashes(board)
        num_flashes += len(flashes)
        for flash in flashes:
            adjacent = get_adjacent(flash[0],flash[1], board)
            for point in adjacent:
                board[point[0]][point[1]] += 1
            board[flash[0]][flash[1]] = 0
print(f"final total flashes: {num_flashes}")