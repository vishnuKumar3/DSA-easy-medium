'''
https://leetcode.com/problems/find-the-duplicate-number/description/
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        fast,slow=nums[0],nums[0]
        i=0
        while(True):
            if(slow==fast):
                if(i>0):
                    break
                else:
                    i=1
            slow=nums[slow]
            fast=nums[nums[fast]]

        fast=nums[0]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[fast]
        return fast

'''
Time complexity: O(n)
Space complexity: O(1)
'''
