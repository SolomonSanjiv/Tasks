class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
def bound(node, n, W, items):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight
    while j < n and total_weight + items[j][1] <= W:
        total_weight += items[j][1]
        profit_bound += items[j][0]
        j += 1
    if j < n:
        profit_bound += (W - total_weight) * items[j][0] / items[j][1]
    return profit_bound
def knapsack_branch_and_bound(W, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    n = len(items)
    queue = []
    root = Node(-1, 0, 0, 0)
    root.bound = bound(root, n, W, items)
    queue.append(root)
    max_profit = 0
    while queue:
        current_node = queue.pop(0)
        if current_node.level == n - 1:
            continue
        next_level = current_node.level + 1
        left_child = Node(next_level,
                          current_node.profit + items[next_level][0],
                          current_node.weight + items[next_level][1],
                          0)
        if left_child.weight <= W and left_child.profit > max_profit:
            max_profit = left_child.profit
        left_child.bound = bound(left_child, n, W, items)
        if left_child.bound > max_profit:
            queue.append(left_child)
        right_child = Node(next_level,
                           current_node.profit,
                           current_node.weight,
                           0)
        right_child.bound = bound(right_child, n, W, items)
        if right_child.bound > max_profit:
            queue.append(right_child)
    return max_profit
values = [40, 50, 100, 95, 30]
weights = [2, 3.14, 1.98, 5, 3]
capacity = 10
items = list(zip(values, weights))
max_profit = knapsack_branch_and_bound(capacity, items)
print(f"Maximum possible profit: {max_profit}")
