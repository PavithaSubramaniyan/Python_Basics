"""1. ABCDE ... String rotation Program
EABCD
DEABC
CDEAB
BCDEA
ABCDE"""

rotation = "ABCDE"
for i in range(5):
    rotation = rotation[-1]+rotation[:-1]
    print(rotation)


"""2.Pattern Program:
If supplied Input: 5 Needs to print Below like this
a
aB
aBc
aBcD
aBcDe"""

asciKey = 65
charpatter = " "
for i in range(5) :
    if i%2 == 0:
        charpatter += chr(asciKey).lower()
    else:
        charpatter += chr(asciKey)
    print(charpatter)
    asciKey += 1

""" 3.  Sort string characters in descending order. Program:
 Input: str = “for”
 Output: “rof”"""
value = "for"

print(sorted(value))
"""4.  Merge two strings
 Input:
 S1 = “Hello” S2 = “Bye”
 Output: HBeylelo"""
s1 = "Hello"
s2 = "Bye"
temp =""
result = ""
res = ""
for i in range(len(s1)):
    temp  += s1[i]
    print("temp",temp)
    for j in range(len(s2)):
        result += s2[j]
        print("result",result)
    res = temp + result
    print("res", res)
print(res)


"""5.  Extract maximum and minimum number
 Example 1:
 Input:
 S =100klh564abc365bg
 Output:
 Maximum: 564
 Minimum: 100"""

S = "100klh564abc365bg"
num_list = []
temp = ""

for char in S:
    if char.isdigit():
        temp += char

    else:
        if temp != "":
            num_list.append(int(temp))
            temp = ""
max_num = max(num_list)
min_num = min(num_list)
print(f"max: {max_num}, min: {min_num}")

