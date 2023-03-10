class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def leaf_list(root):
    if root is None:
        return []
    stack = [root]
    leafs = []
    while stack:
        current = stack.pop()
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
        if current.left is None and current.right is None:
            leafs.append(current.val)
    return leafs

def leaf_list(root):
    leafs = []
    _leaf_list(root, leafs)
    return leafs
    
def _leaf_list(root, leafs):
    if root is None:
        return
    if root.left is None and root.right is None:
        leafs.append(root.val)
    _leaf_list(root.left, leafs)
    _leaf_list(root.right, leafs)