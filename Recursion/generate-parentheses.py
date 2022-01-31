"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Link: https://leetcode.com/problems/generate-parentheses/
"""


# Approach 1: Using recursion
# Time: 2 x T(n-1)
# Runtime: 32 ms, faster than 91.53% of Python3 online submissions for Generate Parentheses.
def gen(n):
    """
        Common mistake:
        Writing this inside if conditions is wrong as it adds extra bracket to the answer
            answer+=')'
            helper(...)
        
        The correct approach is to add the bracket in the function parameter only!
    """

    def helper(n, open, close, answer):
        if close < open:
            helper(n, open, close + 1, answer + ')')
        if open < n:
            helper(n, open + 1, close, answer + '(')
        if open == close == n:
            answers.append(answer)

    answers = []
    helper(n, 0, 0, "")
    return answers


print(gen(3))
