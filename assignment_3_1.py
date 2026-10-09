#Get how many numbers user want
n=int(input("Enter how mny inpute you want:"))
sod=0
soe=0
i=0
#Enter the numbers and sum of evenand odd numbers
while i<=n:
    a=int(input("Enter a number:"))
    if(a%2==0):
        soe+=a
    else:
        sod+=a
    i+=1    

print("Sum of even is: ",soe," Sum of odd is: ",sod)    
        
        

