#add two numbers
import math
from functools import reduce
from operator import mul

a = 10
b= 90
c= a+b
print(c)

#minimum of two numbers
a= 7
b= 10
c= a if a <b else b
print(c)

#maximum of two numbers
a=90
b =89
num = [a,b]
num.sort()
print(num[-1])

#factorial number
n= 4
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

def fact(n):
   if n == 0:
       return 1
   else:
       return n* fact(n-1)

print(fact(5))

#simple interest
def fun(p, t, r):
    return (p*r*t)/100
p,r,t = 8,6,8
print(fun(p, t, r))

# Compound Interest
P = 1200
R = 5.4
T = 2

A = P * (1 + R/100) ** T
CI = A - P

print("Compound interest:", CI)

#Armstrong number
def armstrong(n):
    total = 0
    power = len(str(n))

    while n > 0:
        digit = n%10
        total += digit**power
        n= n//10
    if total == num:
        return "Armstrong number"
    else:
        return "Not Armstrong number"
num = 153
print(armstrong(num))

num = 153
power = len(str(num))

def armstrong_sum(n):
    if n == 0:
        return 0
    return (n % 10) ** power + armstrong_sum(n // 10)

if armstrong_sum(num) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

def recur_armstrong(nu):
    power = len(str(nu))
    if nu == 0:
        return 0
    return (nu%10) ** power + recur_armstrong(nu//10)

nou  = 153
if recur_armstrong(num) == num:
    print("Recur armstrong number")
else:
    print("Not Recur armstrong number")
print(recur_armstrong(nou))

for num in range(2, 10 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
#wheather number is prime or not
n= 17
for i in range(2,n):
    if n%i==0:
        print("Non prime number")
else:
    print("prime number")

#nth fibonaci series
n  =5
fib = [0,1]
while n>0:
    fib.append(fib[-1]+fib[-2])
    n -=1
print(fib)

def fib (n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

ns= 5
for i in range(ns+1):
    print(fib(i))

#if a Given Number is Fibonacci number 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
fibNum = 34
fibli = [0,1]
flag = False
for im in range(fibNum):
    fibli.append(fibli[-1]+fibli[-2])
for i in fibli:
    if i == fibNum:
        print("Fibonacci number")
        break
else:
    print("Not Fibonacci number")


#Nth multiple of a number in Fibonacci Series in Python
def multiplefib(nj,mu):
    count = 0
    lis = [0,1]
    lm = []
    while True:
        lis.append(lis[-1]+lis[-2])
        if  lis[-1]%mu == 0:
            print("lis",lis[-1])
            count += 1
            lm.append(lis[-1])
            if count == nj:
                return lm[-1]

n,m =4,3
print(multiplefib(n,m))

def fun(n, m):
    fib = [0, 1]
    count = 0
    while True:
        fib.append(fib[-1] + fib[-2])
        if fib[-1] % m == 0:
            count += 1
            if count == n:
                return fib[-1]

n, m = 4, 3
print(fun(n, m))

# print asci key for character
io = "z"
print(ord(io))

# sum of square of natural number
n = 10
res = sum(i*i for i in range(1, n+1))
print("li",res)

#lambda
n= 10
res = reduce(lambda x, y : x+y*y ,range(1, n+1) )
print("lambda",res)
#for
nis= 10
resf=0
for i in range(1, nis+1):
    resf += i*i
    print("for",resf)

#cube of first 3 numbers
n= 10
resi = sum(i**3 for i in range(1, n+1))
print("lambda",resi)

#sum of array
arr = [1,9,8,4,5,6,7,2,3]
res=0
for i in arr:
    res += i
print("store",res)

res = sum([x for x in arr])
print("li",res)

res = reduce(lambda x,y : x+y, arr)
print("lambda",res)

#largest element in a array
arr.sort(reverse = True)
larg = arr[0]
print("lambda",larg)
print("max", max(arr))

rs = arr[0]
for i in range(1, len(arr)):
    if arr[i] > rs:
        rs  = arr[i]
print("llop",rs)

#array rotation

def arr_rotation(arr , d):
    arr[:] = arr[d:]+arr[:d]
    return arr

print(arr_rotation(arr, 2))
# array rotaion using reverse algorithm
def rev(arr,d):
    c = arr[d:]+ arr[:d]
    return c
print(rev(arr,2))

# Python program to split array and move first
# part to end.

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
    print(i)

arr = [100, 10, 5, 25, 35, 14]
product = 1
n=11
for i in arr:
    product *= i
mod = product%n
print("Product",mod)

#swap two elements in a list
lim = [9,7,8]
lim[0], lim[2] = lim[2], lim[0]
print(lim)

temp = lim[0]
lim[0] = lim[2]
lim[2] = temp
print(lim)

#2 ways to find length of list
res = len(lim)
print(res)

c= 0
for i in lim:
    c +=1
print(c)

#3Check if element exists in list in Python
ch = 8
if ch in lim:
    print("It is exist")
else:
        print("It is not exist")
    # if i in ch:
    #     print("It is exists")
    # else:
    #     print("Not exists")
#4Different ways to clear list
lim.clear()
print(lim)
#5 reversing list
lim = [1,3,4,5,6,7]
print(lim[::-1])
lim.reverse()
list(reversed(lim))
print(lim)

#6find sum of elements in list
print(sum(lim))
res=0
for i in lim:
    res += i
print(res)
print(sum([x for x in lim]))
print(reduce(lambda x,y : x+y , lim))
#7 multiply all number in list
print(math.prod(lim))
print(reduce(mul, lim))

#8 smallest num in list
lim.sort()
print(lim[0])

tep =lim[0]
for i in lim:
    if i<tep:
        tep = i
print(tep)

#9 largest num in list
print(max(lim))
temp =lim[0]
for i in lim:
    if i > temp:
        temp = i
print(temp)

#10 second largest
lim.sort()
print(lim)

print(lim[-2])

#11 n largest elemeny from a list

ljf= [2,4,6,7,4,8]
n = 3
ljf.sort(reverse = True)
print(ljf)
if len(ljf) >=  n:
    print(ljf[:3])

lis = []

# Python program to find N largest
# element from given list of integers

# Function returns N largest elements


list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n= 4
final_list=[]
max1 = 0
for i in list1:
    if i > max1:
        max1 = i
list1.remove(max1)
final_list.append(max1)
print(final_list)


def average(array):
    return sum(set(array)) / len(array)

if __name__ == '__main__':

    arr = [154,161,167,170,174,176,182]
    result = average(arr)#169.14285714285714
    print(result)
#Even numbers in a list
for i in arr:
    if i%2 == 0:
        print(i)
#odd numbers in a list
def odd(arr):
    for i in arr:
        if i%2 != 0:
          return i
arr = [1,4,3,7,13]
result = odd(arr)
print(result)
for i in arr:
    if i%2 != 0:
        print(i, end=" ")
r = [i for i in arr if i%2 !=0]
print(r)
rm = list(filter(lambda x: x%2==0,arr))
print(rm)

#print all even numbers in a range
for i in range(1, 20):
    if i % 2 == 0:
        print(i, end = " ")
#print all odd numbers in a range
ofdfil = list(filter(lambda x: x%2 != 0, range(1, 20)))
print(ofdfil)

#print positive numbers in a list
li = [-10, 15, 0, 20, -5, 30, -2]
for i in li:
    if i >=0 :
        print(i, end = " ")
x = [i for i in li if i >= 0]
fi = list(filter(lambda x : x>0, li))
print(fi)

#print all negative numbers
a = [5, -3, 7, -1, 2, -9, 4]
lifil = list(filter(lambda x: x<0, a))
print(lifil)

#print all positive numbers in a range

liscom = [x for x in range(-9, 9)  if x>0]
print(liscom)

#print all negative numbers in a range
fil = list(filter(lambda x : x<0, range(-9, 9)))
print(fil)

#reemove multiple elements from a list
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 30, 40]
res = []
for i in a:
    if i  in remove:
        a.remove(i)
print( a)
a = [10, 20, 30, 40, 50, 60, 70]
remove = [10, 60, 70]
l = [i for i in a if i not in remove ]
print(l)

#Remove empty Lists from List - Python

a = [[1, 2], [], [3, 4], [], [5]]
res = []
for i in a:
    if i:
        res.append(i)
print(res)

#cloning or copying a list
li =[1, 2, 3, 4, 5]
li1 = li.copy()
print(li)
print(li1)

lm = [1,2,3,4,5]
lm1 = lm
print(lm)
print(lm1)

#count occurences of an list
lrf =  [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

nk = 0
for i in lrf:
    if i ==3:
        nk += 1
print(nk)

#remove empty tuples from list
a = [(1, 2), (), (3, 4), (), (5,)]
emtup = [x for x in a if x]
print(emtup)

#print duplicates from a list of integer
a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
s = set()
rs =[]
for i in a:
    if i  in s:
        rs.append(i)
    else:
        s.add(i)
print(rs)

#Python program to find Cumulative sum of a list
l = [1, 2, 3, 4]

li = []
total =0
for i in l:
    total += i
    li.append(total)
print(li)

#Sum of number digits in List in Python
a = [123, 456, 789]
res = []
for i in a:
    total = 0
    while i>0:
        total += i%10
        i //= 10
    res.append(total)
print(res)

#Break a List into Chunks of Size N in Python
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
res = []
for i in range(0, len(a), n):  # Slice list in steps of n
    print(a[i])
    print("get",a[i:i])
    print("rx",a[i:i+n])
    res.append(a[i:i + n])

print(res)


#palindrome
s = "malayalam" # string
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#check whether the string is symmetrical or palindrome
a = "abaaba"

half = len(a)//2
print(half)
symmetric = a[:half] == a[half:] if len(a) % 2 == 0 else a[:half]+a[half+1:]
palindrome = a==a[::-1]
print ("Symmetrical" if symmetric else "Palindrome")
print("Palindrome" if palindrome else "Not Palindrome")

#reverse words in given string
s= "Python is fun "
res = " ".join(s.split()[::-1])
print(res)

#remove letters from a string in python
st= "Hello"
remove ="l"
smp = st.replace('l',"")
print(smp)

#way to remove ith character from a string
sete = "Pavitha"
ref = sete.replace('a',"")
print(ref)

import re
ref = re.sub("v", "",sete)
print(ref)

#check if string contains substring in python
string = "geeks for geeks"
substring = "geeks"
listString = string.split()
print(listString)
for i in listString:
    if i in substring:
        print(i +"yes")
    else:
        print(i +"no")
s = "hello world hello everyone"
char_count = {}
for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1
print(char_count)
s = "hello world hello everyone"
res ={}
for word in s.split():
    res[word] = res.get(word,0)+1
print(res)
from collections import Counter
res = Counter(s.split())
print(res)
# Output: {'hello': 2, 'world': 1, 'everyone': 1}
snake = 'geeksforgeeks_is_best'
res = snake.replace("_"," ").title().replace(" ","")
print(res)
s = 'geeksforgeeks_is_best'
res = s.replace("_", "").title()
print(res)
smp = "geeksforgeeks_is_bedt"
ress = "".join(i.capitalize() for i in s.split('_'))
print(ress)

#count
a = "dfgfggg"
print(len(a))
count =0
l = 0
for i in a:
    count +=  1

print(count)

for k , v in enumerate(a):
    l += 1
print(l)

s= a.count("")-1
print(s)
#Python program to print even length words in a string
s = "This is a python language"

wor = [i for i in s.split() if len(i)%2==0]
res =" ".join(wor)
print(res)

spn = "Geeksforgeeks"
v = 'e'

if all(i in spn for i in v):
    print("True")
else:
    print("False")

#Count the Number of matching characters in a pair of string
s1 = "VISHAKSHI"
s2 = "VANSHIKA"

res = len(set(s1).intersection(set(s2)))
print(res)
#remove all duplicates
s = "geeksforgeeks"
seen = set()
res = " "
for i in s:
    if i not in seen:
        seen.add(i)
        res += i
print(res)

#least frequent character in string
from collections import Counter
s = "GeeksforGeeks"
lc = Counter(s)
res = min(lc, key = lc.get)
print(res)

from collections import Counter
shj = "Geeksgotgeeks"
freq = Counter(shj)
resik = max(freq, key = freq.get)
print(resik)

#string contain special character
import string

def check_string(s):
    for c in s:
        if c in string.punctuation:
            print("String is not accepted")
            return
    print("String is accepted")

# Example usage
check_string("Geeks$For$Geeks")  # Output: String is not accepted
check_string("Geeks For Geeks")  # Output: String is accepted

#find words greater than given length k
strin = "hello geeks for geeks is ccomputer science portal"
k = 4
res = []
for i in strin.split():
    if len(i)>k:
        res.append(i)
print(res)

#remove ith character from a string
ks = 10
op = strin[:ks]+strin[ks+1:]
print(op)

#split and join string
b = strin.split()
c = "_".join(b)
print(c)
#given string binary or not
import re
s = "101010000111"
if re.fullmatch('[01]+',s):
    print("True")
else:
    print("False")

if all( i in '01' for i in s):
    print("yes")
else:
    print("no")

#unccommon words
a = "i got pen"
b = "i got pencil"

count = Counter(a.split())+Counter(b.split())

res = [word for word in count if count[word] ==1 ]
print(res)
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"

set1 = set(s1.split())
set2 = set(s2.split())
uncmmon = set1.symmetric_difference(set2)
print(uncmmon)

#replace duplicate occurrence in string
test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better .'
repl_dict  = {'Gfg':'It', 'Classes':'They'}

words = test_str.split(' ')
seen = set()

for i , k in enumerate(words):
    if k in repl_dict:
        if k in seen:
            words[i] = repl_dict[k]
        else:
            seen.add(k)
result = ' '.join(words)
print(result)

#replace multiple words with k
s = 'Geeksforgeeks is best for geeks and CS'
li = ["best", "CS", "for"]
k ="gfg"
res = ' '.join([k if  i in li else i for i in s.split()])
print(res)

#permutation of a given string

import itertools
s = "GFG"
res = ["".join(p) for p in itertools.permutations(s)]
print(res)

#check url in a string
s = 'My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/'
pattern = "https?://\S+|www\.\S+"
print(re.findall(pattern, s))

#execute a string code in python
code = "5+10"
res = eval(code)
print(res)

#Using Slicing
s = "GeeksForGeeks"
d = 2
left = s[d:]+s[:d+1]
right = s[-d:]+s[:-d]
print(left)
print(right)

#find all duplicate characters in string in python
c= "Geeks"
print(set(c))
from collections import Counter

s = "GeeksforGeeks"
d = Counter(s)
print(d)

res =[ c for c , cnt in d.items() if cnt>1]
print(res)
#replace all occurence of string
a = "Python hjava html pythonn"
res = a.replace("Python", "++")

#find the size of  a tuple
a = (1,2,3,4)
print(len(a))

#Maximum and Minimum K elements in Tuple
import heapq
s = (2,4,5,6,7)
k= 2
smallest = heapq.nsmallest(k, s)
largest = heapq.nlargest(k,s)
print(smallest)
print(largest)

sort = sorted(s)
print(sort)
mini = sort[:k]
maxs = sort[-k:]
print(mini)
print(maxs)

#using for loop with append()
a = [1,2,3,4,5]
b=[]
for i in a:
    b.append((i, i**3))
print(res)

liicom = [(cu, cu**3) for cu in a]
print(liicom)

lammap = list(map(lambda x: (x,x**3) ,a))
print(lammap)

a = [1,2,3]
b = (4,5)
c = [6,7,8]
a.append(b)
print(a)

d = (*b, *c)
print(d)

#Extract unique values dictionary

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

print("Original: "+str(test_dict))
nums = set()
for val in test_dict.values():
    print("Value",val)
    for i in val:
        nums.add(i)
print(list(sorted(nums)))

#sum of all ittems in dictonary
d = {'a': 100, 'b': 200, 'c': 300}
res = sum(d.values())
print(res)

#remove a key from dictonary
a = {"name": "Nikki", "age": 25, "city": "New York"}
rv = a.pop("city")
print(a)
print(rv)
del a["age"]
print(a)

#ways to sort list of dictionaries by values using itemgetter
from operator import itemgetter
data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]

print(sorted(data_list, key = itemgetter("age")))

#using lambda function
print(sorted(data_list, key = lambda x:x["age"]))

#merging two dictionaries
data_list = {"name": "Nandini", "age": 20}

data_lisr1 = {"name": "Nikhil", "age": 19}
data = data_list | data_lisr1
print(data)
#convert key_values list to flat dictionary
a = [("name", "Emma"), ("age", 25), ("city", "New York")]
print(dict(a))

#insertion at the beginning in ordereddict
from collections import OrderedDict
original_dict = OrderedDict([("name", "Emma"), ("age", 25)])
item_to_be_inserted = ('c', 3)

original_dict.update({item_to_be_inserted})
original_dict.move_to_end('c', last = False)
print(original_dict)

#check order of character in string using OrderedDict()
