
# Valid
abc = "Hello"
Abc = "hELLO"
ABC = "ghello"

abc123 = "world!"
aBc_def = "world!"
abc_123 = "world!"

_abc = "valid"


# Invalid
# 123abc = "invalid"


# Arithematic operators: +,-,*,/,**
a = 100
b = 200
a+b
b*a

# Assignment operators

# c = 100
# print(c)

# # c = c+200
# c += 200
# print(c)

# # c = c-100
# c-=100
# print(c)

# c*=4
# print(c)

# c/=100
# print(c)


# c**=2
# print(c)



# Comparision operator
# if a == 100:
#     print("Hello")

# if a > 100:
#     print("Hello")

# if a < 100:
#     print("Hello")

# if a >= 100:
#     print("Hello")

# if a <= 100:
#     print("Hello")

# if a >= 100:
#     print("Hello")

# if a != 100:
#     print("Hello")
    
# Membership operators
str1 = "hello this is a string!"

# print("is" in str1)
# print("is" not in str1)


# Logical operators


# OR operator
# 0 or 0 = 0
# 0 or 1 = 1
# 1 or 0 = 1
# 1 or 1 = 1

# if a==101 or a==100:
#     print("OR")

# AND operator
# 0 and 0 = 0
# 0 and 1 = 0
# 1 and 0 = 0
# 1 and 1 = 1

# if (not a ==101) and (a==100):
#     print("AND")


# Identity opertaor

print(a is b)
print(a is not a)


# Bitwise operators

# |

# &

# ^

# ~

# <<

# >>



# Strings

str1 = 'hello'
str2 = "hello"
str3 = """hello this is a very loooooong stringgggggggggggggggggggggggg"""

# Access elements of a string
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])

# Slicing a string
# Range - [lower index, upper index)
print(str2[1:3])
print(str3[4:8])
print(len(str2))

print("hello" in str3)


str4 = "hello world this is"
str5 = str4.split(" ")
# print(str5)


print(str4.upper())
print(str4.lower())


print(str4+" "+str2)

print(str4.replace("hello","world"))


# Lists


lst1 = []
lst2 = list()

lst1.append("Apple")
lst2.append("Apple")

lst1.append("Apple")
lst2.append("Apple")


lst1.append(23)
lst1.append(True)
lst1.append(lst2)

print(lst1)
print(lst2)

# Access elements

# Slicing


a = [1,2,3,4,5]
a.remove(2)
a.remove(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
a.pop(1)
3
a.pop(6)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: pop index out of range




a.sort()
sorted(a)
[1, 4, 5]
a.reverse()


a = [1,2,3,4,5,6,7]
a[1:4] = "a"
a
[1, 'a', 5, 6, 7]















