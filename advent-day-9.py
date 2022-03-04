import sys

def out_of_bounds(pair, num_rows, num_cols):
    return pair[0] < 0 or pair[0] > (num_rows - 1) or pair[1] < 0 or pair[1] > (num_cols - 1)

def get_adjacent(row, column, num_rows, num_cols):
    adjacent = []
    top = [row - 1, column]
    left = [row, column - 1]
    bottom = [row + 1, column]
    right = [row, column + 1]
    if not out_of_bounds(top, num_rows, num_cols):
        adjacent.append(top)
    if not out_of_bounds(right, num_rows, num_cols):
        adjacent.append(right)
    if not out_of_bounds(left, num_rows, num_cols):
        adjacent.append(left)
    if not out_of_bounds(bottom, num_rows, num_cols):
        adjacent.append(bottom)
    return adjacent

def get_adjacent_unused(row, column, num_rows, num_cols, basins):
    adjacent = []
    top = [row - 1, column]
    left = [row, column - 1]
    bottom = [row + 1, column]
    right = [row, column + 1]
    if not out_of_bounds(top, num_rows, num_cols) and not top in basins:
        adjacent.append(top)
    if not out_of_bounds(right, num_rows, num_cols) and not right in basins:
        adjacent.append(right)
    if not out_of_bounds(left, num_rows, num_cols) and not left in basins:
        adjacent.append(left)
    if not out_of_bounds(bottom, num_rows, num_cols) and not bottom in basins:
        adjacent.append(bottom)
    return adjacent

def board_value_greater(point1, point2, board):
    return board[point1[0]][point1[1]] > board[point2[0]][point2[1]] and board[point1[0]][point1[1]] != 9

def get_adjacent_to_region(points, num_rows, num_columns, board, basin):
    adjacent_to_region = []
    added_points = []
    for point in points:
        adjacent = get_adjacent_unused(point[0], point[1], num_rows, num_columns, basin)
        for adjacent_point in adjacent:
            if not adjacent_point in points and not adjacent_point in added_points and board_value_greater(adjacent_point, point, board):
                adjacent_to_region.append(adjacent_point)
                added_points.append(adjacent_point)
    return adjacent_to_region

board = []
in_basin = []

for line in sys.stdin:
    if line[:-1] == '':
        break
    row = line[:-1]
    row_nums = []
    for i in range(len(row)):
        row_nums.append(int(row[i]))
    board.append(row_nums)
low_point_vals = []
low_point_coordinates = []
basins = []
basin_sizes = []
points_in_basins = []
num_rows = len(board)
num_cols = len(board[0])
for i in range(num_rows):
    for j in range(num_cols):
        current = board[i][j]
        adjacent = get_adjacent(i, j, num_rows, num_cols)
        adjacent_values = []
        basin = []

        for pair in adjacent:
            pair_val = board[pair[0]][pair[1]]
            if pair_val != 9:
                adjacent_values.append(pair_val)
                basin.append(pair)
        adjacent_values.append(current)
        basin.append([i,j])
        
        if current != 9 and current == min(adjacent_values):        
            low_point_coordinates.append([i,j])
            low_point_vals.append(current + 1)
            adjacent_to_basin = get_adjacent_to_region(basin, num_rows, num_cols, board, points_in_basins)
            while(len(adjacent_to_basin) > 0):
                basin += adjacent_to_basin
                adjacent_to_basin = get_adjacent_to_region(basin, num_rows, num_cols, board, points_in_basins)
            basins.append(basin)
            for point in basin:
                if not point in points_in_basins:
                    points_in_basins.append(point)
            basin_sizes.append(len(basin))
            #print(f"Basin {[i,j]} is {basin}")

print(f"{len(low_point_coordinates)} total low points, sum is {sum(low_point_vals)}")
print(f"{len(basins)} total basins:\n")
print(f"{len(points_in_basins)} total points on the board were found in a basin.")
print(f"Board was {num_rows} by {num_cols}")
first = -1
second = -2
third = -3

for basin in basin_sizes:
    if basin >= first:
        third = second
        second = first
        first = basin
    elif basin >= second:
        third = second
        second = basin
    elif basin >= third:
        third = basin

print(f"Top three basin sizes are {first}, {second}, {third}, multiplied together is {first * second * third}")
print(f"Checking basin points for dupes:")
print(points_in_basins[:100])

    #print(f"{point[0]},{point[1]}: {board[point[0]][point[1]]}")
#print(f"First basin: {basins[0]}")

#print(f"Testing adjacent to region on first low point: {get_adjacent_to_region(basins[0], num_rows, num_cols, board)}")