# List of numbers
nums = [2, 4, 6, 8, 10]

# Window size
k = 3
# List to store (mean, variance) for each window
result = []

# Loop to create sliding windows
for i in range(len(nums) - k + 1):

    # Create a window of size k
    window = nums[i : i + k]

    # Calculate mean of the window
    mean = sum(window) / k

    # Initialize variance sum
    var_sum = 0

    # Calculate sum of squared differences
    for x in window:
        var_sum += (x - mean) ** 2

    # Calculate variance
    variance = var_sum / k

    # Store mean and variance as a tuple
    result.append((mean, variance))

# Print final result
print(result)
