class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")

a.right = b


def path_finder(root, target):  # Recursive Depth First Solution - O(n^2) Time
    if root is None:
        return None
    if root.val == target:
        return [root.val]
    left_values = path_finder(root.left, target)
    right_values = path_finder(root.right, target)
    if left_values:
        return [root.val, *left_values]
    if right_values:
        return [root.val, *right_values]


def path_finder(root, target):  # Recursive Depth First Solution O(n) time
    result = _path_finder(root, target)
    if result:
        return result[::-1]
    else:
        return None


def _path_finder(root, target):  # Helper Function
    if root is None:
        return None
    if root.val == target:
        return [root.val]
    left_values = _path_finder(root.left, target)
    right_values = _path_finder(root.right, target)
    if left_values is not None:
        left_values.append(root.val)
        return left_values
    if right_values is not None:
        right_values.append(root.val)
        return right_values
