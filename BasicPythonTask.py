# # 1.Write a Python program to print "Hello Python".
# print("Hello Python")
#
# #2. Write a Python program to do arithmetical operations addition and division.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# add = num1 +  num2
# print(f"Addition of {num1} and {num2} is {add}")
# division = num1/num2
# print(f"Division of {num1} and {num2} is {division}")
#
# #3. Write a Python program to find the area of a triangle.
# base = float(input("Enter a base:"))
# height = float(input("Enter a height:"))
# area = 0.5*base*height
# print(f"The area of {base} and {height} is {area}")
#
# #4. Write a Python program to swap two variables. without temp
# a = int(input("Enter an integer to swap:"))
# b = int(input("Enter another integer to swap:"))
# a,b = b,a
# print(f"Swapping two variables a and b is {a} and {b}")
#
# #5. Write a Python program to generate a random number.
# import random
# rand = random.randint(1,10)
# print(f"Random numbers: {rand}")
#
# # 6.Write a Python program to convert kilometers to miles.
# kilometer = float(input("Enter a kilometer: "))
# miles = kilometer * 0.621371
# print(f"Miles: {miles}")
#
# # 7.Write a Python Program to Check if a Number is Odd or Even.
# a = float(input("Enter a number to check even or odd:"))
# if a%2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")
#
# # 8.Write a Python Program to Check Leap Year.
# num = int(input("enter a year: "))
# if((num%4==0) and (num%100!=0))or(num%400==0):
#     print(f"{num} is a leap year")
# else:
#     print(f"{num} is not a leap year")
#
# # 9.Write a Python Program to Display the multiplication Table.
# multi = int(input("Enter a number to do multiplication: "))
# for i in range(1, 11):
#     print(f"Multiplication of {multi} table  {i} X {multi} = {i*multi}")
#
# # 10.Write a Python Program to Find the Factorial of a Number.
# fact = int(input("enter a fact: "))
# factorial = 1
# for i in range (1, fact+1):
#     factorial *= i
# print(f" The factoria number of {fact} is {factorial}")
#
# """ *** Next 10 programs **** """
# #11.Write a Python program to swap two variables.
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# print(f"Original value of {a} and {b}")
# temp = a
# a = b
# b = temp
# print(f"After swap a  and b is {a} and {b}")
#
# #12.Write a Python Program to Check if a Number is Positive, Negative or Zero.
# a = int(input("Enter a number: "))
# if(a > 0):
#     print(f"{a} is positive")
# elif(a == 0):
#     print(f"{a} is zero")
# else:
#     print(f" {a} is negative")

##13.Write a Python Program to Check Prime Number.
# pri = int(input("Enter a number:"))
# prime =[]
#
# for i in range(2, pri):
#     if pri%i ==0:
#         prime.append(i)
#
# if prime:
#     print(prime)
#     print(f"{pri} is not a prime number")
#
# else:
#     print(f"{pri} is a prime number")

# 14.Write a Python Program to Print all Prime Numbers in an Interval.
# low = int(input("Enter a starting number: "))
# high = int(input("Enter a stopping number: "))
# prime = []
# for i in range(low , high+1):
#     if i%2 !=0:
#         prime.append(i)
# print(prime)

##15.Write a Python Program to Print the Fibonacci sequence.
# li = [0,1]
# num = 5
# for i in range(num):
#     li.append(li[-1]+li[-2])
# print(li)
##16. Write a Python Program to Check Armstrong Number.
# num = int(input("Enter a number: "))
# digits = len(str(num))
# sum = 0
# temp = num
#
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digits
#     temp = temp//10
# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")

## 17.Write a Python Program to Find Armstrong Number in an Interval.
# low = int(input("Enter a low number: "))
# high = int(input("Enter a high number: "))
#
# for num in range(low , high +1):
#     digits = len(str(num))
#     sum = 0
#     temp = num
#     while temp >0:
#          digit = temp % 10
#          sum += digit ** digits
#          temp = temp//10
#     if sum == num:
#         print(num)

## 18.Write a Python Program to Find the Sum of Natural Numbers.
# inp = int(input("Enter a string: "))
# sum = 0
#
# for i in range(1, inp+1):
#     sum += i
# print(sum)
# #19.Write a Python program to display calendar.
# import calendar
# year = int(input("Enter a year:  "))
# month = int(input("Enter a month: "))
# calen = calendar.month(year,month)
# print(calen)
## 20.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# deci = int(input("Enter a number: "))
# decToBin = bin(deci)
# decToOctal = oct(deci)
# decToHex = hex(deci)
# print(f"Binary value is {decToBin} , octal value is {decToOctal} and hex value is {decToHex}")

""" 21Write a Python Program To Find ASCII value of a character."""
from collections import OrderedDict
from operator import truediv

char = input("Enter a character: ")
print(ord(char))

