# stre = "161 182 161 154 176 170 167 171 170 174"
#
# '''
# first = stre.split()
# temp = []
#
# for i in first:
#     temp.append(int(i))
#
#
# map(operation, DS)
# '''
# print(list(map(int, stre.split())))
# Li = [3,4,5,2,0,1,8,6]

#Sort the above list without using inbuilt function
#Find minimum number in the list


# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
#
# plt.plot(x, y)
# plt.title('Line Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#


# import seaborn as sns
# import matplotlib.pyplot as plt
#
# data = {'apples': 10, 'bananas': 25, 'grapes': 17}
# names = list(data.keys())
# values = list(data.values())
#
# sns.barplot(x=names, y=values)
# plt.title('Fruit Sales')
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns
#
# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(nums)
# plt.title('Matplotlib Histogram')
# plt.show()
#
# sns.histplot(nums, kde=True)
# plt.title('Seaborn Histogram')
# plt.show()
# base = 2
# exp = 5
# result = 1
# for i in range(exp):
#     result *= base
# print(result)

num = 1000
n= []
for i in range(1, num+1):
    temp = i
    total = 0
    digits = len(str(i))
    while temp >0:
         digit = temp%10
         total += digit**digits
         temp //= 10
    if i == total and i>9:
          n.append(i)
print(n)

num = 5
for i in range(num+1):
    for j in range(1,i+1):
        print("*", end ="")
    print()

for i in range(1, num+1):
    spaces = num - i
    star = 2*i - 1
    print(" "*spaces+"*"*star)
#Check if a number is strong (sum of factorial of digits = number)

num = 145
digi = 0
while num > 0:
    digi += num%10
    fact = 1
    for i in range(1,digi+1):
        fact *= i
        digi +=fact
        num //= 10
if digi == temp:
    print("Strong number")

def natural(num):
   if num == 0:
       return 0
   else:
       return num + natural(num-1)
a = 30
print(natural(a))

a = "I love pyhon"
b = a.split()
rev = " "

for i in b:
    rev = i+" "+rev
print(rev)

a = 28
sums =0
for i in range(1, a):
  if a%i == 0:
     sums += i
if sums == a:
  print("It is perfect")
else:
  print("It is not perfect")

import re

a = "a12b3"
b= re.findall('\d', a)
total =0
for i in b:
    total +=int(i)
print(total)

st = "paviparthipan"
sp = list(st)
print(sp)
dicts = {}
nonrep = ""
for i in sp:
    if i  in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1

for v,k in dicts.items():
    print(v,k)
    if k == 1:
        nonrep += v
        print("value",v)
print("alllvalue",nonrep)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a = int(input())
b = int(input())
c = (input())
operations = ['+','-','*','/']
if c == '+':
    print(add(a,b))
elif c == '-':
    print(sub(a,b))
elif c == '*':
    print(mul(a,b))
elif c == '/':
    print(div(a,b))