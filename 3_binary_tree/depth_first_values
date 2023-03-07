class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    if not root:
        return []
    values = []
    stack = [root]
    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values


def depth_first_values(root):
    if root is None:
        return None
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]
