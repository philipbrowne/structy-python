from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    sum = 0
    stack = [root]
    while stack:
        node = stack.pop()
        sum += node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return sum


def tree_sum(root):
    if not root:
        return 0
    left_values = tree_sum(root.left)
    right_values = tree_sum(root.right)
    return root.val + left_values + right_values


def tree_sum(root):
    if not root:
        return 0
    sum = 0
    queue = deque([root])
    while queue:
        current = queue.popleft()
        sum += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum
