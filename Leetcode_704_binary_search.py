'''
https://leetcode.com/problems/binary-search/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            if(nums[mid]==target):
                return mid
            elif(target>=nums[mid]):
                return bin(mid+1,e)
            else:
                return bin(s,mid-1)

        n=len(nums)
        return bin(0,n-1)
'''
Time complexity: O(logn)
Space complexity: O(1)
'''
