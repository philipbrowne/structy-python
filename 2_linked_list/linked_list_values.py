class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    res = []
    current = head
    while current is not None:
        res.append(current.val)
        current = current.next
    return res


def linked_list_values(head, res=[]):
    if head is None:
        return res
    res.append(head.val)
    return linked_list_values(head.next, res)