""" 22Write a Python Program to Display Fibonacci Sequence Using Recursion."""

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

num = 7
for fi in range(num):
    print(fib(fi))

""" 23Write a Python Program to Find Factorial of Number Using Recursion."""
def factorial (n):
    if n <= 1:
        return n
    else:
        return factorial(n-1) * n
num = 5
for i in range(num+1):
 print(factorial(i))

""" 24Write a Python Program for cube sum of first n natural numbers?"""
def cube(n):
    total = 0
    if n <= 0:
        return "Positive Number"
    else:
        for i in range(1, n+1):
            total += i**3
        return total
n= 2
print(cube(n))

"""25 Write a Python Program to find sum of array."""
# a = input("enter a array")
# arr = list(map(int, a.split()))
# res = sum(arr)
# print("Res value:"+str(res))

def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
arr = [1,2,3]
print(sum(arr))

"""26 Write a Python Program to find largest element in an array"""
def largest_array(arr):
    if not  arr:
        return "array is empty"
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest
array = [190, 80, 100, 170]
print(f"largest{largest_array(array)}")

"""27 Write a Python Program to Split the array and add the first part to the end?"""
def split_array(arr,k):
    return arr[k:]+ arr[:k]

arra = [1,2,3,4,5]
k = 3
result = split_array(arra, k)
print(f"Split array{result}")

"""28 Write a Python Program to Sort Words in Alphabetic Order."""
def sort_words(words):
    return sorted(words)
strc = "ampyhib"
res = ''.join(sort_words(strc))
print(res)
"""29 Write a Python Program to Remove Punctuation From a String."""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
strs = "@#$#%%%gsgrgsfhs@$@"
val = ""
for char in strs:
    if char not in punctuations:
        val += char

print(val)

"""30 Write a Python program to Multiply all numbers in the list."""
def multiply(li):
    total = 1
    for i in li:
        total *= i
    return total
list_m = [1,2,3,3]
print(f"Multiply list  {multiply(list_m)}")

""" 31 Write a Python program to find sum of elements in list"""
def sum_of_list(li):
    total = 0
    for i in li:
        total += i
    return total
list_s =[10, 20, 30, 40, 50]
print(f"Sum of list  {sum_of_list(list_s)}")

"""32 Write a Python program to find smallest number in a list."""
def smalles(li):
    smallest = arr[0]
    for i in li:
        if i <  smallest:
            smallest = i
    return smallest
arr = [4,5,2,-4]
print(smalles(arr))

"""33 Write a Python program to find second largest number in a list."""
def second_largest(li):
    li.sort()
    print(f"Second largest number in list {li}")
    if len(li) >= 2:
     return li[-2]
    else:
        return "Too small"



# numbers = [30, 10, 45, 5, 20]
# numbers.sort(reverse=True)
# if len(numbers) >= 2:
# second_largest = numbers[1]
#  print("The second largest number in the list is:", second_largest)
#  else:
#  print("The list does not contain a second largest number.")
# arr = [4,5,8,9]
# print("Second largest",second_largest(arr))

"""34 Write a Python program to find N largest elements from a list."""
def largest_elements(li,n):
    li.sort(reverse = True)
    return li[:n]
arr = [4, 7, 8, 9, 12, 56, 78, 90,8]
n= 3
print("n largest elements",largest_elements(arr,n))

"""35  Write a Python program to print even numbers in a list."""
def even_numbers(li):
    even= []
    for i in li:
        if i%2 == 0:
            even.append(i)
    return even
arr = [4, 7, 8, 9, 12, 56, 78, 90,8]
print("Even numbers", even_numbers(arr))

"""36  Write a Python program to print odd numbers in a List."""
def odd_numbers(li):
    odd =[num for num in li if num%2 !=0]
    return odd
arr = [4, 7, 8, 9, 12, 56, 78, 90,8]
print("Odd numbers", odd_numbers(arr))

"""37  Write a Python program to Remove empty List from List."""
def empty_list(empty):
    filter = []
    for sublist in empty:
        if sublist:
            filter.append(sublist)
    return filter

arr = [[1,2,3],[],[],[5,7,9]]
print("Empty list", empty_list(arr))

"""38  Write a Python program to Cloning or Copying a list."""
# 1. Using Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
copiedlist = original_list[:]
# copiedlist1 = list(original_list)
copiedlist3 = [item for item in original_list]

"""39  Write a Python program to Count occurrences of an element in a list."""
def count_occurrences(listm, elements):
    return listm.count(elements)

li = [1,2,3,4,5,6,2,4,5,2,2,1]
elements=2
print("Remove roit", count_occurrences(li,elements))

"""40  Write a Python program for removing i th character from a string."""
def remove_char(string, ele):
 return string[:ele]+string[ele+1:]
strm = "hello , wWorld "
element = 8
print(remove_char(strm,element))

