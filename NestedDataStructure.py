""""""
"""Task1:
Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]


5
56
222
50000
put
5555
7777
666
89
on
333
3333"""
Li1 = [2,3,4,5,
       [45,56,67,78,[111,222,333, [5555,3333, [10000,50000,"python","computer"],
                                   1111,7777,8888],
                     444,555,666,777],
        89,23,34]]
print(Li1[3])
print(Li1[4][1])
print(Li1[4][4][1])
print(Li1[4][4][3][2][1])
print(Li1[4][4][3][2][3][3:-2])
print(Li1[4][4][3][0])
print(Li1[4][4][3][4])
print(Li1[4][4][6])
print(Li1[4][5])
print(Li1[4][4][3][2][2][-2:])
print(Li1[4][4][2])
print(Li1[4][4][3][1])

"""Task2
a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]

Extract
#science
#computer"""
a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
print(a[4][3][-7:])
print(a[4][3][:8])
"""Task3
a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]

Extract
#666
#201
#102
#999
#777"""
a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
print(a[4][4])
print(a[4][3][0])
print(a[4][3][2][0])
print(a[4][1])
print(a[4][5])

"""Task4:

Li1 = [2,3,"python","hello",4,5,0]  

Extract
#ll
#thon"""

Li1 = [2,3,"python","hello",4,5,0]
print("hdedfe",Li1[3][2:4])
print("hdedfe",Li1[2][2:])

"""Task5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

Output Prediction 

print(Li1[5][0])
print(Li1[5][6])
print(Li1[5][-2])
print(Li1[5][7])
print(Li1[6])
print(Li1[5][5][1])

print(Li1[-2][-1])


print(Li1[-2][2:4])"""
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]
print(Li1[5][0]) #11
print(Li1[5][6]) #6666
print(Li1[5][-2]) #6666
print(Li1[5][7]) #7777
print(Li1[6]) #7777
print(Li1[5][5][1]) #111
print(Li1[-2][-1]) #7777
print(Li1[-2][2:4]) #33, 44

"""Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}
#py
#ello
#en
#zoo
#Bot
print(a)"""
a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}
print(a[1][3][:2])
print(a[2][10][1:])
print(a[2][40][3:5])
print(a[40][1][:3])
print(a[40][2][:3])
"""Task7:

Covert below two lists in to a dictionary

[1,2,3,4,5]
["python","cpp","c","java","php"]"""
a=[1,2,3,4,5]
b= ["python","cpp","c","java","php"]
listToDict = dict(zip(a,b))
print(listToDict)
print(type(listToDict))

"""Task8:

Convert below set in to a list

{5,4,3,6,2,7,1}"""

setToList = {5,4,3,6,2,7,1}
print(list(setToList))


"""Task9:

Remove duplicates from below list

[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]"""
list1 = [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
list1 = set(list1)
print(list1)

"""Task10:

Convert below one to tuple

[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]"""
li1 = [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
li1 = tuple(li1)
print(li1)