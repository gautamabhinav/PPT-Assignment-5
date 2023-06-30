def distance_value(arr1, arr2, d):
    count = 0
    
    for num1 in arr1:
        found = False
        
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break
        
        if not found:
            count += 1
    
    return count

# Test case
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
result = distance_value(arr1, arr2, d)
print(result)
