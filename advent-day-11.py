import sys
import math
sequence = 'OOVSKSPKPPPNNFFBCNOV'

insertion_rules = {}
for line in sys.stdin:
    if line[:-1] == '':
        break
    pair = line[:-1].split(' -> ')
    insertion_rules[pair[0]] = pair[1]
print(f"number of rules: {len(insertion_rules)}")

print(f"original polymer is {sequence}, length is {len(sequence)}")
for i in range(40):
    seqlen = len(sequence)
    print(f"sequence length is {seqlen}")
    sequence_2 = ''
    for j in range(seqlen - 1):
        pair = sequence[j:j+2]
        sequence_2 += sequence[j]
        sequence_2 += insertion_rules[pair]
    sequence_2 += sequence[seqlen - 1]
    sequence = sequence_2
    #if i == 39:
    #    pass
    #else:
    #    sequence_2 += sequence[seqlen - 1]
    #    sequence = sequence_2
    #print(f"new polymer is {sequence}, length is {len(sequence)}")
print(f"length of sequence is {len(sequence)}")
frequencies = {}
for i in range(len(sequence)):
    element = sequence[i]
    if element in frequencies:
        frequencies[element] += 1
    else:
        frequencies[element] = 1

frequencies_as_list = list(frequencies.values())
least = min(frequencies_as_list)
most = max(frequencies_as_list)
print(f"want to subtract {least} from {most}, result is {most - least}")
