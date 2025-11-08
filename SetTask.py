#Create two empty sets

set1 = {}
print(type(set1))
set1= set()
set2= set()

#update set1 with 7,8,9,1,2,3,4,5,0
set1.update({7,8,9,1,2,3,4,5,0})
print(set1)

#update set2 with 4,5,6,0
set2.update({4, 5, 6, 0})
print(set2)

#check whether set2 is subset of set1 or no ?
check = set2.issubset(set1)
print(check)

"""#check whether both have common elements are no ?"""
commonElements = set1.intersection(set2)
print(commonElements)


#remove 8 from set 1 and set 2 ==> find the inferences
set1.remove(8)
print(set1)
# set2.remove(8)
# print(set2) KeyError: 8

#discard 0 from set1 and set2
set1.discard(0)
print(set1)
set2.discard(0)
print(set2)

#find collection of both sets ===> set1 and set2

set1.union(set2)
print(set1)
print(set2)
