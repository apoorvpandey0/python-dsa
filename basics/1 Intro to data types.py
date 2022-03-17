# Bool
isDataLoading = False
isDataLoading = True
 
if(isDataLoading):
    print("Loading data please wait!!!!")
else:
    print("Show data")
 
# int
num1 = 100
num2 = 200
 
print(num1+num2)
 
# String
str1 = "Hello"
str2 = 'World'
myName = """Hi this is a python tutorial"""
 
# print("My Fruits: ",fruits)
# print(myName)
 
 
# List
# A list is a mutable data type
fruits = ['Apple','Orange',"Papaya"]
print("My Fruits 1: ",fruits)
 
fruits.append("Mango")
 
print("My Fruits 2: ",fruits)
 
fruits.pop()
 
print("My Fruits 3: ",fruits)
 
 
# Tuple
# A Tuple is a immutable data type
fruits = ('Apple','Orange',"Papaya")
print("My Fruits Tuple: ",fruits)
# fruits.append("Mango")
 
 
# Set
# A set only has unique elements
mySet = set()
mySet.add("Apple")
mySet.add("Guava")
mySet.add("Grapes")
mySet.add("Apple")
print(mySet)
 
 
# Dictionary
# Dict stores the values in (key:value) pairs
# Very fast in operations
myDict = {
    'username':'apoorvpandey',
    'email':'abc@gmail.com',
    'phone':'123456789'
}
print(myDict)
print("Email is:",myDict['email'])
print("Phone is:",myDict['phone'])
 
myLst2 = list()
myTuple = tuple()
mySet2 = set()
myDict2 = dict()
 
# Dict 
myDict = "Hello"
print(myDict)
 