"""41  Write a Python program to find words which are greater than given length k."""
def greater(words, k):
    li= []
    for word in words:
        if len(word) > k:
            li.append(word)
    return li

lim = ["apple", "sdfghfgh", "dsfghkdsrteyui", "makog"]
print(greater(lim, 5))

"""42  Write a Python program to split and join a string."""
string = "the mah tiuo9 jppg jio"
spli = string.split()
print(spli)
jmerge =" "
joi = " ".join(spli)
print(joi)

"""43  Write a Python program to check if a given string is binary string or not."""
def binary_string(string):
    for i in string:
        if i not in "01":
            return False
    return True
li = "67990243"
print(binary_string(li))

"""44  Write a Python program to find uncommon words from two Strings."""
def uncommon_words(a, b):
    word1 = set(a.split())
    print(word1)
    word2 = set(b.split())
    return list(word1.symmetric_difference(word2))

s1 = "This is the first string"
s2 = "This is the second string"
print("Uncommon words:", uncommon_words(s1, s2))

"""45. Write a Python Program to check if a string contains any special character."""
def special_character(string):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    for char in string:
        if char  in pattern:
            return True
    return False

strsvm = "Hello, world!"
contains = special_character(strsvm)

if contains:
    print("string contains special character")
else:
    print("string does not contain special character")

"""46. Write a Python program to find all duplicate characters in string."""
def duplicate_characters(string):
    counts ={}
    for char in string:
        if char in counts:
            counts[char] +=1
        else:
            counts[char] = 1
    duplicates = []
    for ch in counts:
        if counts[ch] >1 and ch !=" ":
            duplicates.append(ch)
    return duplicates

strsv = "Pavithiia"
res = duplicate_characters(strsv)
print(res)

"""47.  Write a Python program to Extract Unique dictionary values."""
mydict = {
    'a':10,
    'b':10,
    'c':30,
    'd':20,
    'e':30
}
unique = set()
for value in mydict.values():
    unique.add(value)

print(list(unique))
"""48.  Write a Python program to find the sum of all items in a dictionary."""
def sum_dict(dict1):
    sum = 0
    for value in dict1.values():
        sum += value
    return sum
dicts = {
 'a': 10,
 'b': 20,
 'c': 30,
 'd': 40,
 'e': 50
 }
print(sum_dict(dicts))
"""49.  Write a Python program to Merging two Dictionaries."""
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)

merge = {**dict1, **dict2}
print(merge)
"""50.  Write a Python program to convert key-values list to flat dictionary."""
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict= {}
for key, value in key_values_list:
    flat_dict[key] = value
print(flat_dict)

"""51.   Write a Python program to insertion at the beginning in OrderedDict."""
orderd_dict = OrderedDict([('b',2),('c', 3), ('d', 4)])
new_item = ('a',1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(orderd_dict)
print(new_ordered_dict)

"""52.  Write a Python program to check order of character in string using OrderedDict()."""
def check_order(string, reference):
    string = OrderedDict.fromkeys(string)
    reference =  OrderedDict.fromkeys(reference)
    return string == reference

strs = "Hello World"
ref = "Helo Wrld"
order = check_order(strs, ref)

if order:
    print("The order in the input string matches the reference")
else:
    print("The order in the input string does not match the reference")

"""53.  Write a Python program to sort Python Dictionaries by Key or Value."""
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")

"""54.  Write a Python program to convert Celsius to Fahrenheit."""
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
      
"""55.  Write a Python program to solve quadratic equation.
 The standard form of a quadratic equation is:
 2
 𝑥
 𝑎 +𝑏𝑥+𝑐=0
 where
 a, b and c are real numbers and
 𝑎 ≠ 0
 The solutions of this quadratic equation is given by:
 2
 𝑏
 (−𝑏 ± ( −4𝑎𝑐 )/(2𝑎)
 )1/"""

import math

a = 1
b = 4
c = 8
d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print(f"Root 1: {real} + {imag}i")
    print(f"Root 2: {real} - {imag}i")

""" 56.... 22 Write a Python Program to Find LCM.
 Least Common Multiple (LCM):
 LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
 more numbers.
 Formula:
 For two numbers a and b, the LCM can be found using the formula:
 LCM(𝑎,𝑏) = 
|𝑎⋅𝑏|
 GCD(𝑎,𝑏)
 For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
 numbers at a time until you reach the last pair.
 Note: GCD stands for Greatest Common Divisor"""
def compute_Lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
        while True:
            if greater % 4 == 0 and greater % 2 == 0:
                return greater
            greater +=1

num1 = 4
num = 6
print(compute_Lcm(num1,num))

"""57. Write a Python Program to Find HCF."""
def hcf(num1,num2):
    if num1> num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if num1%i == 0 and num2 % i == 0:
            hcf = i
    return hcf

num1 = 54
num2 = 24
print(hcf(num1,num2))

"""58.  26Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations."""
def add(x, y):
    return x+y
def sub(x,y):
    return x-y
def mull (x,y):
    return x*y
def divide(x,y):
   return x/y

print("Simple Calculator")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

while True:
    choice = input("Enter 1 to 5: ")

    if choice == '5':
        print("Exit the calculator")
        break
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {mull(num1, num2)}")
        elif choice == '4':
            if num2 == 0:
                print("Error , not divisible by zero")
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
            print("Invalid choice ! Please select valid output")

"""59. 29 Write a Python Program to calculate your Body Mass Index."""
def body_mass_index(weight, height):
    return round(weight/height*2, 2)

weight = 70
height = 1.8

bmi = body_mass_index(weight, height)

if bmi <= 18.5:
    print("You are under weight")
elif 18.5 < bmi <=24.9:
    print("You are over weight")
elif bmi >= 25 and bmi <= 29.9:
    print("You are obese weight")
else:
    print("You are under weight")

"""60. 30 Write a Python Program to calculate the natural logarithm of any number."""
import math
num = 15
if num <=0:
    print("Please enter a positive number")
else:
    print(math.log(num))

"""61 Write a Python Program for array rotation."""
def rotate_array(arr, d):
    n = len(arr)
    if d < 0 or d >= n:
        return "invalid rotation value"
    rotated_arr = [0]*n
    for i in range(n):
        rotated_arr[i] = arr[(i+d) % n]
    return rotated_arr

arr = [1, 2, 3, 4, 5]
d = 2
print(rotate_array(arr,d))

"""62 Write a Python Program to check if given array is Monotonic."""
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

arr1 = [1, 2, 2, 3]
arr2 = [3, 2, 1]
arr3 = [1, 3, 2, 4]

print(is_monotonic(arr1))
print(is_monotonic(arr2))
print(is_monotonic(arr3))

"""63  Write a Python Program to Add Two Matrices."""
def add_two_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
        result.append(row)
    return result

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]
matrix2 = [
    [6, 5, 4],
    [3, 2, 1]
 ]

