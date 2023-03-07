from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    stack = ([root])
    while stack:
        node = stack.pop()
        if node.val == val:
            return True
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return False


def tree_includes(root, val):
    if not root:
        return False
    return root.val == val or tree_includes(root.left, val) or tree_includes(root.right, val)


def tree_includes(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == val:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False
