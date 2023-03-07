def pair_product(nums, target):
    previous = {}
    for index, num in enumerate(nums):
        compliment = target / num
        if compliment in previous:
            return (previous[compliment], index)
        previous[num] = index
