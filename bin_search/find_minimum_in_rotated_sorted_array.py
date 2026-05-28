'''
https://takeuforward.org/data-structure/minimum-in-rotated-sorted-array
'''
#solution - 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        res=[float("+inf")]
        def findMin(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            if(nums[s]<=nums[mid]):
                res[0]=min(res[0],nums[s])
                return findMin(mid+1,e)
            else:
                res[0]=min(res[0],nums[mid])
                return findMin(s,mid-1)
        
        findMin(0,n-1)
        return res[0]

        ret=findMin(0,n-1)
        return nums[ret]

#solution - 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        def findMin(s,e):
            if(s>e):
                return 0
            mid=(s+e)//2
            if(mid>0):
                if(nums[mid]<nums[mid-1]):
                    return mid
            if(nums[mid]>=nums[s] and nums[mid]>nums[e]):
                return findMin(mid+1,e)
            else:
                return findMin(s,mid-1)

        ret=findMin(0,n-1)
        return nums[ret]

'''
Time complexity: O(logn)
Space complexity: O(1)
'''
