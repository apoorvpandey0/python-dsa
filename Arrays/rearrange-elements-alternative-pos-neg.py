"""
    https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""

# Brute forced
# Two pass |  O(n) space and time
def rearrangeArray(self, nums: List[int]) -> List[int]:
  # Seperate out positive and negatives
  # pos and neg should be equal in length as per constraints in question
    pos = []
    neg = []
    for ele in nums:
        if ele<0: neg.append(ele)
        if ele>0: pos.append(ele)
    # print(pos,neg)

    # Update answer array as per index value of i
    p = 0
    n = 0
    i = 0
    ans = []
    # Since nums has even length ans consists of an equal number of positive and negative integers.
    while p<len(pos) or n<len(neg):
        if i%2 ==0 and p<len(pos):
            ans.append(pos[p])
            p+=1
        elif i%2 and n<len(neg):
            ans.append(neg[n])
            n+=1
        # print(ans,i)
        i+=1
    return ans


# One pass solution | O(n) space and time
def rearrangeArray(self, nums: List[int]) -> List[int]:
    pos = 0
    neg = 1
    ans = [0 for i in nums]

    for i,ele in enumerate(nums):
        if ele>0:
            ans[pos] = ele
            pos+=2
        else:
            ans[neg] = ele
            neg+=2
    return ans
