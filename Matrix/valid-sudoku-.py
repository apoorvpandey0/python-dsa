"""
    Validate a sodoku board
    Link: https://leetcode.com/problems/valid-sudoku/
"""
# TODO: better explaination in soln2

from collections import defaultdict


# Solution 1:
# Easy to understand approach
# Time: O(n^2) | Space: O(n^2)
# Runtime: 169 ms, faster than 25.47% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.8 MB, less than 99.73% of Python3 online submissions for Valid Sudoku.
def valid(board):
    # Validate rows
    for row in board:
        rs = set()
        for ele in row:
            if ele == '.': continue
            if ele in rs: return False
            else: rs.add(ele)

    # Validate columns
    for col in zip(*board):
        rs = set()
        for ele in col:
            if ele == '.': continue
            if ele in rs: return False
            else: rs.add(ele)
    sq = [[set(), set(), set()] for _ in range(3)]
    # print(sq)
    for r in range(9):
        for c in range(9):
            ele = board[r][c]
            if ele == '.': continue
            if ele in sq[r // 3][c // 3]:
                print(ele, r, c)
                return False
            else:
                sq[r // 3][c // 3].add(ele)
    # print(sq)
    return True


# Solution 2:
# One pass approach
# Time: O(n^2) | Space: O(n^2)
# Runtime: 138 ms, faster than 46.79% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.9 MB, less than 95.58% of Python3 online submissions for Valid Sudoku.
def valid2(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    sq = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.': continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c]
                    or board[r][c] in sq[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            sq[(r // 3, c // 3)].add(board[r][c])
    return True


print(
    valid([["8", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
