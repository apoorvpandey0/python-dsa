https://youtu.be/vTG32RrjJaQ?si=kqX_8QmtT8J3H34X
https://www.youtube.com/watch?v=DtJVwbbicjQ better






Primitive Soln: only for dictinct array elements
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = Stack()
        nxtG = {}

        for num in nums2:

            while not stack.is_empty() and stack.peek() <= num:
                popele = stack.pop()
                nxtG[popele] = num
            
            stack.push(num)
        
        return [nxtG[ele] if ele in nxtG else -1 for ele in nums1]
