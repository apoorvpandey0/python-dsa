# For loops

# for i in range(10):
#     print(i)

names = ['Person1','Person2','Person3']

print('For loop')
# Normal for loop
# Format 
# for index in range:
#     do something

for index in range(len(names)):
    print(names[index],index)
print(" ")

print('For In loop')
# For in loop
# for variable in list
#     do something
for element in names:
    print(element)
    
    
# While loop

# Format:
# while some condition == True:
#     do something
    
print(" ")
print("While loop")
i = 1
while i<=10:
    print(i)
    i+=1
    
    
    
    
    
    
# Print a table of a given number
N = int(input('Enter the number: '))

for i in range(1,11):
    print("{} x {} = {}".format(N,i,N*i))

i = 1
while i<=10:
    print("{} x {} = {}".format(N,i,N*i))    
    i+=1


# Question 2:
# print all the even number between given range including upper
lower = int(input('Enter the lower range: '))
upper = int(input('Enter the upper range: '))

if lower%2==0:
    isEven = True
else:
    isEven = False
    lower+=1
    
for i in range(lower,upper+1,2):
    print(i)



    




    
    
    
    
    
    
    
    

