https://www.youtube.com/watch?v=KtpqeN0Goro&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=3
find maximum sum of all subarrays of nums of a fixed size 

Core
1. Add j to currSum always
2. Once we hit window size then maintain it

def forloopimpl():
    nums = [2,5,1,8,2,9,1]
    size = 3
    
    i = 0
    j = 0
    
    curSize = 0
    currSum = 0
    ans = 0
    
    for j in range(len(nums)):
      print(i,j,currSum)
      
      currSum += nums[j]
          
      if j - i + 1 == 3:
          ans = max(ans,currSum)
          currSum -= nums[i]
          i+=1
    
    print(ans)
