n = int(input("Enter the length of the list: "))
print("Enter the numbers:")

# Step 1: read list
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)

# Step 2: initialize variables
block_count = 0
current_length = 1
longest = 1

# Step 3: loop from 2nd element to last
for i in range(1, n):
    if arr[i] > arr[i - 1]:   # strictly increasing
        current_length += 1
    else:                     # block ends here
        block_count += 1
        longest = max(longest, current_length)
        current_length = 1    # reset for next block

# Step 4: handle last block (not counted inside loop)
block_count += 1
longest = max(longest, current_length)

# Step 5: output
print("Number of increasing blocks:", block_count)
print("Length of the longest block:", longest)
