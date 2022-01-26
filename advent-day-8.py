import sys

def large_contains_small(large, small):
    for char in small:
        index = 0
        while index < len(large) and large[index] != char:
            index += 1
        if index == len(large):
            return False
    return True

def anagrams(num1, num2):
    if len(num1) != len(num2):
        return False
    for char in num1:
        if not char in num2:
            return False
    return True

patterns = []
outputs = []
for line in sys.stdin:
    if line[:-1] == '':
        break
    vals = line[:-1].split(' ')
    pattern = []
    output = []
    for i in range(10):
        pattern.append(vals[i])
    patterns.append(pattern)

    for i in range(4):
        output.append(vals[i + 11])
    outputs.append(output)
    
num_unique = 0
output_sum = 0
for i in range(len(patterns)):
    current_pattern_map = {
    }
    pattern_map_inverted = {
    0 : '',
    1 : '',
    2 : '',
    3 : '',
    4 : '',
    5 : '',
    6 : '',
    7 : '',
    8 : '',
    9 : '',}
    pattern = patterns[i]
    #print(f"pattern: {pattern}")
    remaining5 = []
    remaining6 = []
    for val in pattern:
        val_len = len(val)
        if val_len == 2:
            #print(f"{val} is 1!")
            current_pattern_map[val] = '1'
            pattern_map_inverted[1] = val
        elif val_len == 3:
            #print(f"{val} is 7!")
            current_pattern_map[val] = '7'
            pattern_map_inverted[7] = val
        elif val_len == 4:
            #print(f"{val} is 4!")
            current_pattern_map[val] = '4'
            pattern_map_inverted[4] = val
        elif val_len == 5:
            remaining5.append(val)
            #print(f"{val} is 2 or 3 or 5!")
        elif val_len == 6:
            remaining6.append(val)
            #print(f"{val} is 6 or 9 or 0!")
        elif val_len == 7:
            #print(f"{val} is 8!")
            current_pattern_map[val] = '8'
            pattern_map_inverted[8] = val
    for val in remaining6:
        if not large_contains_small(val, pattern_map_inverted[1]):
            current_pattern_map[val] = '6'
            pattern_map_inverted[6] = val
        elif not large_contains_small(val, pattern_map_inverted[4]):
            current_pattern_map[val] = '0'
            pattern_map_inverted[0] = val
        else:
            current_pattern_map[val] = '9'
            pattern_map_inverted[9] = val

    for val in remaining5:
        if large_contains_small(val, pattern_map_inverted[1]):
            current_pattern_map[val] = '3'
            pattern_map_inverted[3] = val
        elif large_contains_small(pattern_map_inverted[6], val):
            current_pattern_map[val] = '5'
            pattern_map_inverted[5] = val
        else:
            current_pattern_map[val] = '2'
            pattern_map_inverted[2] = val

    #print(f"Current map: {current_pattern_map}\nInverted map: {pattern_map_inverted} \nremaining: {remaining5} {remaining6}")
    current_output = outputs[i]
    unscrambled = ''
    for val in current_output:
        for key in current_pattern_map:
            if anagrams(val, key):
                unscrambled += current_pattern_map[key]
    print(f"Unscrambled output: {unscrambled}")
    output_sum += int(unscrambled)

print(f"At the end, the sum of outputs is {output_sum}")

