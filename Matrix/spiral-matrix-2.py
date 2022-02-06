"""
    Spiral matrix 2
    Traverse the matrix in spiral and put numbers in the places you visit
    Link: https://leetcode.com/problems/spiral-matrix-ii/
"""


# Runtime: 45 ms, faster than 40.46% of Python3 online submissions for Spiral Matrix II.
def spm(n):
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    # print(matrix)

    height = n
    width = n

    top = 0
    bottom = height - 1
    left = 0
    right = width - 1
    counter = 1
    while top < bottom and left < right:

        for col in range(left, right):
            matrix[top][col] = counter
            counter += 1

        for row in range(top, bottom):
            matrix[row][right] = counter
            counter += 1

        for col in range(right, left, -1):
            matrix[bottom][col] = counter
            counter += 1

        for row in range(bottom, top, -1):
            matrix[row][left] = counter
            counter += 1

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    # If a matrix remain inside it is either a 1xn or a mx1
    # a linear scan will return the same order as spiral for these
    if counter <= height * width:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                matrix[row][col] = counter
            counter += 1

    return matrix


print(spm(3))
print(spm(0))
print(spm(1))
