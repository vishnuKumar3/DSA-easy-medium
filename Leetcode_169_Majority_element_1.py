'''
https://leetcode.com/problems/majority-element/
We can solve this problem using hash data structure too in an easy way
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count,val=0,None
        for i in nums:
            if(count==0):
                val=i
            if(i==val):
                count+=1
            else:
                count-=1
        return val

'''
Time complexity: O(n)
Space complexity: O(1)
'''

