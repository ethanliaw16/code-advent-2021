from email.mime import image
import sys

image_key = '##.##.#..###....##..##.#.##...#..#..##.####..##...###.....##.####.##.##.##...####.######..#.###.#.##..###.#..#####...#.##.#..#.#.#..######..###.##.#..##.#..##..##..#...###.##..####.#..#....#####.#.###..##.....#...#.##.#####.###.###....#.#..###.##.##.#..##.##.#.##..##.##.##..###.#.#....#.##..###.###.#.##......#.##..#..#.#...##.##.....###...#..#...###..##.####..#..##..#.#..###......#.#####....#####..###..####...###.#.####..#.##..#.#####..##...##.#.#.#...##.#...#.##.##..#.#.##....##.####.#.#..#.##.#.#..#..#.#.'
sample_key = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
def binary_string_to_decimal(binary_num):
    result = 0
    current_bit = len(binary_num) - 1
    power2 = 0
    while(current_bit >= 0):
        result += int(binary_num[current_bit]) * (2**power2)
        current_bit -= 1
        power2 += 1
    return result

def binary_string_for_position(row, column, board):
    top = [row - 1, column, (row - 1) * 10 + column]
    left = [row, column - 1, (row * 10) + column - 1]
    bottom = [row + 1, column, (row + 1) * 10 + column]
    right = [row, column + 1, (row * 10) + column + 1]
    top_left = [row - 1, column - 1]
    top_right = [row - 1, column + 1]
    bottom_left = [row + 1, column - 1]
    bottom_right = [row + 1, column + 1]
    binary_string = ''
    binary_string += board[top_left[0]][top_left[1]]
    binary_string += board[top[0]][top[1]]
    binary_string += board[top_right[0]][top_right[1]]
    binary_string += board[left[0]][left[1]]
    binary_string += board[row][column]
    binary_string += board[right[0]][right[1]]
    binary_string += board[bottom_left[0]][bottom_left[1]]
    binary_string += board[bottom[0]][bottom[1]]
    binary_string += board[bottom_right[0]][bottom_right[1]]
    return binary_string.replace('.','0').replace('#','1')

def add_border_to_board(board):
    new_board = []
    horizontal_border = ''
    for i in range(len(board[0]) + 2):
        horizontal_border += '.'
    for row in board:
        new_board.append('.' + row + '.')
    return [horizontal_border] + new_board + [horizontal_border]

board = []
for line in sys.stdin:
    if line[:-1] == '':
        break
    board.append(line[:-1])
    
#8000728

test_binary_string = binary_string_for_position(1,1,board)
print(f"the index of the first position is {test_binary_string}, or {binary_string_to_decimal(test_binary_string)}")
print(f"board is {len(board)} rows by {len(board[0])} cols")
#for i in range(3):
#    board = add_border_to_board(board)
for j in range(2400):
    board = add_border_to_board(board)
for i in range(2):
    
    
    #print(f"board:")
    #for row in board:
    #    print(row)
    #print("Applying filter")
    output_board = list(board)
    input_row = 1
    
    while input_row < len(board) - 1:
        #print(f"row {input_row}")
        input_col = 1
        while input_col < len(board[0]) - 1:
            #print(board[input_row][input_col])
            output_key_index = binary_string_to_decimal(binary_string_for_position(input_row, input_col, board))
            output_val = image_key[output_key_index]
            output_board[input_row] = output_board[input_row][:input_col] + output_val + output_board[input_row][input_col + 1:]
            input_col += 1
        input_row += 1
    
    #print("resulting image:")
    #for row in output_board:
    #    print(row)
    board = output_board

num_lit = 0
for row in board:
    for pixel in row:
        if pixel == '#':
            num_lit += 1
print(f"final number of lit pixels is {num_lit}")


    