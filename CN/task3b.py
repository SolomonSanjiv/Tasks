import sys
def initialize_routing_table(cost_matrix, num_nodes):
    routing_table = []
    for i in range(num_nodes):
        distance = cost_matrix[i][:]
        next_hop = [j if cost_matrix[i][j] != sys.maxsize else -1 for j in range(num_nodes)]
        routing_table.append({"distance": distance, "next_hop": next_hop})
    return routing_table
def update_routing_table(routing_table, cost_matrix, num_nodes):
    updated = False
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                for k in range(num_nodes):
                    if routing_table[i]["distance"][j] > cost_matrix[i][k] + routing_table[k]["distance"][j]:
                        routing_table[i]["distance"][j] = cost_matrix[i][k] + routing_table[k]["distance"][j]
                        routing_table[i]["next_hop"][j] = k
                        updated = True
    return updated
def print_routing_tables(routing_table, num_nodes):
    for i in range(num_nodes):
        print(f"Routing Table for Node {i}:")
        print("Destination\tDistance\tNext Hop")
        for j in range(num_nodes):
            next_hop = "-" if routing_table[i]["next_hop"][j] == -1 else routing_table[i]["next_hop"][j]
            distance = "∞" if routing_table[i]["distance"][j] == sys.maxsize else routing_table[i]["distance"][j]
            print(f"{j}\t\t{distance}\t\t{next_hop}")
        print()
def distance_vector_routing(cost_matrix, num_nodes):
    routing_table = initialize_routing_table(cost_matrix, num_nodes)
    print("Initial Routing Tables:")
    print_routing_tables(routing_table, num_nodes)
    while update_routing_table(routing_table, cost_matrix, num_nodes):
        pass
    print("Final Routing Tables after Convergence:")
    print_routing_tables(routing_table, num_nodes)
if __name__ == "__main__":
    INF = sys.maxsize
    cost_matrix = [
        [0, 2, 5, INF],
        [2, 0, 4, 6],
        [5, 4, 0, 3],
        [INF, 6, 3, 0]
    ]
    num_nodes = len(cost_matrix)
    distance_vector_routing(cost_matrix, num_nodes)