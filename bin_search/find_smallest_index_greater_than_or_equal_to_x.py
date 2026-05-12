'''
https://takeuforward.org/plus/dsa/problems/lower-bound-?source=strivers-a2z-dsa-track
'''
class Solution:
    def lowerBound(self, nums, x):
        s,e=0,n-1
        ans=n-1
        while(s<=e):
            mid=(s+e)//2
            if(nums[mid]>=x):
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
            
'''
Time complexity: O(logn)
Space complexity: O(1)
'''

