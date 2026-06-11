'''
https://leetcode.com/problems/find-peak-element/description/
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1): 
            return 0
        elif(nums[0]>nums[1]):
            return 0
        elif(nums[n-1]>nums[n-2]):
            return n-1
        s,e=1,n-2
        while(s<=e):
            mid=(s+e)//2
            if(nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]):
                return mid
            elif(nums[mid]>nums[mid+1]):
                e=mid-1
            elif(nums[mid]>nums[mid-1]):
                s=mid+1
            else:
                e=mid-1
'''
Time complexity: O(n)
Space complexity: O(1)
'''
        
