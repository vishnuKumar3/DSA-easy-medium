'''
https://leetcode.com/problems/sort-colors/description/
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        s,mid,e=0,0,n-1
        while(mid<=e):
            if(nums[mid]==1):
                mid+=1
            elif(nums[mid]==0):
                nums[s],nums[mid]=nums[mid],nums[s]
                s+=1
                mid+=1
            else:
                nums[mid],nums[e]=nums[e],nums[mid]
                e-=1

'''
Time complexity: O(n)
Space complexity: O(1)
'''


    
