# SHOW ALL COURSES WITH COURSE CODE
print("Course with course code")
print("BTech=1","BCA=2","BBA=3","BHHA=4")
print("BSc=5","MBA=6","MCA=7")
#Now student input
c_code=int(input("Enter the couese code you want to know the total fees for you:"))
tig=int(input("Enter 1 if you are completed your previous degree from Techno India Group else enter 0:"))
e_test=int(input("Enter 1 if you are admission through rank else 0:"))
gen=str(input("Enter your gender in from m or f:"))
#Code for Course fee check
#FOR BTech Male
if   c_code== 1 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BTech your course fee is:530000 rupees ")
elif c_code== 1 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice Btech your course fee is:545000  rupees")   
elif c_code== 1 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BTech your course fee is:610000 rupees")
elif c_code== 1 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BTech your course fee is:625000 rupees")

   
#For BTech Female 
elif c_code== 1 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice Btech your course fee is:520000 rupees")
elif c_code== 1 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice Btech your course fee is:535000 rupees")
elif c_code== 1 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice Btech your course fee is:600000 rupees")
elif c_code== 1 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice Btech your course fee is:615000 rupees")   


#FOR BCA Male
elif c_code== 2 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BCA your course fee is:325000 rupees ")
elif c_code== 2 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BCA your course fee is:340000 rupees")   
elif c_code== 2 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BCA your course fee is:405000 rupees")
elif c_code== 2 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BCA your course fee is:420000 rupees")

   
#For BCA Female 
elif c_code== 2 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice BCA your course fee is:315000 rupees")
elif c_code== 2 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BCA your course fee is:330000 rupees")
elif c_code== 2 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice BCA your course fee is:395000 rupees")
elif c_code== 2 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BCA your course fee is:410000 rupees")


#FOR BBA Male
elif c_code== 3 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BBA your course fee is:325000 rupees ")
elif c_code== 3 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BBA your course fee is:340000 rupees")   
elif c_code== 3 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BBA your course fee is:405000 rupees")
elif c_code== 3 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BBA your course fee is:420000 rupees")

   
#For BBA Female 
elif c_code== 3 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice BBA your course fee is:315000 rupees")
elif c_code== 3 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BBA your course fee is:330000 rupees")
elif c_code== 3 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice BBA your course fee is:395000 rupees")
elif c_code== 3 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BBA your course fee is:410000 rupees")

#FOR BHHA Male
elif c_code== 4 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BHHA your course fee is:210000 rupees ")
elif c_code== 4 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BHHA your course fee is:225000 rupees")   
elif c_code== 4 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BHHA your course fee is:270000 rupees")
elif c_code== 4 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BHHA your course fee is:285000 rupees")

   
#For BHHA Female 
elif c_code== 4 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice BHHA your course fee is:200000 rupees")
elif c_code== 4 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BHHA your course fee is:215000 rupees")
elif c_code== 4 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice BHHA your course fee is:260000 rupees")
elif c_code== 4 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BHHA your course fee is:275000 rupees")

#FOR BSc Male
elif c_code== 5 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BSc your course fee is:125000 rupees ")
elif c_code== 5 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BSc your course fee is:140000 rupees")   
elif c_code== 5 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice BSc your course fee is:185000 rupees")
elif c_code== 5 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice BSc your course fee is:200000 rupees")

   
#For BSc Female 
elif c_code== 5 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice BSc your course fee is:115000 rupees")
elif c_code== 5 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BSc your course fee is:130000 rupees")
elif c_code== 5 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice BSc your course fee is:175000 rupees")
elif c_code== 5 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice BSc your course fee is:190000 rupees")


#FOR MBA Male
elif c_code== 6 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice MBA your course fee is:3.85 lakh ")
elif c_code== 6 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice MBA your course fee is:4 Lakh")   
elif c_code== 6 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice MBA your course fee is:4.25 Lakh")
elif c_code== 6 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice MBA your course fee is:4.4 Lakh")

   
#For MBA Female 
elif c_code== 6 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice MBA your course fee is:3.75 Lakh")
elif c_code== 6 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice MBA your course fee is:3.9 Lakh")
elif c_code== 6 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice MBA your course fee is:4.15 Lakh")
elif c_code== 6 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice MBA your course fee is:4.3 Lakh")


#FOR MCA Male
elif c_code== 7 and tig== 1 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice MCA your course fee is:3.05 Lakh ")
elif c_code== 7 and tig== 1 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice MCA your course fee is:3.2 Lakh")   
elif c_code== 7 and tig== 0 and e_test== 1 and (gen== 'm' or gen =='M'):
   print("You choice MCA your course fee is:3.45 Lakh")
elif c_code== 7 and tig== 0 and e_test== 0 and (gen== 'm' or gen =='M'):
   print("You choice MCA your course fee is:3.6 Lakh ")

   
#For MCA Female 
elif c_code== 7 and tig== 1 and e_test== 1 and (gen== 'f' or gen =='F'):
   print("You choice MCA your course fee is:2.95 Lakh")
elif c_code== 7 and tig== 1 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice MCA your course fee is:3.1 Lakh")
elif c_code== 7 and tig== 0 and e_test== 1 and (gen== 'F' or gen =='f'):
   print("You choice MCA your course fee is:3.35 Lakh")
elif c_code== 7 and tig== 0 and e_test== 0 and (gen== 'f' or gen =='F'):
   print("You choice MCA your course fee is:3.5 Lakh")




   







   
   
 
