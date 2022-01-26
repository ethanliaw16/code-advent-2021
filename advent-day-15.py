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

#board augmentation
full_board = []
for i in range(5 * num_rows):
    full_board.append([0] * 5 * num_cols)

for i in range(num_rows):
    for j in range(num_cols):
        #print(f"updating board {i} {j}. on the original this is {board[i][j]}")
        full_board[i][j] = board[i][j]
        



for i in range(5):
    for j in range(5):
        for row in range(num_rows):
            for col in range(num_cols):
                new_val = board[row][col] + i + j
                if new_val > 9:
                    new_val -= 9
                full_board[row + (num_rows * i)][col + (num_cols * j)] = new_val

#print("\n")
#for row in full_board:
#    print(row)
#print("\n")    
final_destination_row = (5 * num_rows) - 1
final_destination_column = (5 * num_cols) - 1

destination_row = num_rows - 1
destination_column = num_cols - 1
current_row = 0
current_column = 0
print(f"Map size: {num_rows} rows {num_cols} cols")
print(f"Final map size: {len(full_board)} rows {len(full_board[0])}")

shortest_path_set = [111111111] * (num_rows * num_cols * 25)

min_risks = [9999999] * (num_rows * num_cols * 25)
min_risks[0] = 0
num_shortest_found = 0
found = []

while shortest_path_set[(num_rows * num_cols * 25) - 1] == 111111111:
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
        print(f"uhhh this was already found. length of shortest path set: {len(shortest_path_set)}. length of min_risks: {len(min_risks)}")
        print(f"{shortest_path_set[2499]} {min_risks[2499]}. min: {min(min_risks)}")
        
    position_row = int((position - position % (num_rows * 5)) / (num_rows * 5))
    position_col = position % (num_rows * 5)
    adjacent = get_adjacent(position_row, position_col, num_rows * 5, num_cols * 5)
    for pair in adjacent:
        row = pair[0]
        column = pair[1]
        vector_position = pair[2]
        if min_risks[position] + full_board[row][column] < min_risks[vector_position] and not vector_position in found:
            min_risks[vector_position] = min_risks[position] + full_board[row][column]
            
    min_risks[position] = 9999999

print(f"The total risk is {shortest_path_set[(num_rows * num_cols * 25) - 1]}") #621
#print(f"the path is {path}")