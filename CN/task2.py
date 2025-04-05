def bitmap_protocol(stations):
    n = len(stations)
    slots = [0] * n
    for i in range(n):
        if stations[i] == 1:
            slots[i] = 1
    print("Contention Slots:")
    for i in range(n):
        print(f"Slot {i + 1}: {'1' if slots[i] == 1 else '0'}")
    print("\nTransmission Order:")
    for i in range(n):
        if slots[i] == 1:
            print(f"Station {i + 1} transmits.")
stations = [0, 1, 0, 1, 1]
bitmap_protocol(stations)
