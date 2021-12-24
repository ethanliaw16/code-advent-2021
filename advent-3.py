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
numrows = 0
directions = {}
directions['depth'] = 0
directions['aim'] = 0
directions['forward'] = 0
for line in sys.stdin:
    if line[:-1] == '':
        break
    numrows += 1
    #101010000100
    for i in range(12):
        sums[i] += int(line[i])
    #nums.append(int(line[:-1]))
gamma = ''
epsilon = ''
print(f"there were {numrows} rows")
threshold = int(numrows/2)
print(f"the threshold is {threshold}")
for i in range(12):
    print(f"The sum of {i} is {sums[i]}")
    if sums[i] > threshold:
        print(f"1 is most common in {i}")
        gamma += '1'
        epsilon += '0'
    else:
        print(f"0 is most common in {i}")
        gamma += '0'
        epsilon += '1'

print(f"binary gamma: {gamma} binary epsilon: {epsilon}")
dec_gamma = binaryToDecimal(int(gamma))
dec_epsilon = binaryToDecimal(int(epsilon))
print(f"final gamma is {dec_gamma}, final epsilone is {dec_epsilon}, multipled is {dec_epsilon * dec_gamma}")
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