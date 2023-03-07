class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_univalue_list(head):
    val = head.val
    current = head.next
    while current is not None:
        if current.val != val:
            return False
    return True


def is_univalue_list(head, prev_val=None):
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list(head.next, head.val)
    else:
        return False
