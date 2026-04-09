'''
https://leetcode.com/problems/next-permutation/
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        def reverse(i,j):
            while(i<=j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

        def findDescendingBreakPoint():
            res=-1
            i=n-2
            while(i>=0):
                if(nums[i]<nums[i+1]):
                    res=i
                    break
                i-=1
            return res

        if(n==1):
            return nums
        breakPoint = findDescendingBreakPoint()
        if(breakPoint==-1):
            reverse(0,n-1)
            return nums
        else:
            nextGreater=None
            i=n-1
            while(i>=breakPoint):
                if(nums[i]>nums[breakPoint]):
                    nextGreater=i
                    break
                i-=1
            nums[nextGreater],nums[breakPoint]=nums[breakPoint],nums[nextGreater]
            reverse(breakPoint+1,n-1)
            return nums

'''
Time complexity: O(n)
Space complexity: O(1)
'''
