class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z


def zipper_lists(head1, head2):
    count = 0
    tail = head1
    current1 = head1.next
    current2 = head2
    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    return head1


def zipper_lists(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_lists(next1, next2)
    return head1
