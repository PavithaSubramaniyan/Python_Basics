# Print every element in the list [10, 20, 30, 40].
lis = [10,20,30,40]
for li in lis:
    print(li)
# Print each character of the string "BANANA" on a separate line.
str = "BANANA"
for char in str:
    print(char)
# Print all odd numbers from 1 to 20 using a for loop and range().
for odd in range(1, 20):
    if odd%2 != 0: print(odd)

# Print the square of each number in [2, 4, 6, 8, 10].
nums = [2,4,6,8,10]
for square in nums:
    print(square**2)

# Print each key and value in the dictionary {"A": 1, "B": 2, "C": 3} using a for loop.

dict = {"A":1, "B":2, "C":3}
for key, value in dict.items(): print (key, ":", value)

# Write a for loop to count the number of even numbers in [11][12][13][14][15][16].
evenNumbers = [11,12,13,14,15,16]
count = 0
for evenNumber in evenNumbers:
    if evenNumber%2 == 0:
        count += 1
print(count)


# Print all items in the tuple (1, 3, 5, 7), one per line.
tup =  (1, 3, 5, 7)
for item in tup:
    print(item)

# Use a for loop to make a new list containing the cubes of numbers 1–5.
cubes = []
for i in range(1,6): cubes.append(i**3)
print(cubes)

# Print each item in the set {"red", "blue", "green"} (order may change).
setItem = {"red", "blue", "green"}
for setItems in setItem:
    print(setItems)

#Given words = ["one", "two", "three"], print each word reversed (e.g., eno, owt, eerht).
rever = ["one", "two", "three"]
for reverseStr in rever: print(reverseStr[::-1])
#========================whie loop=======================================

# Print numbers from 1 to 10 using a while loop.
i = 1
while i<=10:
    print(i)
    i +=1

# Print countdown from 10 to 1 using while.
n = 10
while n>=1:
    print(n)
    n -= 1


# Keep asking user for a number until they type 0. (Use input())
# user_input = int(input("Enter number (0 to stop): "))
# while user_input != 0:
#     user_input = int(input("Enter number (0 to stop): "))

# Print even numbers 2 to 20 using while loop.
n = 2
while n <= 20:
    if n%2 ==0: print(n)
    n += 1
# Print characters in the word "PYTHON" using a while loop (one at a time).
str = "PYTHON"
while i <= len(str):
    print(str[i])
    i += 1
# Count and print the number of vowels in "HELLO WORLD" using while loop.
# strchar = "HELLO WORLD"
# VOWELS = ["a", "e", "i", "o", "u"]
# while i <= len(strchar):
#     if strchar[i].contains('a', '``e', 'i', 'o', 'u'): print(strchar[i])
# Print the multiplication table of 5 (from 5×1 to 5×10) using while.
n = 1
while n>=10:
    print(n*5)
    n  += 1
# Sum numbers from 1 to 50 using while loop.
n = 1
total = 0
while n <=50:
    total += 1
    n +=1
    print(total)

# Print numbers from 100 down to 90 using while loop.
n = 100
while n>=90:
    print(n)
    n -=1
# Ask the user for numbers; stop if they type a negative number.
num = int(input("Enter a number (negative to stop): "))
while num >= 0:
    num = int(input("Enter a number (negative to stop): "))


# Range — 10 Questions
# Use range() to print numbers 0 to 9.
for  i in range(0,10): print(i)
# Create a list of numbers from 5 to 15 using range() and print it.
print(list(range(5,16)))
# Print every even number from 2 to 20 (use appropriate range() step).
for  i in range(2, 21):
    if i % 2 == 0:print(i)
# Use range() to go backwards and print numbers 10 to 1.
for i in range(10, 0, -1):
    print(i)
# Print all multiples of 3 from 3 to 30 using range().
for i in range(3 , 31,3):
    print(i)
# Print numbers from 50 to 60 using range().
for i in range(50, 61):
    print(i)
# Print every third number from 2 to 20 using range().
for i in range(2, 21,3):
    print(i)
# Use a for loop and range() to create a list of squares for numbers 1–10.
square  = []
for i in range(1, 11):
    square.append(i**2)
    print(square)
# Print numbers that start from 5 and end at 20, stepping by 2 each time.
for i in range(5, 21,2):
    print(i)
# Use range() and a loop to print only two-digit numbers (from 10 to 99).
for i in range(10, 100):
    print(i)

# Recursion — 10 Questions
# Write a recursive function to calculate factorial of a number.

# Write a recursive function to compute sum of numbers from 1 to n.
#
# Write a recursive function to print every character in a string one by one.
#
# Write a recursive function to find the nth Fibonacci number.
#
# Use recursion to reverse a string.
#
# Write a recursive function to print a list backwards.
#
# Write a recursive function to find the maximum in a list.
#
# Check if a number is a palindrome using recursion.
#
# Use recursion to print all numbers from n down to 1.
#
# Use recursion to find the sum of all digits in a number.

# 1. Write a function greet() that prints "Hello, World!"
def greet():
    print("Hello World")
greet()
# 2. Write a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    return a+b
# 3. Write a function is_even(n) that returns True if a number is even, else False.
def is_even(n):
    if n % 2 == 0:
        return True
    return False
# 4. Write a function max_of_three(a, b, c) that returns the largest of three numbers.
def max_of_three(a, b , c): return max(a,b,c)
# 5. Write a function reverse_string(s) that returns the reversed string.
def reverse_string(s):
    return s[::-1]

# 6. Write a function count_vowels(text) that returns the number of vowels (a, e, i, o, u) in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count +=1
    return count


# 7.Write a function count_digits(text) that returns the number of digits (0–9) in a string.
def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count
# 8. Write a function is_palindrome(s) that returns True if the string is a palindrome, else False.
def is_palindrome(s):
    return s == s[::-1]
# 9. Write a function sum_list(nums) that returns the sum of all elements in a list.
def sum_list(nums):
    return sum(nums)
# 10. Write a function get_even_numbers(nums) that takes a list and returns a new list with only the even numbers.
def get_even_numbers(nums):
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    return even


# Print "Done" five times.
strf = "Done"
for str in range(5):
    print(strf)
#Print numbers from 1 to 10, but only the odd ones.
for i in range(1, 11, 2):
    print(i)
#Make a new list that stores the squares of numbers 1–5.
empty = []
for emp in range(1, 6):
    empty.append(emp**2)
print(empty)

# Count up by tens starting from 10 until you reach 50 using while.
n= 50
while n>10:
    print(n)
n += 10

# Print "Hello" three times using while.
# str = "Helo"
# while strs >len(str):