import sys

def out_of_bounds(pair):
    return pair[0] < 0 or pair[0] > 99 or pair[1] < 0 or pair[1] > 99

def get_adjacent(row, column):
    adjacent = []
    top = [row - 1, column, (row - 1) * 100 + column]
    left = [row, column - 1, (row * 100) + column - 1]
    bottom = [row + 1, column, (row + 1) * 100 + column]
    right = [row, column + 1, (row * 100) + column + 1]
    if not out_of_bounds(top):
        adjacent.append(top)
    if not out_of_bounds(right):
        adjacent.append(right)
    if not out_of_bounds(left):
        adjacent.append(left)
    if not out_of_bounds(bottom):
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

while(current_row < destination_row and current_column < destination_column):
    risk_of_right = board[current_row][current_column + 1]
    risk_of_down = board[current_row + 1][current_column]
    if(risk_of_down < risk_of_right):
        path.append('D')
        current_row += 1
        total_risk += risk_of_down
    else:
        path.append('R')
        current_column += 1
        total_risk += risk_of_right

print(f"we are now at {current_row} {current_column}")

if current_row < destination_row:
    while(current_row < destination_row):
        current_row += 1
        total_risk += board[current_row][current_column]
        path.append('D')

if current_column < destination_column:
    while(current_column < destination_column):
        current_column += 1
        total_risk += board[current_row][current_column]
        path.append('R')

shortest_path_set = [111111111] * 10000

min_risks = [99999] * 10000
min_risks[0] = 0
num_shortest_found = 0
while shortest_path_set[9999] == 111111111:
    position = min_risks.index(min(min_risks))
    #print(f"shortest path set has {num_shortest_found}, sum of minimum risks is {sum(min_risks)}, cost to destination is {shortest_path_set[9999]}")
    shortest_path_set[position] = min_risks[position]
    num_shortest_found += 1
    position_row = int((position - position % num_rows) / num_rows)
    position_col = position % num_rows
    adjacent = get_adjacent(position_row, position_col)
    for pair in adjacent:
        row = pair[0]
        column = pair[1]
        vector_position = pair[2]
        if min_risks[position] + board[row][column] < min_risks[vector_position]:
            min_risks[vector_position] = min_risks[position] + board[row][column]
    min_risks[position] = 9999999

print(f"The total risk is {shortest_path_set[9999]}") #621
#print(f"the path is {path}")