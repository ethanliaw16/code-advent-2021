import sys

nums = []

for line in sys.stdin:
    if line[:-1] == '':
        break
    nums.append(int(line[:-1]))
    

num_increases = 0

for num in range(len(nums) - 3):
    sum_1 = sum(nums[num:num+3])
    sum_2 = sum(nums[num+1:num+4])
    if sum_2 > sum_1:
        num_increases += 1
print(f"num increases is {num_increases}")