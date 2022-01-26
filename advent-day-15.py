import sys

def out_of_bounds(pair, num_rows, num_cols):
    return pair[0] < 0 or pair[0] > (num_rows - 1) or pair[1] < 0 or pair[1] > (num_cols - 1)

def get_adjacent(row, column, num_rows, num_cols):
    adjacent = []
    top = [row - 1, column, (row - 1) * num_cols + column]
    left = [row, column - 1, (row * num_rows) + column - 1]
    bottom = [row + 1, column, (row + 1) * num_cols + column]
    right = [row, column + 1, (row * num_rows) + column + 1]
    if not out_of_bounds(top, num_rows, num_cols):
        adjacent.append(top)
    if not out_of_bounds(right, num_rows, num_cols):
        adjacent.append(right)
    if not out_of_bounds(left, num_rows, num_cols):
        adjacent.append(left)
    if not out_of_bounds(bottom, num_rows, num_cols):
        adjacent.append(bottom)
    return adjacent
        
board = []
for line in sys.stdin:
    if line[:-1] == '':
        break
    row = line[:-1]
    row_nums = []
    for i in range(len(row)):
        row_nums.append(int(row[i]))
    board.append(row_nums)

path = []

total_risk = 0
num_rows = len(board)
num_cols = len(board[0])
destination_row = num_rows - 1
destination_column = num_cols - 1
current_row = 0
current_column = 0
print(f"Map size: {num_rows} rows {num_cols} cols")


shortest_path_set = [111111111] * (num_rows * num_cols)

min_risks = [99999] * (num_rows * num_cols)
min_risks[0] = 0
num_shortest_found = 0
found = []
while shortest_path_set[(num_rows * num_cols) - 1] == 111111111:
    position = min_risks.index(min(min_risks))
    shortest_path_set[position] = min_risks[position]
    #print(f"minimum in min_risks is at position {position}, with value of {min_risks[position]}")
    #print(f"min_risks: {min_risks}")
    if not position in found:
        num_shortest_found += 1
        if num_shortest_found % 1000 == 0:
            print(f"{num_shortest_found} paths found, most recent is {position}")
        found.append(position)
    else:
        print(f"uhhh this was already found")
        
    position_row = int((position - position % num_rows) / num_rows)
    position_col = position % num_rows
    adjacent = get_adjacent(position_row, position_col, num_rows, num_cols)
    for pair in adjacent:
        row = pair[0]
        column = pair[1]
        vector_position = pair[2]
        if min_risks[position] + board[row][column] < min_risks[vector_position] and not vector_position in found:
            min_risks[vector_position] = min_risks[position] + board[row][column]
    min_risks[position] = 99999

print(f"The total risk is {shortest_path_set[(num_rows * num_cols) - 1]}") #621
#print(f"the path is {path}")