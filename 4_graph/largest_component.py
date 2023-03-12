def largest_component(graph):
    visited = set()
    largest = float("-inf")
    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:
            largest = size
    return largest

def explore(graph, current, visited):
    if current in visited:
        return 0
    size = 1
    visited.add(current)
    for neighbor in graph[current]:
        if explore(graph, neighbor, visited) == 0:
            size += 1
    return size