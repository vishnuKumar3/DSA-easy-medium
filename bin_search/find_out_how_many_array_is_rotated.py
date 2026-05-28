'''
https://takeuforward.org/arrays/find-out-how-many-times-the-array-has-been-rotated
'''

class Solution:
    def findKRotation(self, nums):
        n=len(nums)
        res=[float("+inf")]
        ind=[0]
        def findRotations(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            if(nums[s]<=nums[mid]):
                if(nums[s]<res[0]):
                    res[0]=nums[s]
                    ind[0]=s
                return findRotations(mid+1,e)
            else:
                if(nums[mid]<res[0]):
                    res[0]=nums[mid]
                    ind[0]=mid
                return findRotations(s,mid-1)
        findRotations(0,n-1)
        return ind[0]             

'''
Time complexity: O(logn)
Space complexity: O(1)
'''

