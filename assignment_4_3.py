"""a = input("Enter first string: ")
b = input("Enter second string: ")

missing = []

for ch in a:
    if ch not in b:
        missing.append(ch)

if len(missing) == 0:
    print(True)  
else:
    print(False)  
    print("Missing characters:", missing)"""
# Take first string input from the user
a = input("Enter first string: ")

# Take second string input from the user
b = input("Enter second string: ")

# Create an empty list to store missing characters
missing = []

# Check each character in the first string
for ch in a:
    # If the character is NOT present in the second string
    if ch not in b:
        # Add the character to the missing list
        missing.append(ch)

# If no characters are missing
if len(missing) == 0:
    # All characters of 'a' are present in 'b'
    print(True)

# If some characters are missing
else:
    print(False)
    print("Missing characters:", missing)


    

