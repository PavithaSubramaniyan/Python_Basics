a= int(input("Please enter A Value: "))
b= int(input("Please enter B Value: "))

#ArthimeticOperator
print("******Arithmetic Operator****")
print("Adding a and b value:",a+b)
print("Subtracting a and b value:",a-b)
print("Multiplying a and b value:",a*b)
print("Divisioning a and b value:",a/b)
print("Floor Divisioning a and b value:",a//b)
print("Modulus of a and b value:",a%b)
print("Square value of a and b value:",a**b)
print("Square value of a and b value:",b**2)


#AssignmentOperator
print()
print("******Assignment Operator*****")
print("a is Smaller Value of b value:",a<b)
print("a is Larger Value of and b value:",a>b)
print("A is greater than or equal to b",a>=b)
print("Compare a and b value is equal or not:",a==b)
print("A is not equal to B:",a!=b)


#LogicalOperator
print()
print("*******Logical Operator*******")
print("a is greater than 10 or b is less than 15",a>10 or b>15)
print("a is greater than 10 and b is less than 15", a<10 and b>15)
print("a is equal to 10 and b is less than 15", a==10 and b>15)


print()
#Ternary operator
print("*******Ternary Operator*******")
b= 10 if a > 10 else 20
print("b value:",b)


print()
#membership operator
print("*******membership Operator*******")
print("pa in pavitha", "pa" in "pavitha")
print("sv not in pavitha", "sv" not in "pavitha")