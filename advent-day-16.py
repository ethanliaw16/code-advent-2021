from base64 import decode
from ensurepip import version
import sys
from tracemalloc import start
from unicodedata import decimal
puzzle_input = '220D700071F39F9C6BC92D4A6713C737B3E98783004AC0169B4B99F93CFC31AC4D8A4BB89E9D654D216B80131DC0050B20043E27C1F83240086C468A311CC0188DB0BA12B00719221D3F7AF776DC5DE635094A7D2370082795A52911791ECB7EDA9CFD634BDED14030047C01498EE203931BF7256189A593005E116802D34673999A3A805126EB2B5BEEBB823CB561E9F2165492CE00E6918C011926CA005465B0BB2D85D700B675DA72DD7E9DBE377D62B27698F0D4BAD100735276B4B93C0FF002FF359F3BCFF0DC802ACC002CE3546B92FCB7590C380210523E180233FD21D0040001098ED076108002110960D45F988EB14D9D9802F232A32E802F2FDBEBA7D3B3B7FB06320132B0037700043224C5D8F2000844558C704A6FEAA800D2CFE27B921CA872003A90C6214D62DA8AA9009CF600B8803B10E144741006A1C47F85D29DCF7C9C40132680213037284B3D488640A1008A314BC3D86D9AB6492637D331003E79300012F9BDE8560F1009B32B09EC7FC0151006A0EC6082A0008744287511CC0269810987789132AC600BD802C00087C1D88D05C001088BF1BE284D298005FB1366B353798689D8A84D5194C017D005647181A931895D588E7736C6A5008200F0B802909F97B35897CFCBD9AC4A26DD880259A0037E49861F4E4349A6005CFAD180333E95281338A930EA400824981CC8A2804523AA6F5B3691CF5425B05B3D9AF8DD400F9EDA1100789800D2CBD30E32F4C3ACF52F9FF64326009D802733197392438BF22C52D5AD2D8524034E800C8B202F604008602A6CC00940256C008A9601FF8400D100240062F50038400970034003CE600C70C00F600760C00B98C563FB37CE4BD1BFA769839802F400F8C9CA79429B96E0A93FAE4A5F32201428401A8F508A1B0002131723B43400043618C2089E40143CBA748B3CE01C893C8904F4E1B2D300527AB63DA0091253929E42A53929E420'
#puzzle_input = '9C0141080250320F1802104A08'
hex_bin_map = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def all_zeros(str):
    for char in str:
        if char != '0':
            return False
    return True

def binary_string_to_decimal(binary_num):
    result = 0
    current_bit = len(binary_num) - 1
    power2 = 0
    while(current_bit >= 0):
        result += int(binary_num[current_bit]) * (2**power2)
        current_bit -= 1
        power2 += 1
    return result

def perform_operation(operator, vals):
    if operator == 0:
        #print(f"Doing sum on {vals}")
        return sum(vals)
    elif operator == 1:
        result = 1
        for val in vals:
            result *= val
        return result
    elif operator == 2:
        return min(vals)
    elif operator == 3:
        return max(vals)
    elif operator == 5:
        return 1 if vals[0] > vals[1] else 0
    elif operator == 6:
        return 1 if vals[0] < vals[1] else 0
    elif operator == 7:
        return 1 if vals[0] == vals[1] else 0

def translate_packet(sequence, start):
    version = binary_string_to_decimal(sequence[start:start + 3])
    packet_type = binary_string_to_decimal(sequence[start+3:start + 6])
    if packet_type == 4:
        return translate_literal_packet(sequence, start)
    else:
        return translate_operator_packet(sequence, start)
    

def translate_literal_packet(sequence, start):
    #need to return literal value, length of packet
    binary_literal_val = ''
    version = binary_string_to_decimal(sequence[start:start + 3])
    next_index = start + 3
    packet_type = sequence[next_index:next_index + 3]
    next_index += 3
    if packet_type != '100':
        print(f"Error! {packet_type} was not a literal")
    while(next_index <= len(sequence) - 5 and sequence[next_index] != '0'):
        binary_literal_val += sequence[next_index + 1:next_index + 5]
        next_index += 5
    binary_literal_val += sequence[next_index + 1:next_index + 5]
    next_index += 5
    literal_packet_length = next_index - start
    decimal_literal_value = binary_string_to_decimal(binary_literal_val)
        #print(f"Got a literal! {sequence[start:start + literal_packet_length]} {[decimal_literal_value, literal_packet_length, version]}")
    #print(f"literal: {sequence[start:start + literal_packet_length]}\nvalue: {binary_literal_val}->{decimal_literal_value}")
    return [decimal_literal_value, literal_packet_length, version]
    
def translate_operator_packet(sequence, start):
    length_type = sequence[start + 6]
    version_number_sum = binary_string_to_decimal(sequence[start:start + 3])
    operator = binary_string_to_decimal(sequence[start + 3:start + 6])
    operator_packet_length = 0
    sub_packet_vals = []
    if length_type == '0':
        total_sub_length = binary_string_to_decimal(sequence[start + 7: start + 7 + 15])
        current_sub_length = 0
        sub_packet_start = start + 7 + 15
        while current_sub_length < total_sub_length:
            translated_packet = translate_packet(sequence, sub_packet_start)
            sub_packet_vals.append(translated_packet[0])
            sub_packet_start += translated_packet[1]
            current_sub_length += translated_packet[1]
            version_number_sum += translated_packet[2]
        operator_packet_length = 7 + 15 + total_sub_length
    else:
        num_sub_packets = binary_string_to_decimal(sequence[start + 7: start + 7 + 11])
        sub_packet_start = start + 7 + 11
        operator_packet_length = 7 + 11
        for i in range(num_sub_packets):
            translated_packet = translate_packet(sequence, sub_packet_start)
            sub_packet_vals.append(translated_packet[0])
            sub_packet_start += translated_packet[1]
            operator_packet_length += translated_packet[1]
            version_number_sum += translated_packet[2]
    evaluated_packet_val = perform_operation(operator, sub_packet_vals)
    return [evaluated_packet_val, operator_packet_length, version_number_sum]

#puzzle_input = ''

#for line in sys.stdin:
#    
#    if line[:-1] == '':
#        break
#    puzzle_input += line[:-1]
decoded_input = ''
for char in puzzle_input:
    decoded_input += hex_bin_map[char]
print(f"decoded with trailing: {decoded_input}")
end_of_packet = len(decoded_input)
#while(decoded_input[end_of_packet] == '0'):
#    end_of_packet -= 1
decoded_input = decoded_input[0:end_of_packet]
current_start = 0
version_number_sum = 0
print(f"decoded: {decoded_input}")
#print("Testing literal packet translation of 00111000000000000110111101000101001010010001001000000000")
#print(f"The result is {translate_packet('00111000000000000110111101000101001010010001001000000000', 0)}")
foo = translate_packet(decoded_input, 0)
#while(current_start < len(decoded_input) and not all_zeros(decoded_input[current_start:])):
#    #get version and type
#    print(f"New loop iteration, current start: {current_start}")
#    translated_packet = translate_packet(decoded_input, current_start)
#    version_number_sum += translated_packet[2]
#    current_start += translated_packet[1]

print(f"The version number sum at the end of this is {foo[2]}, the result of the expression is {foo[0]}")
    #current_position = decoded_input[start_current_sequence]
    #end_current_sequence = decoded_input[start_current_sequence + 1]
    #start_current_sequence += 1

