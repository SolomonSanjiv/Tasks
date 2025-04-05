def multistage_shortest_path(graph, source, destination, stages):
    INF = float('inf')
    n = len(graph)
    dp = [INF] * n
    dp[destination] = 0
    for stage in range(stages - 1, 0, -1):
        for vertex in range(n):
            if graph[vertex][0] == stage:
                for neighbor, weight in graph[vertex][1].items():
                    dp[vertex] = min(dp[vertex], weight + dp[neighbor])
    return dp[source]
graph = [
    (1, {3: 2, 4: 9}),
    (1, {3: 6, 4: 3}),
    (2, {4: 1}),
    (2, {5: 4}),
    (3, {5: 7}),
    (3, {6: 2}),
    (4, {5: 1, 6: 5}),
    (4, {6: 6}),
    (5, {}),
    (5, {}),
    (6, {}),
]
source = 0
destination = len(graph) - 1
stages = 7
shortest_path_distance = multistage_shortest_path(graph, source, destination, stages)
print("Shortest path distance from source to destination:", shortest_path_distance)
