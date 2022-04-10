"""
    Find the town judge
    
    Desc: If the town judge exists, then:
            The town judge trusts nobody.
            Everybody (except for the town judge) trusts the town judge.
            There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

    Link: https://leetcode.com/problems/find-the-town-judge/
"""


from typing import List


class Solution:
    # Runtime: 764 ms, faster than 89.61% submissions.
    # Memory Usage: 18.9 MB, less than 93.83% submissions.
    def findJudge(self, n: int, edges: List[List[int]]) -> int:
        

        # arr[0] is the array of number of people i trusts
        # arr[1] is the array of number of people who trust i
        arr = [
            [0]*(n+1),
            [0]*(n+1)
        ]
        
        for v1,v2 in edges:
            arr[0][v1]+=1
            arr[1][v2]+=1

        # Judge is a person who trusts no one i.e in arr[0] i should be 0
        # And is trusted by rest of the people (N-1 people) i.e. in arr[1] i should be N-1
        for i in range(1,n+1):
            if arr[0][i] == 0 and arr[1][i]==n-1:
                return i
        else:
            return -1