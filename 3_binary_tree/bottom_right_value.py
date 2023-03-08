class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
       
def bottom_right_value(root):
    if root is None:
        return None
    queue = deque([root])
    current = None
    while queue:
        current = queue.popleft()
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return current.val
            