"""
    Excel sheet column number
    Desc: Given a column title as appear in an Excel sheet, return its corresponding column number.
    Link: https://leetcode.com/problems/excel-sheet-column-number/
"""

"""
    Explaination:
    Essentially, what we asked to do here is to convert a number in the base 26 numeral system to a decimal number.
    This is a standard algorithm, 
    where we iterate over the digits from right to left and multiply them by the base to the power of the position of the digit.
    To translate a letter to a number we use the Python method ord which returns the Unicode code of the letter.
    By subtracting the code by 64, we can map letters to the numbers from 1 to 26.
"""
# Runtime: 36 ms, faster than 77.88% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.9 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans,pos = 0,0
        for letter in reversed(s):
            # Converting Character to Unicode number 
            # - 64 as "A" is 65 in Unicode so this will give "A" = 1
            digit = ord(letter)-64

            # Multiplying the number with 26^pos pos is its place in number ex. ones,tens,hundreds etc
            ans+=digit*26**pos
            pos+=1
        return ans
            
        