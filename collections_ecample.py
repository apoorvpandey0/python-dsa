import collections as c
from typing import ChainMap

# Named tuple is a way to create a new data type with a name.
nt = c.namedtuple('course',['name','technology','duration'])
course1 = nt('Python for Beginners','Python',3)
course2 = nt._make(['Data Science','Python',3])

# print(course1)
# print(course1.name)
# print(course2)

# -------------------------------------------------------------------

# Deque in Python is a double-ended queue.
# It is optimized for fast appends and pops from either end.
dq = c.deque(["Mon","Tue","Wed"])
# print (dq)

# Append to the right
# print("Adding to the right: ")
dq.append("Thu")
# print (dq)

# append to the left
# print("Adding to the left: ")
dq.appendleft("Sun")
# print (dq)

# Remove from the right
# print("Removing from the right: ")
dq.pop()
# print (dq)

# Remove from the left
# print("Removing from the left: ")
dq.popleft()
# print (dq)

# Reverse the dequeue
# print("Reversing the deque: ")
dq.reverse()
# print (dq)

# ----------------------------------------------------------------------

# Chainmap in Python is a class that combines multiple mappings/ sets into one list.
a = {'a':1,'b':2}
b = {'c':3,'d':4}
c = {'e':5,'f':6}
cm = ChainMap(a,b,c)
# print(cm)