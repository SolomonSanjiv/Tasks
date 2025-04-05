def bit_stuffing(data):
    stuffed_data = ""
    count = 0
    for bit in data:
        if bit == '1':
            count += 1
            stuffed_data += bit
            if count == 5:
                stuffed_data += '0'
                count = 0
        else:
            count = 0
            stuffed_data += bit
    return stuffed_data
def bit_destuffing(stuffed_data):
    destuffed_data = ""
    count = 0
    for bit in stuffed_data:
        if bit == '1':
            count += 1
            destuffed_data += bit
            if count == 5:
                continue
        else:
            count = 0
            destuffed_data += bit
    return destuffed_data
data_bits = "11111011111101111110"
stuffed_bits = bit_stuffing(data_bits)
print("Stuffed Bits:", stuffed_bits)
destuffed_bits = bit_destuffing(stuffed_bits)
print("Destuffed Bits:", destuffed_bits)