import sys

nums = []
directions = {}
directions['depth'] = 0
directions['aim'] = 0
directions['forward'] = 0
for line in sys.stdin:
    if line[:-1] == '':
        break
    line_tokenized = line.split(" ")
    key = line_tokenized[0]
    distance = int(line_tokenized[1])
    if key == 'up':
        directions['aim'] -= distance
        if directions['aim'] <= 0:
            print('negative aim!')
    elif key == 'down':
        directions['aim'] += distance
    else:
        directions[key] += distance
        directions['depth'] += (directions['aim'] * distance)
    
    #nums.append(int(line[:-1]))
    
depth = directions['depth']
horizontal = directions['forward']

print(f"depth is {depth}, forward is {horizontal}, multipled is {depth * horizontal}")
num_increases = 0

for num in range(len(nums) - 3):
    sum_1 = sum(nums[num:num+3])
    sum_2 = sum(nums[num+1:num+4])
    if sum_2 > sum_1:
        num_increases += 1
print(f"num increases is {num_increases}")