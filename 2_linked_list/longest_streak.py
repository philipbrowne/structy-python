def longest_streak(head):
    if not head:
        return 0
    current = head
    longest_streak = 0
    current_streak = 0
    prev_val = current.val
    while current is not None:
        if current.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1
        prev_val = current.val
        if current_streak > longest_streak:
            longest_streak = current_streak
        current = current.next
    return longest_streak
