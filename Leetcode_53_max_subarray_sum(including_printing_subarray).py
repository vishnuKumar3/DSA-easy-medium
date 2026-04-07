'''
https://leetcode.com/problems/maximum-subarray/description/
'''
def extendedKadane(nums):
  n=len(nums)
  res=[-1,-1]
  start=0
  s=0
  i=0
  large=float("-inf")
  while(i<n):
    val=nums[i]
    s+=val
    if(s>large):
      large=s 
      res=[start,i]

    if(s<=0):
      start=i+1
    print(i,res)
    i+=1
    
  print(res)

ar=[1,2,-3,5,6,-1,8,2,-5]
extendedKadane(ar)

'''
Time complexity: O(n)
Space complexity: O(n)
'''
