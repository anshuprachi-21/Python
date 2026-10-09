d = int(input("Enter number of days you are late: "))

if d <= 5:
    fine = 0.50 * d
    print("Your fine is:", fine, "rupees")

elif d <= 10:
    fine = (0.50 * 5) + (d - 5) * 1
    print("Your fine is:", fine, "rupees")

elif d <= 30:
    fine = (0.50 * 5) + (1 * 5) + (d - 10) * 5
    print("Your fine is:", fine, "rupees")

else:
    print("Membership cancelled")
