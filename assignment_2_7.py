#MCA COURSE ADDMISSION ELIGIBILITY CHECK
#USER INPUT
g=int(input("Enter 1 if you are graduated else 0:"))
gp=int(input("Eter your percentage in gradution:"))
print("For SC/ST student 45% or 45% up need in graduation else 50%or 50% up needed")
cast=int(input("Enter 1 if your cast is SC/ST else enter 0:"))     
mp=int(input("If you pass with 50% in math in HS or Graduation enter 1 else 0:"))
#CONDITION CHECK
if (g==1 and cast==0 and gp>=50 and mp==1)or (g==1 and cast== 1 and gp>=45 and mp==1):
      print("You are eligible for MCA ")
else:
    print("You are not eligible")
      
      

