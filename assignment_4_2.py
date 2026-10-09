"""s1=input("Enter a string with number:")
num_list=[]
n=0
for i in s1:
    if ord(i)>=48 and ord(i)<=57:
        v=ord(i)
        dif=v-48
        num_list.append(dif)
if num_list==[]:
    print("No number is available in this string")
else:        
    print(num_list)        
    length=len(num_list)
    i=0
    s=0
    mini=num_list[0]
    maxi=num_list[0]
    while i<length:
        s=s+num_list[i]
        if i+1 <length:
            if mini>=num_list[i+1]:
                mini=num_list[i+1]
            if maxi<=num_list[i+1]:
                maxi=num_list[i+1]
        i+=1    
    print("The sum of the list:",s)
    print("The average of the list:",s//length)
    print("Max number of the list:",maxi)
    print("Minimum number of the list:",mini)"""
# Take input string from the user (string may contain numbers and letters)
s1 = input("Enter a string with number: ")
# Create an empty list to store extracted numbers
num_list = []
# Loop through each character in the string
for i in s1:
    # Check if the character is a digit (ASCII value between 48 and 57)
    if ord(i) >= 48 and ord(i) <= 57:
        # Convert character to its ASCII value
        v = ord(i)
        # Convert ASCII value to actual number (0–9)
        dif = v - 48
        # Add the number to the list
        num_list.append(dif)
# If no numbers are found in the string
if num_list == []:
    print("No number is available in this string")
# If numbers are found
else:
    # Print the list of numbers
    print(num_list)
    # Find the length of the number list
    length = len(num_list)
    # Initialize index and sum
    i = 0
    s = 0
    # Assume first number is both minimum and maximum
    mini = num_list[0]
    maxi = num_list[0]
    # Loop through the list
    while i < length:
        # Add current number to sum
        s = s + num_list[i]
        # Compare with next element (if it exists)
        if i + 1 < length:
            if mini >= num_list[i + 1]:
                mini = num_list[i + 1]
            if maxi <= num_list[i + 1]:
                maxi = num_list[i + 1]
        # Move to next index
        i += 1
    # Print results
    print("The sum of the list:", s)
    print("The average of the list:", s // length)
    print("Max number of the list:", maxi)
    print("Minimum number of the list:", mini)

