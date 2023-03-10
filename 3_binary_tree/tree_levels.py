from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def tree_levels(root): # Depth First Iterative
    if root is None:
        return []
    levels = []
    stack = [(root, 0)]
    while stack:
        current = stack.pop()
        if len(levels) <= current[1]:
            levels.append([])
        levels[current[1]].append(current[0].val)
        if current[0].right is not None:
            stack.append((current[0].right, current[1]+1))
        if current[0].left is not None:
            stack.append((current[0].left, current[1]+1))
    return levels

def tree_levels(root): # Breadth First Iterative
    if root is None:
        return []
    levels = []
    queue = deque([(root, 0)])
    while queue:
        current = queue.popleft()
        if len(levels) <= current[1]:
            levels.append([])
        levels[current[1]].append(current[0].val)
        if current[0].left is not None:
            queue.append((current[0].left, current[1]+1))
        if current[0].right is not None:
            queue.append((current[0].right, current[1]+1))
    return levels

def tree_levels(root): # Recursive
    levels = []
    _tree_levels(root, levels, 0)
    return levels

def _tree_levels(root, levels, level_num):
    if root is None:
        return
    if len(levels) <= level_num:
        levels.append([])
    levels[level_num].append(root.val)
    _tree_levels(root.left, levels, level_num+1)
    _tree_levels(root.right, levels, level_num+1)