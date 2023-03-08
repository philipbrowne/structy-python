from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_value_count(root, target):  # DF Recursive
    count = 0
    if root is None:
        return 0
    if root.val == target:
        count += 1
    left_count = tree_value_count(root.left, target)
    right_count = tree_value_count(root.right, target)
    return count + left_count + right_count


def tree_value_count(root, target):  # DF Iterative
    if root is None:
        return 0
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node.val == target:
            count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count


def tree_value_count(root, target):  # BF Iterative
    if root is None:
        return 0
    queue = deque([root])
    count = 0
    while queue:
        current = queue.popleft()
        if current.val == target:
            count += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return count
