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