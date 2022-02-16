"""
    Simplify directory path
    Desc: Given an absolute path for a file (Unix-style), simplify it.
    Link: https://leetcode.com/problems/simplify-path/
"""


# Solution:
# Easiest approach by splitting the given path
# Time: O(n) | Space: O(n)
# Runtime: 45 ms, faster than 50.29% of Python3 online submissions for Simplify Path.
# Memory Usage: 13.9 MB, less than 94.72% of Python3 online submissions for Simplify Path.
def simplifyPath(self, path: str) -> str:

    # For example "/home//../abc/" would be aplit as ['', 'home', '', '..', 'abc', '']
    stack = []
    path = path.split('/')

    # for each element in split path
    for ele in path:

        # ignore = '', '.' and '..' if stack is empty
        if ele == '' or ele == '.' or (ele == '..' and not stack):
            continue

        # if ele is '..' and stack is not empty, pop the last element
        elif ele == '..' and stack:
            stack.pop()

        # push normal strings to stack
        else:
            stack.append(ele)
    # print(stack)

    return "/" + "/".join(stack) if stack else "/"