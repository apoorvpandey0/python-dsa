"""
 6 OCT
 https://leetcode.com/problems/time-based-key-value-store/submissions/
"""

from collections import defaultdict,OrderedDict
class TimeMap:
    # Runtime: 1708 ms, faster than 31.17% of Python3 online submissions for Time Based Key-Value Store.
    # Memory Usage: 69.9 MB, less than 90.76% of Python3 online submissions for Time Based Key-Value Store.
    def __init__(self):
        self.store = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: str) -> None:
        self.store[key][timestamp] = value
        # print(self.store)
        

    def get(self, key: str, timestamp: int) -> str:
        # print(self.store[key].items())
        if timestamp in self.store[key]: return self.store[key][timestamp]
        
        for i in range(timestamp,-1,-1):
            if i in self.store[key]: return self.store[key][i]
        return ""
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)