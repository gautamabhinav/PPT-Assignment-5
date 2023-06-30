from collections import Counter

def findOriginalArray(changed):
    # Check if the length of the changed array is odd
    if len(changed) % 2 != 0:
        return []

    # Count the frequency of each element in the changed array
    freq = Counter(changed)

    # Sort the changed array in ascending order
    changed.sort()

    # Construct the original array
    original = []
    for num in changed:
        # Check if the doubled value is available in the frequency counter
        if freq[num] > 0 and freq[num * 2] > 0:
            original.append(num)
            freq[num] -= 1
            freq[num * 2] -= 1

    # Check if all elements have been used in the original array
    for count in freq.values():
        if count > 0:
            return []

    return original

# Test case
changed = [1, 3, 4, 2, 6, 8]
original = findOriginalArray(changed)
print(original)
