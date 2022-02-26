"""
    Add one to a number represented as an array of digits.
    Link: https://leetcode.com/problems/plus-one/
"""

# Algorithm
# Add one to last element
# If last element is 10, then start the loop
# from the second last element and add 1 to it
# If the last second element is 10 set it as 0 and continue the loop to last 3rd
# If the last second element is <=9, simply break the loop 
# Handle the leftover carry case after everything
# Runtime: 32 ms, faster than 88.77% of Python3 online submissions for Plus One.
# Memory Usage: 13.9 MB, less than 83.78% of Python3 online submissions for Plus One.
def plusOne(nums):
    N = len(nums)
    nums[-1]+=1
    
    if nums[-1] == 10:
        nums[-1] = 0
    
        for i in range(N-2,-1,-1):
            nums[i]+=1

            # Ex: [1,2,3,4] => No carry is left
            if nums[i]<=9: break

            # Ex: [1,2,10,4] => Carry is still left
            if nums[i]==10:
                nums[i]=0
    
    #If carry is still left
    if nums[0]==0:
        nums[0]=0
        nums.insert(0,1)

            
    return nums

# Solution 2: Cleaner code
# we employ 3 variables:
# s - the sum between the digit[i], res and mem
# res = s % 10 ( initially 1, because we need to add one to the last digit)
# mem = s // 10
# we iterate backwards on the digits and we add update the digits array until mem becomes 0 ( we don't need to add anything anymore)
# if we have updated all the digits and mem != 0, we need to add it to the array as well ( e.g. input: digits = [9], output = [1, 0] )
class Solution:
    def plusOne(digits):
        n = len(digits)
        res = 1
        mem = 0 
        for i in range(n - 1, -1, -1):
            s = digits[i] + res + mem
            res = s % 10
            mem = s // 10
            digits[i] = res
            if mem == 0:
                break
        if mem != 0:
            digits = [mem] + digits
        return digits