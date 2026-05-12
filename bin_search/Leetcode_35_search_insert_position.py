'''
https://leetcode.com/problems/search-insert-position/
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s,e=0,n-1
        ans=n
        while(s<=e):
            mid=(s+e)//2
            if(nums[mid]>=target):
                ans=mid
                e=mid-1
            else:
                s=mid+1
        
        return ans
'''
Time complexity: O(logn)
Space complexity: O(1)
'''
