from typing import List

class PTriangle1:
    # Runtime: 67 ms, faster than 5.03% of Python3 online submissions for Pascal's Triangle.
    # Memory Usage: 13.8 MB, less than 65.19% of Python3 online submissions for Pascal's Triangle.
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            tmp = [0]*(i+1)
            tmp[0] = tmp[-1] = 1
            for j in range(1,i):
                tmp[j] = ans[i-1][j]+ans[i-1][j-1]
            ans.append(tmp)
        return ans

class PascalsTriangleSolution1:
    """
        This builds up on last approach
        
        Runtime: 40 ms, faster than 60.17% of Python3 online submissions for Pascal's Triangle II.
        Memory Usage: 13.9 MB, less than 60.99% of Python3 online submissions for Pascal's Triangle II.
    """
    def getRow(self, numRows: int) -> List[int]:
        ans = [[1]]
        if numRows ==0:return ans[-1]
        for i in range(1,numRows+1):
            tmp = [0]*(i+1)
            tmp[0] = tmp[-1] = 1
            for j in range(1,i):
                tmp[j] = ans[i-1][j]+ans[i-1][j-1]
            ans.append(tmp)
        return ans[-1]
            
class AnotherSimilarSolution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1: return [[1]]
        elif numRows ==2: return [[1],[1,1]]
        ans = [[1],[1,1]]

        for _ in range(numRows-2):
            tmp = []
            for i in range(len(ans)-1):
                tmp.append(ans[-1][i]+ans[-1][i+1])
            tmp = [1] + tmp + [1]
            ans.append(tmp)
        return ans

class PascalsTriangleSoln2:
    """
        This soln removes the extra rows which are not needed
        since we're only interested in the last row so we keep only last and last second row at all times
        
        Runtime: 38 ms, faster than 67.29% of Python3 online submissions for Pascal's Triangle II.
        Memory Usage: 13.8 MB, less than 97.27% of Python3 online submissions for Pascal's Triangle II.
    """
    def getRow(self, rowIndex: int) -> List[int]:    
        if rowIndex ==0: return [1]
        elif rowIndex ==1: return [1,1]
        last = [1,1]
        for itr in range(1,rowIndex):
            tmp = [1]
            for i in range(itr):
                tmp.append(last[i]+last[i+1])
            tmp.append(1)
            last = tmp
        return last
            
