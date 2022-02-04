"""
    Max consecutive ones
    Given a boolean 2D array of n x m dimensions where each row is sorted.
    Find the 0-based index of the first row that has the maximum number of 1's.
    Link: https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
"""

# Solution 1:
# Brute force - Time: O(nm)

# Solution 2:
# Find first one using Binary search - Time: O(nlog(m))


# Solution 3:
# Time taken: 0.5/1.6s
# Store max value and check against it in next rows - Time: O(n+m)
def mco(mat):
    rows = len(mat)
    cols = len(mat[0])
    counter = 0
    counter = mat[0].count(1)
    index = 0
    for i, row in enumerate(mat[1:]):
        toCheck = cols - counter - 1
        # print(counter, index)
        if toCheck >= 0:
            if row[toCheck] == 1:
                remainingOnesInTheRow = row[:toCheck + 1].count(1)
                counter += remainingOnesInTheRow
                if remainingOnesInTheRow > 0:
                    index = i + 1
    return index if counter > 0 else -1


print(mco([[0, 0, 0, 0]]))
print(mco([[1, 1, 1, 1, 1]]))
print(mco([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