result_matrix = add_two_matrices(matrix1, matrix2)
# if isinstance(result_matrix, str):
#     print(result_matrix)
# else:
print("Sum of matrices:")
for row in result_matrix:
 print(row)

"""64 An isogram is a word that has no duplicate letters. Create a function that takes a
 string and returns either True or False depending on whether or not it's an "isogram".
 Examples
 is_isogram("Algorism") 
➞ True
 is_isogram("PasSword") 
➞ False- Not case sensitive.
 is_isogram("Consecutive") 
➞ False
 Notes
 Ignore letter case (should not be case sensitive).
 All test cases contain valid one word strings."""

def is_isogram(words):

    unique_letters = set()
    for letter in words:
        if letter in unique_letters:
            return False
        unique_letters.add(letter)
    return True
word = "leTr"
print(is_isogram(word))

"""65  Create a function that takes a string and returns True or False, depending on whether
 the characters are in order or not.
 Examples
 is_in_order("abc") 
➞ True
 is_in_order("edabit") 
➞ False
 is_in_order("123") 
➞ True
 is_in_order("xyzz") 
➞ True"""
def is_in_order(words):
    return words == ''.join(sorted(words))

wor = "edabit"
print(is_in_order(wor))

"""66  Create a function that takes a number as an argument and returns True or False
 depending on whether the number is symmetrical or not. A number is symmetrical
 when it is the same as its reverse.
 Examples
 is_symmetrical(7227) 
➞ True
 is_symmetrical(12567) 
➞ False
 is_symmetrical(44444444) 
➞ True
 is_symmetrical(9939) 
➞ False
 is_symmetrical(1112111) 
➞ True"""
def is_symmetrical(n):
    return n == n[::-1]

sysmen = "12567"
print(is_symmetrical(sysmen))
"""67  Given a string of numbers separated by a comma and space, return the product of
 the numbers.
 Examples
 multiply_nums("2, 3") 
➞ 6
 multiply_nums("1, 2, 3, 4") 
➞ 24
 multiply_nums("54, 75, 453, 0") 
➞ 0
 multiply_nums("10, -2") 
➞ -2"""
def multiply_nums(num_str):
    res  = 1
    nums = [int(num) for num in num_str.split(",")]
    for i in nums:
        res *=i
    return res
print(multiply_nums("1, 2, 3, 4"))
"""68  Create a function that squares every digit of a number.
 Examples
 square_digits(9119) 
➞ 811181
 square_digits(2483) 
➞ 416649
 square_digits(3212) 
➞ 9414
 Notes
 The function receives an integer and must return an integer"""
def square_digits(num):
    num_str = str(num)
    res = ""
    for i in num_str:
        res += str(int(i) ** 2)
    return res
print(square_digits(9119))  # Output: 811181

