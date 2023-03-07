class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(head1, head2):
    dummy = Node(None)
    tail = dummy
    current1 = head1
    current2 = head2
    while current1 is not None and current2 is not None:
        if current1.val < current2.val:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    return dummy.next
