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
# Edge cases
# Since matrix 0,0 is only one place, so it cannot store 0 indicator for both row0 and col 0
# Hence we need one more variable to track if first rows needs to be set as 0
# And we will use 0,0 as regularly for storing 0 indicator for column 0
# This coule be vice versa, or if its confusing use two seperate variable for 0 indicators of 0th row and 0th column
# Time: O(n^2) | Space: O(1)
def sz3(self, matrix: List[List[int]]) -> None:
    nrows = len(matrix)
    ncols = len(matrix[0])
    firstRow0 = False

    # Determine 0 indicator for rows and columns with special case for row 0
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i][j] == 0:
                if (i==0):
                    firstRow0 = True
                else:        
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    # print(matrix)

    # Set all rows 0 where 0 indicator is present from 1,nrows -> again due to special case for row 0
    for r in range(1,nrows):
        if matrix[r][0] == 0:
            for c in range(ncols):
                matrix[r][c] = 0
    # print(matrix)

    # Set all columns to 0 where 0 indicator for column is present
    for c in range(ncols):
        if matrix[0][c] == 0:
            for r in range(nrows):
                matrix[r][c] = 0
    
    # print(firstRow0)

    # Handle special case row 0 at last, if not done at last the first row will be overwritten and history for columns will be lost
    if firstRow0==True:
        for c in range(ncols):
            matrix[0][c] = 0

    # print(mat)
    return matrix


# print(sm([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# print(sm([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# print(
# sm([[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]))
print(sm([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
