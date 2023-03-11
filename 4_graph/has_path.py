def has_path_dfi(graph, src, dst): # Depth First Iterative
    if src not in graph or dst not in graph:
        return False
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False

from collections import deque 

def has_path_bfi(graph, src, dst): # Breadth First Iterative
    if src not in graph or dst not in graph:
        return False
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

def has_path(graph, src, dst): # Recursive
    if src not in graph or dst not in graph:
        return False
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    return False