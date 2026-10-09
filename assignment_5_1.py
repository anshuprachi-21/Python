 
"""n=list(input("Enter a list:"))
result=[]

for i in range(len(n)):
    n1=(n[:i]+n[i+1:])
    result.append(n1)

print(result) """   
# Take input from the user and convert it into a list
# Example input: 123
# Resulting list: ['1', '2', '3']
n = list(input("Enter a list: "))

# Create an empty list to store the final result
result = []

# Loop through each index of the list
for i in range(len(n)):
    # Create a new list by removing the element at index i
    n1 = n[:i] + n[i + 1:]
    
    # Add the new list to the result list
    result.append(n1)

# Print all possible lists formed by removing one element
print(result)