"""69  Create a function that sorts a list and removes all duplicate items from it.
 Examples
 setify([1, 3, 3, 5, 5]) 
setify([4, 4, 4, 4]) 
➞ [1, 3, 5]
 ➞ [4]
 setify([5, 7, 8, 9, 10, 15]) 
➞ [5, 7, 8, 9, 10, 15]
 setify([3, 3, 3, 2, 1]) 
➞ [1, 2, 3"""
def setify(lst):
    sort_list = set(sorted(lst))
    return list(sort_list)
setsm = [1, 3, 3, 5, 5]
print(setify(setsm))
"""70 Create a function that returns the mean of all digits.
 Examples
 mean(42) 
➞ 3
 mean(12345) 
➞ 3
 mean(666) 
➞ 6
 The mean of all digits is the sum of digits / how many digits there are (e.g. mean
 of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
 The mean will always be an integer."""
def mean(n):
    n_str = str(n)
    digit_sum = sum(int(digit) for digit in n_str)
    length = len(n_str)
    digit_mean = digit_sum / length
    return int(digit_mean)
nm = 42
print(mean(nm))


"""71 Create a function that takes an integer and returns a list from 1 to the given number,
 where:
 1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
 number).
 2. If the number cannot be divided evenly by 4, simply return the number.
 Examples
 amplify(4) 
➞ [1, 2, 3, 40]
 amplify(3) 
➞ [1, 2, 3]
 amplify(25) 
➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21,
 22, 23, 240, 25]
 The given integer will always be equal to or greater than 1.
 Include the number (see example above).
 To perform this problem with its intended purpose, try doing it with list
 comprehensions. If that's too difficult, just solve the challenge any way you can."""
def amplify(num):
    return [n*10 if n % 4 == 0 else n for n in range(1, num+1)]
print(amplify(4))

"""72  Create a function that takes a list of numbers and return the number that's unique.
 Examples
 unique([3, 3, 3, 7, 3, 3]) 
➞ 7
 unique([0, 0, 0.77, 0, 0]) 
➞ 0.77
 unique([0, 1, 1, 1, 1, 1, 1, 1]) 
Notes
 ➞ 0
 Test cases will always have exactly one unique number while all others are the same"""
def unique(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] +=1
        else:
            count_dict[num] = 1
    for num, counts in  count_dict.items():
        if counts == 1:
           return num

print(unique([3, 3, 3, 7, 3, 3]))
"""73  Create a function that takes a list of strings and return a list, sorted from shortest to
 longest.
 Examples
 sort_by_length(["Google", "Apple", "Microsoft"]) 
➞ ["Apple", "Google", "Microsoft"]
 sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) 
➞ ["Raphael",
 "Leonardo", "Donatello", "Michelangelo"]
 sort_by_length(["Turing", "Einstein", "Jung"]) 
➞ ["Jung", "Turing", "Einstein"]"""
def sort_by_length(lst):
    return sorted(lst,key = len)
abc =["Leonardo", "Michelangelo", "Raphael", "Donatello"]
print(sort_by_length(abc))

"""74  Create a function that validates whether three given integers form a Pythagorean
 triplet. The sum of the squares of the two smallest integers must equal the square of
 the largest number to be validated.
 Examples
 is_triplet(3, 4, 5) 
3² + 4² = 25
 5² = 25
 ➞ True
 is_triplet(13, 5, 12) 
➞ True
 5² + 12² = 169
 13² = 169
 is_triplet(1, 2, 3) 
➞ False
 1² + 2² = 5
 3² = 9
 Notes
 Numbers may not be given in a sorted order"""
def is_triplet(a, b, c):
     sorts = sorted([a, b, c])
     return sorts[0]**2 + sorts[1]**2 == sorts[2]**2
print(is_triplet(3,4,5))


"""75  Create a function that takes three integer arguments (a, b, c) and returns the amount
 of integers which are of equal value.
 Examples
 equal(3, 4, 3) 
➞ 2
 equal(1, 1, 1) 
➞ 3
 equal(3, 4, 1) 
➞ 0
 Notes
 Your function must return 0, 2 or 3"""
def equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c  or b == c:
        return 2
    else:
        return 0

print(equal(3,2,3))

"""76  Write a function that converts a dictionary into a list of keys-values tuples.
 Examples
 dict_to_list({
 "D": 1,
 "B": 2
 "C": 3
 }) 
➞ [("B", 2), ("C", 3), ("D", 1)]
 dict_to_list({
 "likes": 2,
 "dislikes": 3,
 "followers": 10
 }) 
➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
 Notes
 Return the elements in the list in alphabetical order"""
def dict_to_list(d):
    sort_list = sorted(d.items())
    dictList = [(key,value) for key,value in sort_list]
    return dictList

dlist = {
 "likes": 2,
 "dislikes": 3,
 "followers": 10
 }
print(dict_to_list(dlist))

