# List A contains elements to be rotated
A = [1, 2, 3, 4, 5]
# List B contains elements to be added
B = [10, 20, 30, 40, 50]
# Number of positions for right rotation
k = 2
# Find length of list A
n = len(A)
# Handle case when k is greater than length
k = k % n
# List to store rotated elements
rotated = []
# Step 1: Add last k elements of A to rotated list (right rotation)
i = n - k
while i < n:
    rotated.append(A[i])
    i += 1
# Step 2: Add remaining elements from start of A
i = 0
while i < n - k:
    rotated.append(A[i])
    i += 1
# List to store final merged result
result = []

# Step 3: Add rotated A and B element by element
i = 0
while i < n:
    result.append(rotated[i] + B[i])
    i += 1
# Print the rotated list
print("Rotated list A:", rotated)

# Print the final result list
print("Result after merging:", result)
