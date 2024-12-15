https://www.geeksforgeeks.org/problems/row-with-max-1s0023


===================================== Soln 1 ===========================================

O( N LOG N ) solution | 0( 1 ) 

Go to each row calculate number of ones and update answer based on that
Correct soln but Memory limit exceeded on gfg

class Solution:
    def rowWithMax1s(self, arr):
        
        ans = float('inf')
        max1 = 0
        
        for r in range(len(arr)):
        
            lo = 0
            hi = len(arr[r]) -1
        
            while lo<=hi:
                mid = (lo+hi)//2
                if arr[r][mid] == 1: hi = mid - 1
                else: lo = mid + 1
        
            tmp = len(arr[r]) - lo
        
            if tmp>max1:
                max1 = tmp
                ans = r
        
        return ans



==================================== Soln 2 ============================================
GFG par same python code accept nahi hota - bekar platform issues islie JAVA code

Time O ( R + C ) | space O( 1 )

Mudde ka point: col variable is running the full length of a row only once!
It stops at max 1 col index and starts further if a row with even mmore 1s comes along
class Solution {
    public int rowWithMax1s(int arr[][]) {
        int ans = 0;
        
        int col = arr[0].length - 1;
        
        for(int r = 0; r<arr.length; r++){
            
            while( col>=0 && arr[r][col] == 1 ){
                col-=1;
                ans = r;
            }
        }
        return ans;
    }
}
