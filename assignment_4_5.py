"""words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = []

for word in words:
    placed = False
    for group in groups:
        if sorted(word) == sorted(group[0]):
            group.append(word)
            placed = True
            break
    if not placed:
        groups.append([word])

print(groups)"""
# List of words
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# This list will store groups of anagrams
groups = []

# Loop through each word in the list
for word in words:
    # Flag to check whether the word is placed in any group
    placed = False
    
    # Check existing groups
    for group in groups:
        # Compare sorted letters of the current word
        # with sorted letters of the first word in the group
        if sorted(word) == sorted(group[0]):
            # If they match, it means they are anagrams
            group.append(word)
            placed = True
            break
    
    # If the word was not placed in any group
    if not placed:
        # Create a new group with this word
        groups.append([word])

# Print the final grouped anagrams
print(groups)

