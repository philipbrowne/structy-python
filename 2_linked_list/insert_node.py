class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, val, index):
    if index == 0:
        new_head = Node(val)
        new_head.next = head
        return new_head

    count = 0
    current = head

    while current is not None:
        if index == count+1:
            next = current.next
            current.next = Node(val)
            current.next.next = next
        count += 1
        current = current.next

    return head


def insert_node(head, val, index):
    if head is None:
        if index == 0:
            return Node(val)
        else:
            return None
    if index == 0:
        new_head = Node(val)
        new_head.next = head
        return new_head
    head.next = insert_node(head.next, val, index-1)
    return head


def insert_node(head, val, index, count=0):
    if index == 0:
        new_head = Node(val)
        new_head.next = head
        return new_head

    if head is None:
        return None

    if count == index - 1:
        temp = head.next
        head.next = Node(val)
        head.next.next = temp
        return

    insert_node(head.next, val, index, count+1)

    return head
