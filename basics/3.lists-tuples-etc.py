# Tuple unpacking

# Tuple of strings
tup = ("Python Web dev","Apoorv","1 month")

# 1st
course_name ,instructor,duration = tup

# 2nd
# course_name ,instructor,duration = tup[0],tup[1],tup[2]

# Third
# course_name = tup[0]
# instructor = tup[1]
# duration = tup[2]

print(course_name,instructor,duration)

mySet = {"Apple","Banana","Grapes"}
mydict2 = {} 
mySet3 = set()


# Access elements
print(mySet)
print("Apple" in mySet)

for ele in mySet:
    print(ele)
    
mySet.add("Orange")
mySet.add("Orange")
mySet.add("Orange")
print(mySet)

mySet.remove("Orange")
print(mySet)
    
A = {"Apple","Banana","Grapes","Orange"}
B = {"Apple","Avacado"}

C = A.union(B)
D = A.intersection(B)
print("Union:",C)
print("Intersection:",D)






# Dictionary
# Key: value pair

user = {
    'username':'Batman',
    'password':'Batmobile',
    'phone':'123456789'
}

# Normal accessing
print(user['username'])
print(user['address'])

# Using get
print(user.get('phone'))
print(user.get('address'))


# Adding items to a dictionary
user['address'] = 'Bat homes'
# print(user)

# Changing values if a dict
user['address'] = 'Bat homes Inc'
# print(user)

# Remove the value
user.pop('phone')
print(user)

user.popitem()
print(user)


# Functions of a dict\
print(user.keys())
print(user.values())
print(user.items())


# dict_keys(['username', 'password', 'phone', 'address'])
# dict_values(['Batman', 'Batmobile', '123456789', 'Bat homes Inc'])
# dict_items([('username', 'Batman'), ('password', 'Batmobile'), ('phone', '123456789'), ('address', 'Bat homes Inc')])



























