class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Recursive - O(n) Runtime
def how_high(node):
    if node is None:
        return -1
    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)
    