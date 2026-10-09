"""s1=input("Enter a stinng:")
s2=input("Enter another string:")
len1=len(s1)
len2=len(s2)
i=0
j=len2-1
s3=""
while i < len1 and j >= 0:
    s3 += s1[i] + s2[j]
    i += 1
    j -= 1


if i < len1:
    s3 += s1[i:]

if j >= 0:
    s3 += s2[j::-1]

print("Result:", s3)"""

# Take first string input from the user
s1 = input("Enter a string: ")
# Take second string input from the user
s2 = input("Enter another string: ")

# Find the length of both strings
len1 = len(s1)
len2 = len(s2)

# i will start from the beginning of s1
i = 0

# j will start from the last character of s2
j = len2 - 1

# Empty string to store the final result
s3 = ""

# Loop runs while there are characters left in both strings
while i < len1 and j >= 0:
    # Add one character from s1 (front)
    # and one character from s2 (back)
    s3 += s1[i] + s2[j]
    
    # Move to next character in s1
    i += 1
    
    # Move to previous character in s2
    j -= 1

# If s1 has extra characters left, add them to result
if i < len1:
    s3 += s1[i:]

# If s2 has extra characters left, add them in correct order
if j >= 0:
    s3 += s2[j::-1]
# Print the final mixed string
print("Result:", s3)

