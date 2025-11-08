#Create an empty list (two ways)
li  =[]
li = list()


#Concatenate with [5,6,7,8]
lis = [1,2]
concatList = [5,6,7,8]
print("Get liat",lis+concatList)

#add 8,9,1,5,6,7,8,1 elements to that list
lis.extend([8,9,1,5,6,7,8,1])
print(lis)

#Find frequency of 8 (count)
print(f"find frequency of 8: {lis.count(8)}")

#find the mean of the list
res = sum(lis)/len(lis)
print(res)

#find sum (List) + min + Max
print(f"Find sum of lis: {sum(lis)}")
print(f"Find max of lis: {max(lis)}")
print(f"Find min of lis: {min(lis)}")

#Find median of the list

#remove duplicates from list and give output in the format of tuple
lis = list(set(lis))
print("set Conversion:",lis)
lis = tuple(lis)
print(lis)

print(type(lis))