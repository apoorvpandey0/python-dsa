"""
    Design a basic calculator
    Desc: Calculates simple imputs like [+, -, *, /] not parentheses
    Link: https://leetcode.com/problems/basic-calculator-ii/
"""

from collections import deque


# Solution 1:
# Using a stack
# Time: O(n) | Space: O(n)
# Runtime: 76 ms, faster than 89.52% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.9 MB, less than 29.55% of Python3 online submissions for Basic Calculator II.
def calculate(s: str) -> int:
    """
        We keep track of last operator and last number
        Stack stores all additiions and subtractions
        Thats why we need to add extra + at the end so that the right most number is also considered in loop
    """

    dq = deque()
    curr = ""
    operator = '+'
    ops = ['+', '-', '*', '/']
    s = s + '+'
    for ele in s:
        # Ignore whitespaces
        if ele == ' ':
            continue

        # If an operator is found then make operations on stack
        if ele in ops:
            if operator == '+':
                dq.append(int(curr))
            elif operator == '-':
                dq.append(int(curr) * -1)
            elif operator == '*':
                last = dq.pop()
                new = last * int(curr)
                dq.append(new)
            elif operator == '/':
                last = dq.pop()
                new = int(last / int(curr))
                dq.append(new)
            curr = ''
            operator = ele

        # If a number is found then keep adding it to current number
        else:
            curr += ele

    # Now simply sum up all the values in the stack
    return sum(dq)


# Solution 2:
# Time: O(n) | Space: O(1)
# TODO: Complete this
def calculate2(s):
    """
        Instead of using a stack, we use a variable lastNumber to track the value of the last evaluated expression.
        If the operation is Addition (+) or Subtraction (-), add the lastNumber to the result instead of pushing it to the stack. The currentNumber would be updated to lastNumber for the next iteration.
        If the operation is Multiplication (*) or Division (/), we must evaluate the expression lastNumber * currentNumber and update the lastNumber with the result of the expression. This would be added to the result after the entire string is scanned.
    """
    ops = {'+', '-', '*', '/'}
    curr = ""
    operator = '+'
    s = s + '+'
    result = 0
    last = 0
    for ele in s:
        # Ignore whitespaces
        if ele == ' ':
            continue

        # If an operator is found then make operations on stack
        if ele in ops:
            if operator == '+':
                dq.append(int(curr))
            elif operator == '-':
                dq.append(int(curr) * -1)
            elif operator == '*':
                last = dq.pop()
                new = last * int(curr)
                dq.append(new)
            elif operator == '/':
                last = dq.pop()
                new = int(last / int(curr))
                dq.append(new)
            curr = ''
            operator = ele

        # If a number is found then keep adding it to current number
        else:
            curr += ele

    # Now simply sum up all the values in the stack
    return sum(dq)


print(calculate("2*3-4*5"))