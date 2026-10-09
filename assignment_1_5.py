
num = int(input("Enter a five-digit number: "))

# Extract digits
a = num // 10000
b = (num // 1000) % 10
c = (num // 100) % 10
d = (num // 10) % 10
e = num % 10

# Add 1 to each digit and wrap using %10
a = (a + 1) % 10
b = (b + 1) % 10
c = (c + 1) % 10
d = (d + 1) % 10
e = (e + 1) % 10

# Recombine digits
new_num = a*10000 + b*1000 + c*100 + d*10 + e

print("New number:", new_num)
