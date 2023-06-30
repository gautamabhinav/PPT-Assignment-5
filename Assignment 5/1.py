def convert_to_2d_array(original, m, n):
    if m * n != len(original):
        return []  # Impossible to construct 2D array
    
    result = [[0] * n for _ in range(m)]  # Initialize 2D array with zeros
    
    for i in range(len(original)):
        row = i // n  # Calculate the row index
        col = i % n   # Calculate the column index
        result[row][col] = original[i]  # Assign element to the corresponding position in the 2D array
    
    return result

# Test case
original = [1, 2, 3, 4]
m = 2
n = 2
result = convert_to_2d_array(original, m, n)
print(result)
