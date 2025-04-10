def bit_stuffing(data):
    stuffed = ""
    count = 0
    for bit in data:
        if bit == '1':
            count += 1
            stuffed += bit
            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0
            stuffed += bit
    return stuffed

def bit_destuffing(stuffed):
    destuffed = ""
    count = 0
    for bit in stuffed:
        if bit == '1':
            count += 1
            destuffed += bit
            if count == 5:
                count = 0
                continue
        else:
            count = 0
            destuffed += bit
    return destuffed

data_bits = "11111011111101111110"
stuffed_bits = bit_stuffing(data_bits)
print(f"Stuffed Bits: {stuffed_bits}")
destuffed_bits = bit_destuffing(stuffed_bits)
print(f"Destuffed Bits: {destuffed_bits}")