"""77  Write a function that creates a dictionary with each (key, value) pair being the (lower
 case, upper case) versions of a letter, respectively.
 Examples
 mapping(["p", "s"]) 
➞ { "p": "P", "s": "S" }
 mapping(["a", "b", "c"]) 
➞ { "a": "A", "b": "B", "c": "C" }
 mapping(["a", "v", "y", "z"]) 
➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
 Notes
 All of the letters in the input list will always be lowercase"""
def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
    return result

map_value = ["p", "s"]
print(mapping(map_value))

"""78 Write a function, that replaces all vowels in a string with a specified vowel.
 Examples
 vow_replace("apples and bananas", "u") 
vow_replace("cheese casserole", "o") 
➞ "upplus und bununus"
 ➞ "chooso cossorolo"
 vow_replace("stuffed jalapeno poppers", "e") 
➞ "steffed jelepene peppers"
 Notes
 All words will be lowercase. Y is not considered a vowel."""
def replace_vowels(string, vowel):
    vowels = "aeiou"
    result = ""
    for char in string:
        if char in vowels:
            result += vowel
        else:
            result += char
    return result

replae = "apples"
vowel = "u"
print(replace_vowels(replae, vowel))

"""79Create a function that takes a string as input and capitalizes a letter if its ASCII code
 is even and returns its lower case version if its ASCII code is odd.
 Examples
 ascii_capitalize("to be or not to be!") 
➞ "To Be oR NoT To Be!"
 ascii_capitalize("THE LITTLE MERMAID") 
➞ "THe LiTTLe meRmaiD"
 ascii_capitalize("Oh what a beautiful morning.") 
➞ "oH wHaT a BeauTiFuL
 moRNiNg."""
def ascii_capitalize(string):
    result = ""
    for char in string:
        if ord(char) % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result
asc_cap = "THE LITTLE MERMAID"
print(ascii_capitalize(asc_cap))

"""80 group of friends have decided to start a secret society. The name will be the first
 letter of each of their names, sorted in alphabetical order. Create a function that takes
 in a list of names and returns the name of the secret society.
 Examples
 society_name(["Adam", "Sarah", "Malcolm"]) 
➞ "AMS"
 society_name(["Harry", "Newt", "Luna", "Cho"]) 
➞ "CHLN"
 society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])"""
def society_name(names):
    return ''.join(sorted(name[0] for name in names))

soc_name = ["Adam", "Sarah", "Malcolm"]
print(society_name(soc_name))

"""81 Create a function that takes in two lists and returns True if the second list follows the
 first list by one element, and False otherwise. In other words, determine if the second
 list is the first list shifted to the right by 1.
 Examples
 simon_says([1, 2], [5, 1]) 
➞ True
 simon_says([1, 2], [5, 5]) 
➞ False
 simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) 
➞ True
 simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) 
➞ False
 Notes:- Both input lists will be of the same length, and will have a minimum length of 2.- The values of the 0-indexed element in the second list and the n-1th indexed
 element in the first list do not matter."""
def simon_says(list1, list2):
    return list1[:-1] == list2[1:]

print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))

"""82  Create a function that takes three parameters where:- x is the start of the range (inclusive).- y is the end of the range (inclusive).- n is the divisor to be checked against.
 Return an ordered list with numbers in the range that are divisible by the third
 parameter n.
 Return an empty list if there are no numbers that are divisible by n.
 Examples
 list_operation(1, 10, 3) 
➞ [3, 6, 9]
 list_operation(7, 9, 2) 
➞ [8]
 list_operation(15, 20, 7) 
➞ []"""
def list_operation(start, end, divisor):
    return [num for num in range(start,end+1) if num%divisor==0]
print(list_operation(1, 10, 3))

"""83 Write a function that takes a list of elements and returns only the integers.
 Examples
 return_only_integer([9, 2, "space", "car", "lion", 16]) 
➞ [9, 2, 16]
 return_only_integer(["hello", 81, "basketball", 123, "fox"]) 
➞ [81, 123]
 return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) 
➞ [10, 56, 20,3]
 return_only_integer(["String", True, 3.3, 1]) 
➞ [1]"""
def return_only_integer(list):
    numLis = []
    for num in list:
        if type(num) == int:
            numLis.append(num)
    return numLis
print(return_only_integer([9, 2, "space", "car", "lion", 16]))
"""84  Create a function that takes a string and returns a string with its letters in
 alphabetical order.
 Examples
 alphabet_soup("hello") 
➞ "ehllo"
 alphabet_soup("edabit") 
➞ "abdeit"
 alphabet_soup("hacker") 
➞ "acehkr"
 alphabet_soup("geek") 
➞ "eegk"
 alphabet_soup("javascript") 
➞ "aacijprstv"""
def alphabet_soup(string):
    return ''.join(sorted(string))
print(alphabet_soup("edabit"))

