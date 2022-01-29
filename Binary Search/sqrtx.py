"""
    Find integer part for sqrt x
    Link: https://leetcode.com/problems/sqrtx/
"""

# Time: O(log(n))
# Runtime: 126 ms, faster than 21.23% of Python3 online submissions for Sqrt(x).
from unicodedata import decimal


def sqrt(x):
    left, right = 0, x
    answer = -1
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        # print(left, mid, right)
        if mid * mid == x or (mid * mid <= x and (mid + 1) * (mid + 1) > x):
            return mid
        elif mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return answer


# Time: O( log(n) + p*9 )
def sqrt2(x, p=0):
    # x: find sqrt of x
    # p: decimal points
    i = sqrt(x)
    if p < 1:
        return i
    for power in range(1, p + 1):
        for j in range(0, 10):
            decimal = (0 if not j else j / (pow(10, power)))
            num = i + decimal
            if (num * num <= x) and ((num + pow(10, -power))**2 > x):
                # print(num)
                i = num
                break
    return i


print(sqrt2(0, 5), pow(0, 0.5))
print(sqrt2(1, 5), pow(1, 0.5))
print(sqrt2(10, 5), pow(10, 0.5))
print(sqrt2(64, 5), pow(64, 0.5))

# print(sqrt(0))
# print(sqrt(1))
# print(sqrt(64))