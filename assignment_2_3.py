# Input the length and breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculation
area = length * breadth
peri = 2 * (length + breadth)

# Comparison
if area > peri:
    print("Area is greater than Perimeter")
else:
    print("Perimeter is greater than Area")
