'''
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
'''
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isPossible(num):
            s=0
            for i in nums:
                s+=math.ceil(i/num)
            if(s<=threshold):
                return True
            return False
        
        res=[float("+inf")]
        def solve(s,e):
            if(s>e):
                return
            mid=(s+e)//2
            ret=isPossible(mid)
            if(ret):
                res[0]=min(res[0],mid)
                return solve(s,mid-1)
            else:
                return solve(mid+1,e)
        solve(1,max(nums))
        return res[0]

'''
Time complexity: O(n*log(max(nums)))
Space complexity: O(1)
'''
            
