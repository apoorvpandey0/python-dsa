"""
    Trapping rain water 2
    
    Desc: Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map,
          return the volume of water it can trap after raining.
    
    Solutions: 
          https://www.youtube.com/watch?v=fywyCy6Fyoo
          https://leetcode.com/problems/trapping-rain-water-ii/discuss/644813/Very-Easy-Python-solution-90

    Link: https://leetcode.com/problems/trapping-rain-water-ii/
"""

# Algorithm
"""
Create a visited array for given height map
mark all boundaries as visited
select the smallest boundary from min pq
explore its neighbours
    if neighbours height is >= current element
        simply delegate the boundary to that neighbour
    if neighbours height is < current element
        ie it can store water of volume max(0, current height - neighbours height)
        now set the height of neighbour as the height of current element
        and delegate the boundary to the neighbour
"""

import heapq


# Time: O(mn(log(mn)))
# Runtime: 416 ms, faster than 79.28% of Python3 online submissions for Trapping Rain Water II.
def trapWater(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    # print(matrix)
    h = []
    water = 0

    visited = [[0] * cols for _ in range(rows)]

    # Covering boundaries
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                visited[row][col] = 1
                heapq.heappush(h, (matrix[row][col], row, col))
    # print(visited)
    """
        NOTE:
        A heap is not a sorted structure, so there are many different orderings which form valid heaps.
        To get an element from heap always use heappop.
        
        while h:
            print(heapq.heappop(h), end=" ")
    """

    # Directions for Bottom, Top, Right and Left elements
    # Row x Column
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while h:

        # Current element
        ele = heapq.heappop(h)

        for dir in dirs:
            # Get the neighbour element
            # neighbours row x neighbours column
            nrow = ele[1] + dir[0]
            ncol = ele[2] + dir[1]

            # Boundary cases
            if nrow < 0 or ncol < 0 or nrow >= rows or ncol >= cols or visited[
                    nrow][ncol]:
                continue

            # print((nrow, ncol), matrix[nrow][ncol], (
            #     ele[1],
            #     ele[2],
            # ), ele[0])

            # If neighbour is >= ele simply add neighbur to heap with its own height and coordinates
            if matrix[nrow][ncol] >= ele[0]:
                heapq.heappush(h, (matrix[nrow][ncol], nrow, ncol))
                # print("Skipped")

            # If neighbour is < ele add neighbour to heap with ele height
            else:
                heapq.heappush(h, (ele[0], nrow, ncol))
                water += max(0, ele[0] - matrix[nrow][ncol])
                # print("Added water: ", max(0, ele[0] - matrix[nrow][ncol]))

            visited[nrow][ncol] = 1
            # print("Visited ", nrow, ncol, visited[nrow][ncol])
    return water


# 4
# print(trapWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))

# 10
# print(
#     trapWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3],
#                [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))

# 3
# print(trapWater([[5, 5, 5, 1], [5, 1, 1, 5], [5, 1, 5, 5], [5, 2, 5, 8]]))