"""85  Create the function that takes a list of dictionaries and returns the sum of people's
 budgets.
 Examples
 get_budgets([
 { 'name': 'John', 'age': 21, 'budget': 23000 },
 { 'name': 'Steve', 'age': 32, 'budget': 40000 },
 { 'name': 'Martin', 'age': 16, 'budget': 2700 }
 ]) 
➞ 65700
 get_budgets([
 { 'name': 'John', 'age': 21, 'budget': 29000 },
 { 'name': 'Steve', 'age': 32, 'budget': 32000 },
 { 'name': 'Martin', 'age': 16, 'budget': 1600 }
 ]) 
➞ 6260"""
def get_budgets(people):
          total = sum(person['budget'] for person in people)
          return total


budgets1 = [
    {'name': 'John', 'age': 21, 'budget': 23000},
    {'name': 'Steve', 'age': 32, 'budget': 40000},
    {'name': 'Martin', 'age': 16, 'budget': 2700}]
print(get_budgets(budgets1))


"""86  Write a function that takes a list and a number as arguments. Add the number to the
 end of the list, then remove the first element of the list. The function should then
 return the updated list.
 Examples
 next_in_line([5, 6, 7, 8, 9], 1) 
➞ [6, 7, 8, 9, 1]
 next_in_line([7, 6, 3, 23, 17], 10) 
➞ [6, 3, 23, 17, 10]
 next_in_line([1, 10, 20, 42 ], 6) 
➞ [10, 20, 42, 6]
 next_in_line([], 6) 
➞ "No list has been selected"""
def next_in_line(list1, n):
    if list:
      list1.pop(0)
      list1.append(n)
      return list1
    else:
      return "no list has been selected"
print(next_in_line([5, 6, 7, 8, 9], 1))

"""87 Create a function that takes a list of numbers between 1 and 10 (excluding one
 number) and returns the missing number.
 Examples
 missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) 
➞ 5
 missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) 
➞ 10
 missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) 
➞ 7"""
def missing_num(nums):
    sum_range = sum(range(1, 11))
    sum_lst = sum(nums)
    return sum_range - sum_lst
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))

"""88  Create a function that takes a list of strings and integers, and filters out the list so
 that it returns a list of integers only.
 Examples
 filter_list([1, 2, 3, "a", "b", 4]) 
➞ [1, 2, 3, 4]
 filter_list(["A", 0, "Edabit", 1729, "Python", 1729]) 
➞ [0, 1729]
 filter_list(["Nothing", "here"]) 
➞ []"""
def filter_list(lst):
    return [filter for filter in lst if isinstance(filter, int)]
print(filter_list([1, 2, 3, "a", "b", 4]))
"""89  Using list comprehensions, create a function that finds all even numbers from 1 to
 the given number.
 Examples
 find_even_nums(8) 
➞ [2, 4, 6, 8]
 find_even_nums(4) 
➞ [2, 4]
 find_even_nums(2) 
➞ [2]"""
def find_even_nums(nums):
    return [even for even in range(1, nums+1) if even%2 == 0]
print(find_even_nums(10))

"""90  Create a function that takes a single string as argument and returns an ordered list
 containing the indices of all capital letters in the string.

 Examples
 index_of_caps("eDaBiT") 
➞ [1, 3, 5]
 index_of_caps("eQuINoX") 
➞ [1, 3, 4, 6]
 index_of_caps("determine") 
➞ []
 index_of_caps("STRIKE") 
➞ [0, 1, 2, 3, 4, 5]
 index_of_caps("sUn") 
➞ [1]"""

def index_of_caps(word):
    return [i for i , char in enumerate(word)  if char.isupper()]
print(index_of_caps("eDaBiT"))

"""91.Create a function that reverses a boolean value and returns the string "boolean
 expected" if another variable type is given.
 Examples
 reverse(True) 
➞ False
 reverse(False) 
➞ True
 reverse(0) 
➞ "boolean expected"
 reverse(None) 
➞ "boolean expected"""
def reverse(boolean):
    if isinstance(boolean, bool):
        return not boolean
    else:
        return "boolean expected"
print(reverse(True))

"""92.  Create a function that takes a string and returns a string in which each character is
 repeated once.
 Examples
 double_char("String") 
➞ "SSttrriinngg"
 double_char("Hello World!") 
➞ "HHeelllloo WWoorrlldd!!"
 double char("1234! ") 
➞ "11223344!! """
def repeatCharacter(input_str):
    temp = ""
    for i in input_str:
        temp += i*2
    return temp
print(repeatCharacter("sTRING"))

