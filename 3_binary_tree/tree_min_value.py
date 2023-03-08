from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root):
    minimum = float("inf")
    stack = ([root])
    while stack:
        node = stack.pop()
        if node.val < minimum:
            minimum = node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return minimum


def tree_min_value(root):
    if not root:
        return float("inf")
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))


def tree_min_value(root):
    minimum = float("inf")
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val < minimum:
            minimum = current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return minimum
