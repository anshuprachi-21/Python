n = int(input("Enter your basic salary: "))

# Calculation for DA (40%)
da = n * 40 / 100

# Calculation for HRA (20%)
hra = n * 20 / 100

# Total salary
t = n + da + hra

print("Your total salary is:", t)
