def stats(nums):
    total = 0
    smallest = nums[0]
    largest = nums[0]
    if not nums:
        return None
    for i in nums:
        total += i
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    average = total/ len(nums)
    return smallest, largest, average      
        
print(stats([4, 9, 2, 7]))