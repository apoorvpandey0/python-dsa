"""
    Multiplication of two strings
    Link: https://leetcode.com/problems/multiply-strings/
"""

# Runtime: 263 ms, faster than 19.83% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.9 MB, less than 90.06% of Python3 online submissions for Multiply Strings.
def multiply(num1: str, num2: str) -> str:
    """
        Example: 
            23 x 45 will make four sums as,
            23 x 45 = 3 * 5 + 20 * 5 + 3 * 40 + 20 * 40
            23 x 45 = 15    + 100    + 120    + 800 
            23 x 45 = 1035
        

    """
    l1 = len(num1)
    l2 = len(num2)
    answer= 0
    for i in range(l2-1,-1,-1):
        e2 = int(num2[i])
        for j in range(l1-1,-1,-1):
            e1 = int(num1[j])
            # Use correct place values to get each element then multiply them
            mul = (e2 * ( 10**((l2-1)-i) ) )* (e1 * ( 10**((l1-1)-j) ))
            # print(mul)
            answer+=mul
    return str(answer)