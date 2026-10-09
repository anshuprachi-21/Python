"""s = input("Enter a string: ")
new_s = ""
no_ls = []

for ch in s:
    if ch != " ":
        new_s += ch
    else:
        no_ls.append(new_s)
        new_s = ""

no_ls.append(new_s)

sum_ls = []

for i in range(len(no_ls)):
    dig_s = 0
    
    for ch in no_ls[i]:
        dig_s += int(ch)

    sum_ls.append(dig_s)

max_ln = 1
curr_ln = 1
end = 0

for i in range(1, len(sum_ls)):
    if sum_ls[i] > sum_ls[i - 1]:
        curr_ln += 1
    else:
        curr_ln = 1
    
    if max_ln < curr_ln:
        max_ln = curr_ln
        end = i
start = end - max_ln + 1
for i in range(start, end + 1):
    print(no_ls[i], end = " ")
print("\nLength:", max_ln)
"""
# Input string of numbers
s = input("Enter numbers separated by spaces: ")
# Convert string into list of integers
nums = list(map(int, s.split()))
# Function to calculate digit sum
def digit_sum(n):
    return sum(int(d) for d in str(n))
# Create list of digit sums
digit_sums = [digit_sum(n) for n in nums]

# Initialize variables
max_len = 1
curr_len = 1
end_index = 0
# Find longest increasing digit-sum subsequence
for i in range(1, len(nums)):
    if digit_sums[i] > digit_sums[i - 1]:
        curr_len += 1
        if curr_len > max_len:
            max_len = curr_len
            end_index = i
    else:
        curr_len = 1
# Extract subsequence
start_index = end_index - max_len + 1
result = nums[start_index:end_index + 1]
# Output
print("Longest subsequence:", result)
print("Length:", max_len)
