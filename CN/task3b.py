import sys

def initialize_routing_table(cost_matrix):
    INF = sys.maxsize
    num_nodes = len(cost_matrix)
    routing_table = []
    for i in range(num_nodes):
        distance = cost_matrix[i][:]
        next_hop = [j if cost_matrix[i][j] != INF else -1 for j in range(num_nodes)]
        routing_table.append({"distance": distance, "next_hop": next_hop})
    return routing_table

def update_routing_table(routing_table, cost_matrix):
    updated = False
    num_nodes = len(cost_matrix)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                for k in range(num_nodes):
                    if routing_table[i]["distance"][j] > cost_matrix[i][k] + routing_table[k]["distance"][j]:
                        routing_table[i]["distance"][j] = cost_matrix[i][k] + routing_table[k]["distance"][j]
                        routing_table[i]["next_hop"][j] = k
                        updated = True
    return updated

def distance_vector_routing(cost_matrix):
    routing_table = initialize_routing_table(cost_matrix)
    print("Initial Routing Tables:")
    for i, table in enumerate(routing_table):
        print(f"Node {i}: {table}")
    while update_routing_table(routing_table, cost_matrix):
        pass
    print("Final Routing Tables:")
    for i, table in enumerate(routing_table):
        print(f"Node {i}: {table}")

if __name__ == "__main__":
    cost_matrix = [
        [0, 2, 5, sys.maxsize],
        [2, 0, 4, 6],
        [5, 4, 0, 3],
        [sys.maxsize, 6, 3, 0]
    ]
    distance_vector_routing(cost_matrix)
