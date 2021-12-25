import sys
import math

def plot_line(grid, line):
    #print(line)
    if(line[0][1] == line[1][1]):
        print(f"{line} is horizontal")
        y = line[0][1]
        start = min(line[0][0], line[1][0])
        end = max(line[0][0], line[1][0])
        i = start
        while(i <= end):
            grid[i][y] += 1
            i += 1
    elif(line[0][0] == line[1][0]):
        print(f"{line} is vertical")
        x = line[0][0]
        start = min(line[0][1], line[1][1])
        end = max(line[0][1], line[1][1])
        i = start
        while(i <= end):
            grid[x][i] += 1
            i += 1
    else:
        slope = (line[1][1] - line[0][1])/(line[1][0] - line[0][0])
        left = []
        oright = []
        if(line[0][0] < line[1][0]):
            left = line[0]
        else:
            left = line[1]
        if slope > 1:
            pass
        else:
            pass
        

max_x = 0
max_y = 0
grid = []
segments = []
for line in sys.stdin:
    if line[:-1] == '':
        break
    segment = line.replace('\n', '').split(' -> ')
    segment_tokenized = []
    for point in segment:
        coordinates = point.split(',')
        point_as_int = []
        max_x = max(int(coordinates[0]), max_x)
        max_y = max(int(coordinates[1]), max_y)
        point_as_int.append(int(coordinates[0]))
        point_as_int.append(int(coordinates[1]))
        segment_tokenized.append(point_as_int)
    segments.append(segment_tokenized)

for i in range(max_y + 1):
    grid.append([0]*(max_x + 1))
#print(f"grid dims: x {len(grid)} y {len(grid[0])}")
#print(segments)
for line in segments:
    plot_line(grid, line)
num_intersections = 0
for line in grid:
    for point in line:
        if point > 1:
            num_intersections += 1

print(f"total intersections: {num_intersections}")
