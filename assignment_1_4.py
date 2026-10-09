print("NOTE")
print("The amount is multiple of 10/50/100")

n = int(input("Enter the amount you withdraw: "))

# Calculation for 100 notes
hun = n // 100
n1 = n % 100

# Calculation for 50 notes
fiv = n1 // 50
n2 = n1 % 50

# Calculation for 10 notes
ten = n2 // 10

print("Here 100 notes are:", hun)
print("Here 50 notes are:", fiv)
print("Here 10 notes are:", ten)
