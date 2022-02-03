"""
    Returns the lucky numbers in the matrix.
    Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
"""


# Solution 1:
# Time: O(n^2)
# Runtime: 160 ms, faster than 54.29% of Python3 online submissions for Lucky Numbers in a Matrix.
def ln(mat):
    rows = len(mat)
    cols = len(mat[0])

    minr = [float('inf') for i in range(rows)]
    maxc = [float('-inf') for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            minr[i] = min(mat[i][j], minr[i])
            maxc[j] = max(mat[i][j], maxc[j])
    # print(minr)
    # print(maxc)
    # print(mat)

    return list(set(minr).intersection(maxc))


# Solution 2:
# Time: O(n^2)
# Runtime: 120 ms, faster than 96.78% of Python3 online submissions for Lucky Numbers in a Matrix.
def ln2(mat):
    """
        Key points:
            *matrix decomposes it into separate lists each representing a row.
                Ex: if matrix =[[1,2], [3, 4]] then *matrix returns two lists [1,2] and [3, 4]
            zip([1, 2], [3, 4]) returns two lists of [1, 3] and [2, 4] which are the columns of the matrix
            & between two sets minrow and maxcol returns the intersection of two sets
    """
    rows = len(mat)
    cols = len(mat[0])

    minr = set(min(row) for row in mat)
    maxc = set(max(col) for col in zip(*mat))

    return list(set(minr).intersection(maxc))


print(ln2([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
