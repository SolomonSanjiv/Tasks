def compute_crc(s, p, pad):
    p = p.lstrip("0")
    l = len(s)
    bits = list(s + pad)
    while "1" in bits[:l]:
        i = bits.index("1")
        for j in range(len(p)):
            bits[i+j] = str(int(p[j] != bits[i+j]))
    return "".join(bits)[l:]

def crc_remainder(s, p, f):
    return compute_crc(s, p, f * (len(p.lstrip("0"))-1))

def crc_check(s, p, cv):
    return "1" not in compute_crc(s, p, cv)

input_bits = "11010011101100"
poly = "1011"
rem = crc_remainder(input_bits, poly, "0")
print(f"CRC: {rem}, Valid: {crc_check(input_bits, poly, rem)}")
