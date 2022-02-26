"""
    Valid parentheses
    Ex: Valid:    "()", "()[]{}",
        Invalid:  "(]", "([)]"
        Just like in real expressions:
        An opened bracket of type must be closed before another of the same type is closed.
    Link: https://leetcode.com/problems/valid-parentheses/
"""

# Runtime: 35 ms, faster than 71.87% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 66.49% of Python3 online submissions for Valid Parentheses.
def isValid(self, s: str) -> bool:
    brackets = {"{":"}","(":")","[":"]"}
    stack = []
    for char in s:
        if char in brackets:
            # i.e. this is an opening bracket
            # We can add this to our stack and continue
            stack.append(brackets[char])
        elif stack and stack[-1] == char:
            
            stack.pop()
        else:
            return False
    return len(stack) == 0