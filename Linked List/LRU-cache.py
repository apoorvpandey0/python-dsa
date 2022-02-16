from collections import OrderedDict
"""
    LRU Cache - Least recently used cache
    Design and implement a data structure for Least Recently Used (LRU) cache
    Link: https://www.geeksforgeeks.org/lru-cache-implementation/
"""


# Runtime: 859 ms, faster than 84.24% of Python3 online submissions for LRU Cache.
# Memory Usage: 75.2 MB, less than 82.67% of Python3 online submissions for LRU Cache.
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:

        # If key is present in the dict then move it to the end of the dict and return the value
        if key in self.od:
            """
                Example:
                    Lets say we have ordered dict as [('a', 1), ('b', 2), ('c', 3)]
                    If we want to get value of 'b' then we will move it to the end of the dict and return the value
                    Why? Because b will be recently used key now
            """
            self.od.move_to_end(key)
            # print(self.od)
            return self.od[key]
        else:
            # print(self.od)
            return -1

    def put(self, key: int, value: int) -> None:

        if len(self.od) < self.size or key in self.od:

            # If key is present in the dict and there is space in dict then move it to the end of the dict and update the value
            if key in self.od:
                """
                    Example:
                        Lets say we have ordered dict as [('a', 1), ('b', 2), ('c', 3)]
                        If we want to update value of 'b' then we will move it to the end of the dict and update the value
                        Now the dict will be [('a', 1), ('c', 3), ('b', Updated value)]
                """
                self.od.move_to_end(key)
                self.od[key] = value

            # If key is not present in the dict and there is space in dict then add it to the end of the dict
            else:
                """
                    Example:
                        Lets say we have ordered dict as [('a', 1), ('b', 2)]
                        If we want to add key 'c' with value 3, since there is space in dict we will add it to the end of the dict
                        
                """
                self.od[key] = value

        # If there is no space in dict then we will remove the first element of the dict and add the new key and value
        else:
            """
                Example:
                    Lets say we have ordered dict as [('a', 1), ('b', 2)]
                    If we want to add key 'c' with value 3, since there is no space in dict we will remove the first element of the dict
                    Now the dict will be [('b', 2), ('c', 3)]
            """
            self.od.popitem(last=False)
            self.od[key] = value
        # print(self.od)


if __name__ == '__main__':
    pass
    # ["LRUCache","put","put","put","put","get","get"]
    # [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
    # [null,null,null,null,null,-1,3]
    # cache = LRUCache(2)
    # cache.put(2, 1)
    # cache.put(1, 1)
    # cache.put(2, 3)
    # cache.put(4, 1)
    # print(cache.get(1))
    # print(cache.get(2))

    # ["LRUCache","get","put","get","put","put","get","get"]
    # [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    # [null,-1,null,-1,null,null,2,6]

    # cache = LRUCache(2)
    # print(cache.get(2))
    # cache.put(2, 6)
    # print(cache.get(1))
    # cache.put(1, 5)
    # cache.put(1, 2)
    # print(cache.get(1))
    # print(cache.get(2))
