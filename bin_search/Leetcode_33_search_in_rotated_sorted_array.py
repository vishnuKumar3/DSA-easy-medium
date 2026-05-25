'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''

#Approach - 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def findOrigin(s,e):
            if(s>e):
                return 0
            mid=(s+e)//2
            if(mid>0):
                if(nums[mid-1]>nums[mid]):
                    return mid
                
            if(nums[s]<=nums[mid] and nums[e]<nums[mid]):
                return findOrigin(mid+1,e)
            else:
                return findOrigin(s,mid-1)
        
        def binSearch(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            if(nums[mid]==target):
                return mid
            if(target>nums[mid]):
                return binSearch(mid+1,e)
            else:
                return binSearch(s,mid-1)
        
        origin=findOrigin(0,n-1)
        if(target>=nums[origin] and target<=nums[n-1]):
            return binSearch(origin,n-1)
        else:
            return binSearch(0,origin-1)

#Approach - 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def binSearch(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            if(nums[mid]==target):
                return mid
            if(nums[s]<=nums[mid]):
                if(nums[s]<=target<nums[mid]):
                    return binSearch(s,mid-1)
                else:
                    return binSearch(mid+1,e)
            else:
                if(nums[mid]<target<=nums[e]):
                    return binSearch(mid+1,e)
                else:
                    return binSearch(s,mid-1)
        
        return binSearch(0,n-1)

'''
Time complexity:O(logn)
Space complexity: O(1)
'''


