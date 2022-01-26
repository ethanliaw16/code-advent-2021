import sys

def matching_delimiters(d1, d2):
    return (d1 == '(' and d2 == ')') or (d1 == '{' and d2 == '}') or (d1 == '[' and d2 == ']') or (d1 == '<' and d2 == '>')

delimiter_scores = {')':3,']':57,'}':1197,'>':25137}
closer_scores = {')':1,']':2,'}':3,'>':4}
open_close_pairs = {'(':')','{':'}','[':']','<':'>'}
line_chunks = []
total_score = 0
for line in sys.stdin:
    if line[:-1] == '':
        break
    line_chunks.append(line[:-1])
incomplete_chunks = []
for i in range(len(line_chunks)):
    chunk = line_chunks[i]
    current_index = 0
    found_illegal = ''
    delimiter_stack = []
    while(current_index < len(chunk) and found_illegal == ''):
        current_delimiter = chunk[current_index]
        if(current_delimiter == '(' or
            current_delimiter == '<' or 
            current_delimiter == '{' or 
            current_delimiter == '['):
            delimiter_stack.append(current_delimiter)
        else:
            if len(delimiter_stack) == 0:
                found_illegal = current_delimiter
            else:
                d1 = delimiter_stack.pop()
                if not matching_delimiters(d1, current_delimiter):
                    found_illegal = current_delimiter
        current_index += 1
    if(found_illegal == ''):
        incomplete_chunks.append([chunk, delimiter_stack])
    else:
        total_score += delimiter_scores[found_illegal]


print(f"total incomplete chunks: {len(incomplete_chunks)} out of {len(line_chunks)}")
completion_scores = []
for i in range(len(incomplete_chunks)):
    chunk = incomplete_chunks[i]
    completion_string = ''
    completion_score = 0
    chunk_stack = chunk[1]
    while(len(chunk_stack) > 0):
        current_open = chunk_stack.pop()
        closer = open_close_pairs[current_open]
        completion_string += closer
        completion_score *= 5
        completion_score += closer_scores[closer]
            
    completion_scores.append(completion_score)

    #print(f"the end of {chunk[0][:5]}... is {completion_string} with a score of {completion_score}")
completion_scores.sort()
print(f"{completion_scores}")

middle = int(len(completion_scores)/2)
print(f"The median completion score is {completion_scores[middle]}") #707992290