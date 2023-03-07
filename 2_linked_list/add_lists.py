class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists(head1, head2):  # Iterative Approach
    dummy_head = Node(None)
    tail = dummy_head
    current1 = head1
    current2 = head2
    carry = 0
    while current1 is not None or current2 is not None or carry == 1:
        num1 = 0 if current1 is None else current1.val
        num2 = 0 if current2 is None else current2.val
        sum = num1 + num2 + carry
        carry = sum // 10
        digit = sum % 10
        tail.next = Node(digit)
        tail = tail.next
        if current1 is not None:
            current1 = current1.next
        if current2 is not None:
            current2 = current2.next
    return dummy_head.next


def add_lists(head1, head2, carry=0):  # Recursive Approach
    if head1 is None and head2 is None and carry == 0:
        return None
    num1 = 0 if head1 is None else head1.val
    num2 = 0 if head2 is None else head2.val
    sum = num1 + num2 + carry
    carry = sum // 10
    digit = sum % 10
    result = Node(digit)
    next1 = head1.next if head1 is not None else None
    next2 = head2.next if head2 is not None else None
    result.next = add_lists(next1, next2, carry)
    return result
