def fractional_knapsack(values, weights, capacity):
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
    items.sort(key=lambda x: x[2], reverse=True)
    total_value = 0
    remaining_capacity = capacity
    for value, weight, ratio in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += value * (remaining_capacity / weight)
            break
    return total_value
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in the knapsack: {max_value}")
