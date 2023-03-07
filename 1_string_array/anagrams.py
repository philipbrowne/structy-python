def anagrams(s1, s2):
    if len(s1) is not len(s2):
        return False
    count = {}
    for char in s1:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for char in s2:
        if char not in count or count[char] <= 0:
            return False
        count[char] -= 1
    return True
