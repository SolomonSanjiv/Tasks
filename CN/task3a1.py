def character_stuffing(data, start_delim, end_delim, escape_char):
    stuffed_data = start_delim
    for char in data:
        if char in [start_delim, end_delim, escape_char]:
            stuffed_data += escape_char + char
        else:
            stuffed_data += char
    stuffed_data += end_delim
    return stuffed_data
def character_destuffing(stuffed_data, start_delim, end_delim, escape_char):
    destuffed_data = ""
    i = 0
    while i < len(stuffed_data):
        if stuffed_data[i] == escape_char:
            i += 1
        elif stuffed_data[i] in [start_delim, end_delim]:
            i += 1
            continue
        destuffed_data += stuffed_data[i]
        i += 1
    return destuffed_data
data = "A B DLE D E DLE"
start_delim = "DLESTX"
end_delim = "DLEETX"
escape_char = "DLE"
stuffed = character_stuffing(data, start_delim, end_delim, escape_char)
print("Stuffed Data:", stuffed)
destuffed = character_destuffing(stuffed, start_delim, end_delim, escape_char)
print("Destuffed Data:", destuffed)
