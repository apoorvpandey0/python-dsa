a = 1700
b = 500
c = 300

# These are two structures
if a>b and a>c:
    print('A greatest')
if b>c and b>a:
    print('B greatest')
else:
    print('C is greatest')


# This is one single if elif else structure
if a>b and a>c:
    print('A greatest')
elif b>c and b>a:
    print('B greatest')
else:
    print('C is greatest')

# Enter your data: This is my data
# Words:  ['This', 'is', 'my', 'data']
input_data = input('Enter your data: ')
print("Words: ",input_data.split(' '))