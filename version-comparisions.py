"""
    Compare version numbers
    Desc: Compare two version numbers version1 and version2.
          If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
    Link: https://leetcode.com/problems/compare-version-numbers/
    
"""

# Runtime: 41 ms, faster than 55.66% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 14 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.
def compareVersion(self, v1: str, v2: str) -> int:
    v1 = v1.split('.')
    v2 = v2.split('.')
    lv1 = len(v1)
    lv2 = len(v2)
    switch = 0

    # Make sure second version is longer if not then swap v1 and v2
    if lv1>lv2: 
        switch = 1
        v1,v2 = v2,v1
        lv1,lv2 = lv2,lv1
    
    # Iterate over longer version
    for i in range(lv2):

        # Take out revision number from v1 and v2
        # if i>=lv1 for revision 1 then use 0 instead
        r1 = 0 if i>=lv1 else int(v1[i])
        r2 = int(v2[i])

        # Compare revision numbers and return answer according to switch
        if switch:
            if r1>r2: return -1
            if r2>r1: return 1
        else:
            if r1>r2: return 1
            if r2>r1: return -1
    else:
        return 0