"""93
 Write a function that moves all elements of one type to the end of the list.
 Examples
 move_to_end([1, 3, 2, 4, 4, 1], 1) 
➞ [3, 2, 4, 4, 1, 1]
 Move all the 1s to the end of the array.
 move_to_end([7, 8, 9, 1, 2, 3, 4], 9) 
➞ [7, 8, 1, 2, 3, 4, 9]
 move_to_end(["a", "a", "a", "b"], "a") 
➞ ["b", "a", "a", "a"]"""
def move_to_end(lst, element):
    count = lst.count(element)
    list = [x for x in lst if x != element ]
    list.extend([element]*count)
    return list
print(move_to_end(["a", "a", "a", "b"], "a"))

"""94  Write a function that calculates the factorial of a number recursively.
 Examples
 factorial(5) 
➞ 120
 factorial(3) 
➞ 6
 factorial(1) 
➞ 1
 factorial(0) 
➞ """
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
fact = factorial(4)
print(fact)

"""95 You can assign variables from lists like this:
 lst = [1, 2, 3, 4, 5, 6]
 first = lst[0]
 middle = lst[1:-1]
 last = lst[-1]
 print(first) 
➞ outputs 1
 print(middle) 
➞ outputs [2, 3, 4, 5]
 print(last) 
➞ outputs 6
 With Python 3, you can assign variables from lists in a much more succinct way.
 Create variables first, middle and last from the given list using destructuring
 assignment (check the Resources tab for some examples), where:
 first 
➞ 1
 middle 
➞ [2, 3, 4, 5]
 last 
➞ 6
 Your task is to unpack the list writeyourcodehere into three variables, being
 fi t iddl d l t ith iddl b i
 thi
 i
 b t
 th fi t """

writeyourcodehere = [1,2,3,4,5,6]
first, *middle, last = writeyourcodehere
print(first, middle, last)

""" 96. The "Reverser" takes a string as input and returns that string in reverse order, with
 the opposite case.
 Examples
 reverse("Hello World") 
reverse("ReVeRsE") 
➞ "DLROw OLLEh"
 ➞ "eSrEvEr"
 reverse("Radar") 
➞ "RADAr"""
def reverse(int_str):
    return int_str[::-1].swapcase()
print(reverse("Hello World"))

"""97 Create a function that takes a list of non-negative integers and strings and return a
 new list without the strings.
 Examples
 filter_list([1, 2, "a", "b"]) 
➞ [1, 2]
 filter_list([1, "a", "b", 0, 15]) 
➞ [1, 0, 15]
 filter_list([1, 2, "aasf", "1", "123", 123]) 
In [82]:
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10
 11
 ➞ [1, 2, 123"""
def filter_list(lst):
    filter = [element for element in lst if  isinstance(element, int) and element >= 0]
    return filter
filter = filter_list([1, 2, "aasf", "1", "123", 123])
print(filter)

"""98  Hamming distance is the number of characters that differ between two strings.
 To illustrate:
 String1: "abcbba"
 String2: "abcbda"
 Hamming Distance: 1 - "b" vs. "d" is the only difference.
 Create a function that computes the hamming distance between two strings.
 Examples
 hamming_distance("abcde", "bcdef") 
➞ 5
 hamming_distance("abcde", "abcde") 
➞ 0
 hamming_distance("strong", "strung") 
➞ 1"""
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError( "Both strings must be the same length.")

    count = 0
    for i in range (len(str1)):
        if str1[i] !=  str2[i]:
            count += 1
    return count

s1 = "abcde"
s2 = "abcde"
print(hamming_distance(s1, s2))

"""99 Program 99
 Create a function that replaces all the vowels in a string with a specified character.
 Examples
 replace_vowels("the aardvark", "#") 
➞ "th# ##rdv#rk"
 replace_vowels("minnie mouse", "?") 
➞ "m?nn?? m??s?"
 replace_vowels("shakespeare", "*") 
➞ "shkspr*" """
def replace_vowels(string, char):
    vowels = "AEIOUaeiou"
    for vowel in string:
        if vowel in vowels:
            string = string.replace(vowel, char)
    return string

strw1 = "the aardvark"
print(replace_vowels(strw1, "#"))

"""100 Create a function that returns True if a given inequality expression is correct and
 False otherwise.
 Examples
 correct_signs("3 < 7 < 11") 
➞ True
 correct_signs("13 > 44 > 33 <1") 
➞ False
 correct_signs("1 < 2 < 6 < 9 > 3") 
➞ True"""
def inequality(expression):
    return eval(expression)

print(inequality("3 < 7 < 11"))

"""  Write a Python Program to Multiply Two Matrices."""
"""  Write a Python Program to Transpose a Matrix."""
"""  Write a Python program to check if the given number is a Disarium Number."""
"""  Write a Python program to print all disarium numbers between 1 to 100."""
"""  Write a Python program to check if the given number is Happy Number."""
"""  Write a Python program to print all happy numbers between 1 and 100."""
"""  Write a Python program to determine whether the given number is a Harshad Number."""
"""  Write a Python program to print all pronic numbers between 1 and 100."""
"""  Write a Python program to find words which are greater than given length k."""
