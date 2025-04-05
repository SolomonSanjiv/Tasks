def and_gate(x, y):
    return 1 if x == 1 and y == 1 else 0
def nand_gate(x, y):
    return 0 if x == 1 and y == 1 else 1
def or_gate(x, y):
    return 1 if x == 1 or y == 1 else 0
def not_gate(x):
    return 1 if x == 0 else 0
def xor_gate(x, y):
    return 1 if x != y else 0
def nor_gate(x, y):
    return 1 if x == 0 and y == 0 else 0
if __name__ == "__main__":
    a = 1
    b = 0  
    print("AND Gate:", and_gate(a, b))
    print("NAND Gate:", nand_gate(a, b))
    print("OR Gate:", or_gate(a, b))
    print("NOT Gate (a):", not_gate(a))
    print("NOT Gate (b):", not_gate(b))
    print("XOR Gate:", xor_gate(a, b))
    print("NOR Gate:", nor_gate(a, b))
