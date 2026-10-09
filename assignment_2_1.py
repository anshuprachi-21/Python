#Input cost price and selling price from seller
cp = int(input("Enter the cost price of the item:"))
sp = int(input("Enter the selling price of the item:"))

# Now print how many profit or loss he made
if sp>cp :
    print("The profit is:",sp-cp," rupee")
else:
    print("The loss is:",cp-sp," rupee") 
