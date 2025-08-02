# Write a program to find area of cone ?
# (pi constant, others ==> dynamic input from user, Output ==> interger) Use format function

radius = int(input("Enter radius of cone:"))
length = int(input("Enter length of cone:"))
area= 3.14*radius*length
print(f"The area of cone is:{area}")
height = int(input("Enter height of cone:"))
volume =  (1/3) *3.14*radius*radius*height
print(f"The volume of cone is:{volume}")