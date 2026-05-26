'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        def binSearch(s,e):
            if(s>e):
                return -1
            mid=(s+e)//2
            if(nums[mid]==target):
                return True
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
        
        e=n-1
        if(nums[0]==nums[n-1]):
            j=n-1
            while(j>0):
                if(nums[j]==nums[0]):
                    j-=1
                else:
                    break
            e=j
        ret=binSearch(0,e)
        return True if(ret!=-1) else False

'''
Time complexity: O(logn) best case, O(n) worst case
Space complexity: O(1)
We'll get worst case when there are same values on both left and right sides. For ex: [2,2,0,2,2,2,2], here 2 is on both sides
We are using this condition nums[s]<=nums[mid] to check whether left half is sorted or not, but if we compare for the worst case,
if we get s as 0 and mid as 4, then nums[s]<=nums[mid] will fail its main objective of checking whether left half is sorted or not. That's why we have removed 
the equal values that are on the right side which are equal to the value which is in index 0.
'''
