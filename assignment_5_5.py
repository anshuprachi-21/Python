# Read input list
a = list(map(int, input("Enter some list of integer:").split()))
n = len(a)

max_len = 0
ans = []

# Traverse the list (excluding first and last element)
for i in range(1, n - 1):

    # Check if a[i] is a peak element
    if a[i] > a[i - 1] and a[i] > a[i + 1]:

        # Expand to the left
        left = i
        while left > 0 and a[left] > a[left - 1]:
            left -= 1

        # Expand to the right
        right = i
        while right < n - 1 and a[right] > a[right + 1]:
            right += 1

        # Current mountain subarray
        curr = a[left:right + 1]

        # Update maximum length mountain
        if len(curr) > max_len:
            max_len = len(curr)
            ans = curr

# Output result
if max_len == 0:
    print("None")
else:
    print(max_len)
    print(ans)
