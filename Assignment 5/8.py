from collections import Counter

def find_original(changed):
    count = Counter(changed)

    for num in changed:
        doubled_num = num * 2
        if doubled_num not in count or count[doubled_num] == 0:
            return []

        count[doubled_num] -= 1

    return list(count.keys())

# Test case
changed = [1, 3, 4, 2, 6, 8]
original = find_original(changed)
print(original)
