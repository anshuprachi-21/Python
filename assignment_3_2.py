#user inputs
n=int(input("Enter how many number you need:"))
div=int(input("Enter the divisor:"))
count=0
i=1
num=""
#condition check
while i<=n:
    a=int(input("Enter number:"))
    if(a%div==0):
        count+=1
        if count>1:
            num=num+str(a)+" "
    i+=1
print(num)    
    
