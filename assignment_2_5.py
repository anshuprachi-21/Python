#INPUT FROM USER 
gen=str(input("Enter your gender in from m OR f:"))
age=int(input("Enter your age:"))
c=int(input("If you are from city enter 1 and 0 for village:"))
h=str(input("Enter your health condition enter a for excellent/b for normal/c for poor:"))
#CONDITION CHECK
if gen== 'm' and (age>=25 and age<=35) and h== 'a' and c== 1 :
     print("You are insure ")
     print("Your premium is Rs. 4 per thosend")
     print("your maximum amount for insured is 2 lakh")

elif gen== 'f' and (age>=25 and age<=35) and h== 'a' and c== 1:
     print("You are insure ")
     print("Your premium is Rs. 3 per thosend")
     print("your maximum amount for insured is 1 lakh")
elif gen== 'm'  and (age>=25 and age<=35) and h== 'c' and c== 0:
     print("You are insure ")
     print("Your premium is Rs. 6 per thosend")
     print("your maximum amount for insured is 10,000")
else:
     print("Your are not insured")
