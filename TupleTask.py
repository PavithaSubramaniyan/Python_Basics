from operator import index

#Create two tuples
tup1 = (1,4,5,6,7,8)
tup2=  (5,6,7,8,9)

#Find the common elements between two tuples
result =set(tup1).intersection(set(tup2))
print(tuple(result))

#Concatenate both tuples and remove duplicates from tuple
res = set(tup1+tup2)
print(tuple(res))

#Find the index value of 9 (after concatenation)
res = tuple(res)
print(res.index(9))

#multiply above elements 3 times
multiply = (res*3)
print(multiply)