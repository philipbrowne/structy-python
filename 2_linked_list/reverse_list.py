class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        next.next = current
        current = next
    return head


def reverse_list(head, prev=None):
    if head is None:
        return head
    next = head.next
    head.next = prev
    next.next = head
    return reverse_list(head.next, head)
