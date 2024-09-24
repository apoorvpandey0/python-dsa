"""
    Rotate image
    Desc: Rotate a given 2D matrix 90 degrees clockwise
    Link: https://leetcode.com/problems/rotate-image/
"""


# Solution 1
# Time: O(n^2) | Space: O(1)
# Runtime: 50 ms, faster than 36.55% of Python3 online submissions for Rotate Image.
def rotate(grid):
    matrix.reverse()
    # print(matrix)
    
    n = len(matrix)
    for i in range(n):
        # Start swapping from j = diagonal + 1
        # Diagonal ke i,j -> 0,0 | 1,1 | 2,2
        # Jinko swap karna hai unke ij -> 0,1->n | 1,2->n | 2,3->n
        # Basically j = i+1 selects the upper half of the matrix
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix
        


# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
