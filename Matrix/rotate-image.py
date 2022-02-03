"""
    Rotate image
    Desc: Rotate a given 2D matrix 90 degrees clockwise
    Link: https://leetcode.com/problems/rotate-image/
"""


# Solution 1
# Time: O(n^2) | Space: O(1)
# Runtime: 50 ms, faster than 36.55% of Python3 online submissions for Rotate Image.
def rotate(grid):
    n = len(grid)
    # Transposing the matrix
    for i in range(n):
        # Starting from i+1 avoids the diagonal
        for j in range(i + 1, n):
            print(grid[i][j], grid[j][i])
            # Swapping the elements
            grid[j][i], grid[i][j] = grid[i][j], grid[j][i]
    # Reversing the rows
    for i in grid:
        i.reverse()
    return grid


# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
