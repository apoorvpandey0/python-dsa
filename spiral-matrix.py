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
def spiral3(matrix):
    """
        remove the top row
        remove the right row
        remove the bottom row
        remove the left row
        and repeat until the matrix is empty.
        when you remove a row, append all it's element in a array and that's the answer.
        https://leetcode.com/problems/spiral-matrix/discuss/1557262/Python-or-faster-than-97-or-short-and-simple-solution-(with-comments)
    """
    result = list()
    while len(matrix) > 0:
        try:
            result += matrix.pop(0)  #remove the first nested list (top row)
            result += [x.pop(-1) for x in matrix
                       ]  #remove every last element of the lists (right row)
            result += matrix.pop(
                -1)[::
                    -1]  #remove last nested list in reverse order (bottom row)
            result += [
                x.pop(0) for x in matrix
            ][::-1]  #remove every last element of the lists (left row)
        except:
            break  #if at any moment the matrix is empty, break the loop and return the result array
    return result


# Solution 4:
# God Mode
def spiral4(matrix):
    """
        https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
    """
    return matrix and [*matrix.pop(0)] + spiral3([*zip(*matrix)][::-1])


# print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
