# Repeated digit-sum program
processed = 0

while True:
    n = int(input("Enter a positive integer (<=0 to stop): "))

    # Stop condition
    if n <= 0:
        break

    processed += 1
    iterations = 0

    # If n already single-digit, iterations remain 0 and final_digit is n
    while n > 9:
        s = 0
        # compute digit sum of n
        while n > 0:
            s += n % 10
            n //= 10
        n = s          # new number for next check
        iterations += 1

    # at this point n is single-digit final result
    print("Iterations:", iterations, ", Final digit:", n)

print("Total numbers processed:", processed)

