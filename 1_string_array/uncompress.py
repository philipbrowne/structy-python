def uncompress(s):
    res = []
    i = 0
    j = 0
    nums = '0123456789'
    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            num = int(s[i:j])
            for n in range(num):
                res.append(s[j])
            j += 1
            i = j
    return ''.join(res)
