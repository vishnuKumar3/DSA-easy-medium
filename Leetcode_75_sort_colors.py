'''
https://leetcode.com/problems/sort-colors/description/
Easy trick to solve this problem
1. Consider three variables ones, twos and threes
2. count respective numbers and store in respective variable by traversing through the array
3. Now go through the array and fill the give array as per the count of each value
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


    
