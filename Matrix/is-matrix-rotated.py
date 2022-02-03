"""
    1886. Determine Whether Matrix Can Be Obtained By Rotation
    Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
    Soln: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss/1589592/Key-points-or-Trick-or-Easy-to-remember-for-future
"""


# Time: O(n^2)
# Runtime: 44 ms, faster than 78.15% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
def rotated(mat, target):
    n = len(mat)
    once, twice, thrice, four = True, True, True, True
    for i in range(n):
        for j in range(n):

            # Condition if rotated once
            if mat[i][j] != target[j][(n - 1) - i]:
                once = False

            # Condition if rotated twice
            if mat[i][j] != target[(n - 1) - i][(n - 1) - j]:
                twice = False

            # Condition if rotated thrice
            if mat[i][j] != target[(n - 1) - j][i]:
                thrice = False

            # Condition if rotated four times
            if mat[i][j] != target[i][j]:
                four = False
    # return (once, twice, thrice,four)
    return once or twice or thrice or four


# Once
# print(rotated([[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))

# Twice
print(
    rotated(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))

# Four times
# print(
#     rotated([[0, 0, 0], [0, 0, 1], [0, 0, 1]],
#             [[0, 0, 0], [0, 0, 1], [0, 0, 1]]))
