def operation_count(n):
    count = 0
    for i in range(n):
        count += 1
        for j in range(i):
            count += 1
    return count
n = 5
print("Total operations for n =", n, ":", operation_count(n))
