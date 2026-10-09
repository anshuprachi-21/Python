r = int(input("Enter Ram age: "))
s = int(input("Enter Shyam age: "))
a = int(input("Enter Ajay age: "))

if r < s and r < a:
    print("Ram is youngest")
elif s < r and s < a:
    print("Shyam is youngest")
else:
    print("Ajay is youngest")
