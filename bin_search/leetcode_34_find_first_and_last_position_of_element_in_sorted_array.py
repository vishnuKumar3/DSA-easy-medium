'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        begin,end=-1,-1
        def findStart(s,e):
            ans=-1
            while(s<=e):
                mid=(s+e)//2
                if(nums[mid]<target):
                    ans=mid
                    s=mid+1
                else:
                    e=mid-1
            return ans

        def findEnd(s,e):
            ans=n
            while(s<=e):
                mid=(s+e)//2
                if(nums[mid]>target):
                    ans=mid
                    e=mid-1
                else:
                    s=mid+1
            return ans

        st=findStart(0,n-1)
        end=findEnd(0,n-1)
        if(st==-1 or end==-1):
            return [-1,-1]
        return [st+1,end-1]

'''
Time complexity: O(logn)
Space complexity: O(1)
'''
        
