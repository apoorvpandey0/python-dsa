"""
    Radix sort
"""

from functools import reduce
from typing import List


# Runtime: 806 ms, faster than 61.99% of Python3 online submissions for Sort an Array.
# Memory Usage: 22.7 MB, less than 28.41% of Python3 online submissions for Sort an Array.
def radixSort( nums: List[int]) -> List[int]:
    
    maxdigits = float('-inf')
    
    # Find maxdigits
    for ele in nums:
        maxdigits = max(maxdigits, len(str(ele)))

    # Bucket corresponds to each digit from -9 to 9
    # Run the loop for max number of digits in the list
    for digit in range(maxdigits):
        buckets = [[]for _ in range(10+9)]
        for ele in nums:
            # Get the digit at the current position
            # and append it to the corresponding bucket
            if ele < 0:
                num = 9 - abs(ele)//10**(digit)%10
                buckets[num].append(ele)
            else: 
                num = ele//10**(digit)%10
                buckets[num+9].append(ele)        
        
        # Reduce the buckets to a single list
        nums = reduce(lambda x,y:x+y,buckets)
        # print(buckets)
    return nums

if __name__ == "__main__":
    
    assert(radixSort([1,3,-5,2,0,0,4,6]) == [-5,0,0,1,2,3,4,6])
    assert(radixSort([-2,3,-5]) == [-5,-2,3])
    assert(radixSort([-42,-4434,-3535,-423422]) == [-423422,-4434,-3535,-42])
    assert(radixSort([42,4434,3535,423422]) == [42,3535,4434,423422])
