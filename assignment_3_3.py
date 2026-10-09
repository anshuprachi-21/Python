#input the lenght
n=int(input("Enter the lenght:"))
string=""
c=2
#condision checking for even odd
for i in range(n):
   a=int(input("Enter number:"))
   if c%2==0:
       if a%2==0:
           print("accept")
           string=string+str(a)+","
           c=+1
       else:
           print("skip")
   

   else:
        if a%2!=0:
           print("accept")
           string=string+str(a)+","
           c+=1
        else:
            print("skip")

   i+=1
#show the accepted list values  
print("The list of accepted numbers is ","[",string,"]")
