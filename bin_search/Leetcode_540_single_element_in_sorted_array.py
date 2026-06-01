'''
https://leetcode.com/problems/single-element-in-a-sorted-array/description/
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        def findEnd(ind):
            val=nums[ind]
            left=-1 if(ind==0) else ind-1
            if(left!=-1):
                if(nums[left]==val):
                    return ind
            right=-1 if(ind==n-1) else ind+1
            if(right!=-1):
                if(nums[right]==val):
                    return right
            return -1

        def binSearch(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            end=findEnd(mid)
            if(end==-1):
                return nums[mid]
            if((end+1)%2==0):
                return binSearch(mid+1,e)
            else:
                return binSearch(s,mid-1)
        
        ret=binSearch(0,n-1)
        return ret

  '''
  Time complexity: O(logn)
  Space complexity: O(1)
  '''
