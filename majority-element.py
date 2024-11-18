"""
    169. Majority Element
    Desc: The majority element is the element that appears more than ⌊n / 2⌋ times.
          You may assume that the majority element always exists in the array.
    Link: https://leetcode.com/problems/majority-element/
    soln: https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly
"""

from collections import Counter


# Solution 1:
# Using python collections
# Time: O(n) | Space: O(n)
# Runtime: 176 ms, faster than 60.15% of Python3 online submissions for Majority Element.
def me(nums):
    c = Counter(nums)
    return max(nums, key=c.get)


# Solution 2:
# Using Moores Voting algorithm
# Time: O(n) | Space: O(1)
# Runtime: 192 ms, faster than 59.39% of Python3 online submissions for Majority Element.
def me2(nums):
    candidate_index, count = 0, 1

    # Finding the candidate element
    for i, num in enumerate(nums):
        print(i, count)
        if nums[candidate_index] == num:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate_index = i
            count = 1

    # Since we can assume in this question that there will always be a majority element
    # We may skip this step
    # Verification is done when there is no majority element ex: [1,2,1,3,1,4,5]
    # Verifying the candidate element
    count = 0
    for i in nums:
        if i == nums[candidate_index]:
            count += 1
    if count > len(nums / 2):
        return nums[candidate_index]

# Voting alogirithm but easier implementation
def me21(nums):
    ans = nums[0]
    count = 0

    for i,ele in enumerate(nums):

        # if current ans is found +1
        if ele == ans: 
            count+=1
        
        else:
            # if count will become negative at this point that means the current element cannot be majority element
            if count == 0:
                ans = ele

            # if current ans is not found -1
            else: 
                count-=1
    return ans
        


# Solution 3:
# middlemost element should always be in majority
# Time: O(n log n)
# Runtime: 176 ms, faster than 60.15% of Python3 online submissions for Majority Element.
def me3(nums):
    nums.sort()
    return nums[len(nums) // 2]


print(me2([1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 2, 2]))
