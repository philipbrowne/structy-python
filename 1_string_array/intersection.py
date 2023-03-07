def intersection(list1, list2):
    set1 = set(list1)
    return [item for item in list2 if item in set1]
