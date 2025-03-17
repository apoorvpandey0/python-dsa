class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return len(self.stack) == 0
    def __repr__(self):
        return f"Stack({list(self.stack)})"
    def to_list(self):
        return list(self.stack)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = Stack()

        for ele in asteroids:
            # only collide when there is a positive asteroid on the stack
            while not stack.empty() and stack.peek() > 0 and ele < 0:
                
                # Check for collision (if the current asteroid is larger in absolute value)
                if abs(stack.peek()) < abs(ele):
                    stack.pop()
                    continue
                elif abs(stack.peek()) == abs(ele):  # Both asteroids destroy each other
                    stack.pop()
                break
            else:
                stack.push(ele)
        return stack.to_list()
