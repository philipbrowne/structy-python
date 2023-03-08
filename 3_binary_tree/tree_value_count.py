from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_value_count(root, target): # Depth First Iterative
    if root is None:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == target:
            count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count

def tree_value_count(root, target): # Depth First Recursive
    if root is None:
        return 0
    count = 0
    if root.val == target:
        count += 1
    count_left = tree_value_count(root.left, target)
    count_right = tree_value_count(root.right, target)
    return count + count_left + count_right

def tree_value_count(root, target): # Breadth First
    if root is None:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == target:
            count += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return count