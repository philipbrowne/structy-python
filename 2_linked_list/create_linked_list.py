class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(vals):
    dummy_head = Node(None)
    tail = dummy_head
    for val in vals:
        tail.next = Node(val)
        tail = tail.next
    return dummy_head.next


def create_linked_list(vals, index=0):
    if index >= len(vals):
        return None
    head = Node(vals[index])
    head.next = create_linked_list(vals, index+1)
    return head
