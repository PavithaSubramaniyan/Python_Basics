import os
import re
from functools import reduce

#How do you open a file for reading? Write the code.
f = open("Projects/geeks.txt")
print(f.read())

#Write code to read all lines from a file and print them one by one.
with open("Projects/geeks.txt", "r") as f:
    for line in f:
        print(line.strip())


#How do you write “Hello World” to a new file?
with open ("Projects/geeks.txt", "w") as f:

    f.write("\nHello World")
#What does the .close() method do? Why is it important?
#Write a program that appends a new line to an existing file.

with open ("Projects/geeks.txt", "a") as f:
    f.write("\n")
    f.write("Hello")

#How do you check if a file exists before opening it using Python?
#f =open ("geekgs.txt", "x")

#What’s the difference between "w" and "a" modes in file opening?

# w overwrite
# a  to write

#Show how to use the with statement for file handling.
with open("Projects/geeks.txt") as f:

    print(f.read())
#How can you move the file pointer to the start of a file after reading some lines?
# f.seek(0)

import os
# os.remove("demo.txt")

# import os
# os.rename("demo.txt", "newname.txt")
# import shutil
# shutil.copy("demo.txt", "copy.txt")
f = open("Projects/geeks.txt", "w")
f.truncate(5)
f.close()


# 2. OS Module Questions (15 operations)
# How do you get the current working directory using os module?
print(os.getcwd())
# Write code to list all files and folders in your current directory.
#print(os.listdir())
# What is the command to create a new folder using os?
#             print(os.mkdir("geeks.txt"))
# How can you remove an empty folder using os?
#               print(os.rmdir("geeks.txt"))
# How do you change the working directory to another folder?
#                  print(os.chdir("se.txt"))
# Show how to check if a file exists using os.path.
#            print(os.path.exists("geeks.txt"))
# Write code to join directory and filename into a valid path.
#             print(os.path.join("makf","geek.txt"))
# Write code to remove a file named test.txt.
#                print(os.remove("test.txt"))
# How do you rename a file from file1.txt to file2.txt?
#               print(os.rename("test.txt", "dxm.txt"))
# Use os.walk() to print all files in a directory tree.
#
# How can you get an environment variable using os?
#                print(os.getenv("HOME"))
# Write code to set a new environment variable.
#
# What does os.stat() return for a file?
#
# How do you execute the system command “ls” or “dir” using Python?
#
# Write code to get the absolute path of a file named demo.txt.
#
words = ["hello", "world"]
print(list(map(str.lower, words)))
nums = [5, -4, 9, -2, 0]
print(list(filter(lambda x: x<0, nums)))

sq = [x**2 for x in nums]
eve = [x for x in range(1, 10) if x%2==0]
cub = {x**3  for x in [1,2,3]}
dictf = {x:x*2 for x in {1,2,3}}
tup = tuple(x**2 for x in [1,2,3])
lam = lambda x,y: x*2
ma = list(map(lambda x:x**2, [1,2,3]))
ggil = list(filter(lambda x:x>5, [9,89,8]))
msi = lambda x,y: x*y

res= reduce(lambda x, y: x*y , [1,2,3])
words = ["hello", "world"]
print(list(map(str.upper, words)))
nums = [1,2,3,4,5,6,7,8,9]
even = filter(lambda x:x%2==0, nums)
square = map(lambda x: x**2, nums)
print(list(square))
act = "abcf"
check = "aby"
fin = re.findall(r'abc','abcdef')
print(fin)
text = "Hello 89 worl00d 90mn sag abcg"
match = re.match(r"Hello", text)
print(bool(match))        # Output: True
mat = re.findall(r"\b\w{5}\b", text)
print(mat)
mas = re.findall(r'\d+',text)
print(mas)
ch = re.findall(r'\ba\w+',text)
print(ch)
num = "770845890 9909890890"
result = bool(re.match(r'^[789]\d{9}$', num))

print(result)  # True
text = "My birthday date: 27/10/2025, meeting: 01/11/2025"
dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
print(dates)

SPAC = re.sub(r' ', '-', text)
print(SPAC)
email = "user@example.com"
