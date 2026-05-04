'''
https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/
'''
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        def binSearch(s,e,target):
            ans=n
            while(s<=e):
                mid=(s+e)//2
                if(nums[mid]<target):
                    s=mid+1
                else:
                    ans=mid
                    e=mid-1
            return ans
        
        nums.sort()
        n=len(nums)
        pre=[]
        s=0
        for i in nums:
            s+=i
            pre.append(s)
        res=[]
        for i in queries:
            target=i
            pivot=binSearch(0,n-1, target) 
            low=pre[pivot-1] if(pivot>0) else 0
            count1=abs(pivot*target-low)
            count2=abs(pre[n-1]-low-((n-pivot)*target))
            count=count1+count2
            res.append(count)
        return res

'''
Time complexity: O((n+m)logn)
Space complexity: O(n)
'''


