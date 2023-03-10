class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from statistics import mean

def level_averages(root): # Recursive
    levels = []
    _tree_levels(root, levels, 0)
    avgs = []
    for level in levels:
        avgs.append(mean(level))
    return avgs

def _tree_levels(root, levels, level_num):
    if root is None:
        return
    if len(levels) <= level_num:
        levels.append([])
    levels[level_num].append(root.val)
    _tree_levels(root.left, levels, level_num+1)
    _tree_levels(root.right, levels, level_num+1)