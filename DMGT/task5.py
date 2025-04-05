import sys
def is_safe(graph, color_assignment, vertex, color):
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] and color_assignment[neighbor] == color:
            return False
    return True
def graph_coloring(graph, color_assignment, vertex, num_colors):
    if vertex == len(graph):
        return True
    for color in range(1, num_colors + 1):
        if is_safe(graph, color_assignment, vertex, color):
            color_assignment[vertex] = color
            if graph_coloring(graph, color_assignment, vertex + 1, num_colors):
                return True
            color_assignment[vertex] = 0
    return False
def chromatic_number(graph):
    num_vertices = len(graph)
    num_colors = 1
    color_assignment = [0] * num_vertices
    while not graph_coloring(graph, color_assignment, 0, num_colors):
        num_colors += 1
    return num_colors
def main():
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    print("Chromatic Number:", chromatic_number(graph))
if __name__ == "__main__":
    main()
