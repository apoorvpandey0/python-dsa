"""
    Pallindrome number
    Link: https://leetcode.com/problems/pallindrome-number/
"""

# Time: O(n) | Space: O(1)
# Runtime: 68 ms, faster than 79.62% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14 MB, less than 43.14% of Python3 online submissions for Palindrome Number.
def isPalindrome(self, x: int) -> bool:
    """ 
        https://www.code-recipe.com/post/palindrome-number
    """
    tmp = x
    reversedNum = 0
    while tmp>0:
        lastDigit = tmp%10
        reversedNum = reversedNum*10 + lastDigit
        tmp//=10
        # print(reversedNum,lastDigit)
    return reversedNum == x

# Time: O(n) | Space: O(n)
# Runtime: 59 ms, faster than 93.86% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14 MB, less than 56.14% of Python3 online submissions for Palindrome Number.
def isPalindrome(self, x: int) -> bool:
    return str(x)==str(x)[::-1]