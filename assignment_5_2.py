sales = [
    [5, 7, 0, 2],
    [6, 7, 2, 8],
    [1, 0, 5, 6]
]

pro = len(sales[0])          # Number of products
total = [0] * pro           # Initialize total sales list

# Calculate total sales per product
for day in sales:
    for i in range(pro):
        total[i] += day[i]

# Find maximum and minimum total sales
max_value = max(total)
min_value = min(total)

maxsales = []
minsales = []

# Identify product numbers
for i in range(pro):
    if total[i] == max_value:
        maxsales.append(i + 1)   # Product numbering starts from 1
    elif total[i] == min_value:
        minsales.append(i + 1)

# Print summary
print("Total sales per product:", total)
print("Product(s) with maximum sales:", maxsales)
print("Product(s) with minimum sales:", minsales)
