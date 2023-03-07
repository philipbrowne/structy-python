class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_node(head, target):
    if head.val == target:
        head = head.next
        return head
    prev = head
    current = head.next
    while current is not None:
        if current.val == target:
            next = current.next
            prev.next = next
            break
        prev = current
        current = current.next
    return head


def remove_node(head, target):
    if head is None:
        return None
    if head.val == target:
        return head.next
    head.next = remove_node(head.next, target)
    return head
