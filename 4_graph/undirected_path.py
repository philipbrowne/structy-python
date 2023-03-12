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

def undirected_path_dfi(edges, node_a, node_b):
    graph = build_graph(edges)
    stack = [node_a]
    visited = set()
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        if current == node_b:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False

from collections import deque 

def undirected_path_bfi(edges, node_a, node_b):
    graph = build_graph(edges)
    queue = deque([node_a])
    visited = set()
    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)
        if current == node_b:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
    
def undirected_path(edges, node_a, node_b):
    graph = build_graph(edges)
    return has_path(graph, node_a, node_b, set())
    
def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
            if has_path(graph, neighbor, dst, visited):
                return True
    return False 

