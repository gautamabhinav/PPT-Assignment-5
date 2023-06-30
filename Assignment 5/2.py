def count_complete_rows(n):
    k = 0
    while k * (k + 1) // 2 <= n:
        k += 1
    return k - 1

# Test case
n = 5
result = count_complete_rows(n)
print(result)
