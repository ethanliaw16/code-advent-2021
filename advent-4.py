import sys

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

sums = [0] * 12
nums = []
numrows = 0
directions = {}
directions['depth'] = 0
directions['aim'] = 0
directions['forward'] = 0
for line in sys.stdin:
    if line[:-1] == '':
        break
    numrows += 1
    nums.append(line[:-1])
    #101010000100
    
    #nums.append(int(line[:-1]))
alt_nums = list(nums)

for i in range(12):
    num_rows = 0
    col_sum = 0

    num_rows_alt = 0
    col_sum_2 = 0

    zero_alt = []
    one_alt = []

    zero = []
    one = []
    for num in nums:
        col_sum += int(num[i])
        if int(num[i]) > 0:
            one.append(num)
        else:
            zero.append(num)
        num_rows += 1

    for num in alt_nums:
        col_sum_2 += int(num[i])
        if int(num[i]) > 0:
            one_alt.append(num)
        else:
            zero_alt.append(num)
        num_rows_alt += 1
    
    threshold = num_rows/2
    threshold_alt = int(num_rows_alt/2)
    #print(f"zeros: {zero} ones: {one}")
    if(col_sum >= threshold):
        nums = one
    else:
        nums = zero

    if(col_sum_2 >= threshold_alt):
        alt_nums = zero_alt
        if len(alt_nums) == 0:
            alt_nums = one_alt
    else:
        alt_nums = one_alt
        if len(alt_nums) == 0:
            alt_nums = zero_alt
    #print(f"alt nums: {alt_nums}")
    
    #print(f"remaining nums after position {i}: {nums}")
print(f"nums at the end of the loop: {nums} inverse mode nums: {alt_nums}")

#depth = directions['depth']
#horizontal = directions['forward']
#
#print(f"depth is {depth}, forward is {horizontal}, multipled is {depth * horizontal}")
#num_increases = 0
#
#for num in range(len(nums) - 3):
#    sum_1 = sum(nums[num:num+3])
#    sum_2 = sum(nums[num+1:num+4])
#    if sum_2 > sum_1:
#        num_increases += 1
#print(f"num increases is {num_increases}")