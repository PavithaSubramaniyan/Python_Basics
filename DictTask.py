
#create a dictionary
dictItem = {"Name": "Pavitha",
            "Age": 26,
            "Place":"Chennai",
            "is_student": True}

dictio  = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

#Extract "bobtn" from above dictionary
print(dictio[3][0][::2])

#Extract "arbeg" from above dictionary
print(dictio[3][2][-1:1:-1])

#print all keys in dictionary and convert it into tuple
print(dictItem.keys())
print(tuple(dictItem.keys()))

#Find the average of all numbers available under key
keySum = dictio[2]
print(sum(keySum))