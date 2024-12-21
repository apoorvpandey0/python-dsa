1. seen set
2. while loop to move pointer to next different element 
3. check last element if not same then append

def findUnion(self,a,b):
  i = 0
  j = 0
  ans = []
  while(i<len(a) and j<len(b)):
      if a[i] < b[j]:
      # Add to result if not the same as the last element
          if len(ans) == 0 or ans[-1] != a[i]:
              ans.append(a[i])
          i += 1
      elif a[i] == b[j]:
          # Add to result if not the same as the last element
          if len(ans) == 0 or ans[-1] != a[i]:
              ans.append(a[i])
          i += 1
          j += 1
      else:
          # Add to result if not the same as the last element
          if len(ans) == 0 or ans[-1] != b[j]:
              ans.append(b[j])
          j += 1
  # print(ans)
  if i<len(a):
      for p in range(i,len(a)):
          if len(ans)==0 or ans[-1]!=a[p]:
              ans.append(a[p])
  if j<len(b):
      for q in range(j,len(b)):
          if len(ans)==0 or ans[-1]!=b[q]:
              ans.append(b[q])
  return ans
