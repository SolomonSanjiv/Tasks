def character_stuffing(data, start, end, escape):
    stuffed = start
    for char in data:
        if char in [start, end, escape]:
            stuffed += escape + char
        else:
            stuffed += char
    return stuffed + end

def character_destuffing(stuffed, start, end, escape):
    destuffed = ""
    i = 0
    while i < len(stuffed):
        if stuffed[i] == escape and i + 1 < len(stuffed):
            destuffed += stuffed[i + 1]
            i += 2
        elif stuffed[i] not in [start, end]:
            destuffed += stuffed[i]
            i += 1
        else:
            i += 1
    return destuffed

data = "A B DLE D E DLE"
start_delim = "DLESTX"
end_delim = "DLEETX"
escape_char = "DLE"

stuffed = character_stuffing(data, start_delim, end_delim, escape_char)
print(f"Stuffed Data: {stuffed}")

destuffed = character_destuffing(stuffed, start_delim, end_delim, escape_char)
print(f"Destuffed Data: {destuffed}")
