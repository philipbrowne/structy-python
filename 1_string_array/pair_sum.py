def pair_sum(numbers, target):
    previous = {}
    for index, num in enumerate(numbers):
        compliment = target-num
        if compliment in previous:
            return (previous[compliment], index)
        previous[num] = index
