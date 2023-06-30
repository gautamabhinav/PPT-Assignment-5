def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle

    return nums[left]

# Test case
nums = [3, 4, 5, 1, 2]
result = find_minimum(nums)
print(result)
