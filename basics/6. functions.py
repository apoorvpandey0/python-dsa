# We declare a function using def keyword
# Functions help us to reduce repetitive code
# Functions are block of code

# Syntax
# def function_name( parameters ):
    # write function body
    # return something
    
def isEvenOdd(number):
    if number%2==0:
        print("{} is Even".format(number))
    else:
        print("{} is Odd".format(number))

N = int(input('Please give a number: '))

isEvenOdd(N)


def greet(name="Default name",greeting = "Default greeting"):
    print("Hi {}, Good {}.".format(name,greeting))

# Positional parameters/Arguments
greet('Person1','Evening')
greet('Evening','Person1')

# Keyword/Named arguments
greet(greeting = 'Morning',name = 'Person3')

# Default value
greet()
greet(name = "Apoorv")
greet(greeting = "Night")


def sumAB(a,b):
    # print(a+b)
    return a+b
    
summation = sumAB(100,200)

print(summation)



# Question 2
def evenNumbersinRange(upper,lower):
    if lower%2==0:
        isEven = True
    else:
        isEven = False
        lower+=1
    
    result = []
    for i in range(lower,upper+1,2):
        # print(i)
        result.append(i)
    return result

[10,12,14,16,18,20]
result1 = evenNumbersinRange(lower = 10,upper = 20)
print("Result 1: ",result1)

# Create result2 list which contains elements of list 1 multiplied by 2

result2 = []
for element in result1:
    result2.append(element*2)
print("Result 2: ",result2)











