"""
    Set matrix zeroes
    Given an m x n integer matrix matrix, if an element is 0, 
    set its entire row and column to 0's, and return the matrix.
    Link: https://leetcode.com/problems/set-matrix-zeroes/
"""


# Solution 1:
# Brute forced
# Time and space O(n^2)
def sm1(grid):
    mat = grid.copy()
    rows = len(mat)
    cols = len(mat[0])
    rset = set()
    cset = set()

    print(mat)
    for i in range(rows):
        if i in rset: continue
        for j in range(cols):
            if j in cset: continue
            if grid[i][j] == 0:
                print("Running: ", i, j)
                if i not in rset:
                    mat[i] = [0] * cols
                    rset.add(i)
                if j not in cset:
                    for k in range(rows):
                        # print(k, j)
                        mat[k][j] = 0
                    cset.add(j)
        # print(mat)
        # print(grid)
    return mat


# Solution 2:
# Better Brute forced
# Algorithm
# 1. Traverse the matrix
# 2. record all rows and columns which need to be set as 0
# goto those columns after initial traversal and set the values to 0
# Time: O(n^2) | Space: O(m+n)
# Runtime: 235 ms, faster than 15.35% of Python3 online submissions for Set Matrix Zeroes.
def sm2(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    nrows = len(matrix)
    ncols = len(matrix[0])
    rows = set()
    cols = set()

    # Find out rows and cols to be set 0
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                
    # set rows 0
    for r in rows:
        for c in range(ncols):
            matrix[r][c] = 0
    
    # set cols 0
    for c in cols:
        for r in range(nrows):
            matrix[r][c] = 0
    
    return matrix


# Solution 3:
# Algorithm:
# 1. Instead of keeping seperate record of rownand columns
# 2. Simply use the first elements of the Matrix itself
# 3. In second pass set the rows and cols to 0
# Time: O(n^2) | Space: O(1)
def sm(mat):
    print(mat)
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        # if i in rset: continue
        for j in range(cols):
            # if j in cset: continue
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    # TODO: The code belows needs fixing!
    print(mat)
    for row in range(rows):
        if mat[row][0] == 0:
            mat[row] = [0] * cols
    print(mat)
    for col in range(cols):
        if mat[0][col] == 0:
            for k in range(rows):
                mat[k][col] = 0

    # print(mat)
    return mat


# print(sm([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# print(sm([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# print(
# sm([[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]))
print(sm([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
