def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    polynomial_bitstring = polynomial_bitstring.lstrip("0")
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    while "1" in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index("1")
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(
                int(polynomial_bitstring[i] != input_padded_array[cur_shift + i])
            )
    return "".join(input_padded_array)[len_input:]
def crc_check(input_bitstring, polynomial_bitstring, check_value):
    polynomial_bitstring = polynomial_bitstring.lstrip("0")
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while "1" in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index("1")
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(
                int(polynomial_bitstring[i] != input_padded_array[cur_shift + i])
            )
    return "1" not in "".join(input_padded_array)[len_input:]
input_bits = "11010011101100"
polynomial_bits = "1011"
initial_filler = "0"
remainder = crc_remainder(input_bits, polynomial_bits, initial_filler)
print("CRC Remainder:", remainder)
check_result = crc_check(input_bits, polynomial_bits, remainder)
print("CRC Check Passed:", check_result)
