import builtins
from operator import index

#abs, round, sum, dir, len, pow, max, min , int, input  , float, str
#break, elif, continue, def, return, try, except, finally, import, from , as, true, false, and , or, in

print("After abs" ,abs(-3.4))#removes minus sign
print("Afterround ", round(3.4)) #Rounds to nearest integer
print("Using sum method ",sum([3,4]))
print("Show all strings ",dir(str))
print("Show length of all strings ",len(dir(str)))
print("Print power value: ",pow(2,3))#Power (same as **)
print("Max value: ",max(3,4))
print("Min value: ",min(3,4))
print(int("1230"))
print(len(500))
print(input("Enter something:"))
print(float("12.50"))
print(str(12))

#if print("helllo")# syntax error
#print("hello)# syntax error

print("12"+12)#type error
# "python" ===> h with z a[3] = "z"
# TypeError: 'str' object does not support item assignment

# Attribute error : when i try to change int to upper   'int' object has no attribute 'upper'

print(int("python")) #value error
a = "Comp"
print(a.index("z"))#ValueError: substring not found

#print(f"Get this value : {vl}") # nameError


#Keywords

#break to stop loop early
for i in range(5):
    if i ==3:
        break
    print(i)

#elif - extra condition
a = 10
if a <5:
    print("Small")
elif a == 10:
    print("Equal")
else:
    print(a)

#continue skip one loop iteration
for i in range(5):
    if i ==2:
        continue
    print(i)

#def - define a function
def greeting():
    print("Hello")

#return - send value back from function
def sum(a,b):
    return a+b
print(sum(3,4))

#try - start exception handling
try:
    print(10/0)
except:
    print("Error")

#except
try:
    print(10/0)
except:
    print("Error")

#finally – Always runs (even if error occurs)
try:
    x = 5 / 0
except:
    print("Error happened")
finally:
    print("Cleanup done")

#import - used to bring external files or modules,  when you want to use many functions from the module.
import math
print(math.sqrt(2))

#from - when you want to use only 1–2 functions frequently, to avoid typing math. every time.
from cmath import sqrt
print(sqrt(2))

#as -  when you need details of the error (message, type, traceback).
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

import math as m

print(m.pi)

#Value Keywords True, False, Non
#Operator Keywords	and, or, not, is, in

# true
x = True
print(x)          # True

#and -Returns True only if both conditions are True.
# or -️ Returns True if any one condition is True
# in - Checks if a value exists inside a sequence (list, string, tuple, etc.).
a = 5

print(a > 0 and a < 10)  # True (both conditions true)





