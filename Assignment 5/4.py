def find_missing_elements(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    
    distinct_nums1 = list(set_nums1 - set_nums2)
    distinct_nums2 = list(set_nums2 - set_nums1)
    
    return [distinct_nums1, distinct_nums2]

# Test case
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = find_missing_elements(nums1, nums2)
print(result)
