def is_safe(graph, colors, vertex, color):
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True
def graph_coloring_util(graph, m, colors, vertex):
    if vertex == len(graph):
        return True
    for color in range(1, m + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color
            if graph_coloring_util(graph, m, colors, vertex + 1):
                return True
            colors[vertex] = 0
    return False
def graph_coloring(graph, m):
    colors = [0] * len(graph)
    if graph_coloring_util(graph, m, colors, 0):
        print("Solution exists with the following color assignments:")
        print(colors)
        return True
    else:
        print("No solution exists.")
        return False
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3
graph_coloring(graph, m)