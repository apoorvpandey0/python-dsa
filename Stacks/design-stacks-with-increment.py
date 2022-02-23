"""
    Design Stacks with increment function
    Desc: 
    Link: https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""
# Solution 1:
# Simple approach
# Increment Time: O(n) | Space: O(1)
# Runtime: 265 ms, faster than 9.96% of Python3 online submissions for Design a Stack With Increment Operation.
# Memory Usage: 14.9 MB, less than 87.84% of Python3 online submissions for Design a Stack With Increment Operation.
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        else:return -1
        
    # This is O(n) time and O(1) space
    def increment(self, k: int, val: int) -> None:
        # Random access is not allowed in a real stack!
        for i in range(min(k,len(self.stack))):
            self.stack[i]+=val


# Solution 2:
# Using an increments array and lazily updating the elements when popped
# Increment Time: O(1) | Total Space: O(n)
# Runtime: 114 ms, faster than 83.93% of Python3 online submissions for Design a Stack With Increment Operation.
# Memory Usage: 14.9 MB, less than 61.24% of Python3 online submissions for Design a Stack With Increment Operation.
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = []

    # Simple to understand
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.increments.append(0)


    def pop(self) -> int:
        if self.stack:

            # Say increments is: [0,0,0,5,0,0,0,9]
            # This means increment the first four elements by 5 and also the first eight element by 9
            # Since 9 is present only once but it affetcs all the elements before it
            # Hence we'll pop and increment the new last element by 9, now the effect of 9 will still carry on
            lastIncrement = self.increments.pop()
            
            # This if handles the case to retain 9's effect on previous elements
            # After this new increments will be: [0,0,0,5,0,0,9]
            if self.increments:
                self.increments[-1] += lastIncrement
            
            # And now we can simply pop the last element, add the last increment and return it
            return self.stack.pop() + lastIncrement
        
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            # Make the last element += val 
            # So when we pop them this will increment all the elements of the stack
            if k >= len(self.stack):
                self.increments[-1] += val
            
            # Make last element of the fist k elements += val
            # So when we pop them this will increment only the first k elements
            else:
                self.increments[k-1] += val