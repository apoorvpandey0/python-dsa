# Solution 1:
# My copy of solution 2
# Runtime: 50 ms, faster than 24.62% of Python3 online submissions for Spiral Matrix.
def spiral(matrix):
    if not matrix:
        return []

    answer = []
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1

    while left < right and top < bottom:
        for col in range(left, right):
            answer.append(matrix[top][col])
        # print(answer)

        for row in range(top, bottom):
            answer.append(matrix[row][right])
        # print(answer)
        for col in range(right, left, -1):
            answer.append(matrix[bottom][col])
        # print(answer)
        for row in range(bottom, top, -1):
            answer.append(matrix[row][left])
        # print(answer)
        left += 1
        right -= 1
        top += 1
        bottom -= 1

    # To cover solution 2's edge case
    if len(answer) < rows * cols:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                answer.append(matrix[row][col])

    return answer


# print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# print(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral([[1]]))


# Solution 2:
# Cleaner approach
# Desc: The code speaks for itself
def spiral2(matrix):
    """
        https://leetcode.com/problems/spiral-matrix/discuss/394774/python-3-solution-for-spiral-matrix-one-of-the-most-easiest-you-will-never-forget/1026252
    """
    height = len(matrix)
    width = len(matrix[0])

    top = 0
    bottom = height - 1
    left = 0
    right = width - 1

    ans = []
    while top < bottom and left < right:

        for col in range(left, right):
            ans.append(matrix[top][col])

        for row in range(top, bottom):
            ans.append(matrix[row][right])

        for col in range(right, left, -1):
            ans.append(matrix[bottom][col])

        for row in range(bottom, top, -1):
            ans.append(matrix[row][left])

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    # If a matrix remain inside it is either a 1xn or a mx1
    # a linear scan will return the same order as spiral for these
    if len(ans) < height * width:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                ans.append(matrix[row][col])

    return ans


# print(spiral2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral2([[1]]))


# Solution 3:
# Removing Rows and columns method
# Runtime: 46 ms, faster than 34.16% of Python3 online submissions for Spiral Matrix.
def spiral3(mat):
    """
        remove the top row
        remove the right row
        remove the bottom row
        remove the left row
        and repeat until the matrix is empty.
        when you remove a row, append all it's element in a array and that's the answer.
    """
    result = list()
    # Using try catch here is critical!
    while len(mat) > 0:
        try:
            #remove the first nested list (top row)
            result += mat.pop(0)
            #remove every last element of the lists (right row)
            result += [col.pop(-1) for col in mat]
            #remove last nested list in reverse order (bottom row)
            result += mat.pop(-1)[::-1]
            #remove every last element of the lists (left row)
            result += [col.pop(0) for col in mat][::-1]
        except:
            #if at any moment the matrix is empty, break the loop and return the result array
            break
    return result


# Solution 4:
# God Mode
# Using recursion
def spiral4(matrix):
    """
        https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
    """
    return matrix and [*matrix.pop(0)] + spiral4([*zip(*matrix)][::-1])


# Solution 5:
def spiral5(matrix):
    """
        1 - pop the first row and store it in result
        2 - rotate the remaining matrix
        3 - jump to 1st step.
    """
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = (list(zip(*matrix)))[::-1]
    return result


# print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# print(spiral3([[7], [9], [6]]))
# print(spiral3([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
# print(spiral3([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]))
# print(spiral3([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
