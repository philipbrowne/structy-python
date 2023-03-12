def build_graph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)
    return graph

from collections import deque

def shortest_path(edges, node_a, node_b):
    graph = build_graph(edges)
    queue = deque([(node_a, 0)])
    visited = set([node_a])
    while len(queue) > 0:
        current, distance = queue.popleft()
        if current == node_b:
          return distance
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance+1))
    return -1