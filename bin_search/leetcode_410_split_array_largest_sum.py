'''
https://leetcode.com/problems/split-array-largest-sum/
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def isPossible(num):
            i=0
            s=0
            count=0
            while(i<n):
                val=nums[i]
                s+=val
                if(s>=num):
                    count+=1
                    if(s==num):
                        i+=1
                    s=0
                else:
                    i+=1
            if(s!=0 and s<=num):
                count+=1
            if(s>num):
                count+=2
            if(count<=k):
                return True
            else:
                return False

        s,e=max(nums),sum(nums)
        res=0
        while(s<=e):
            mid=(s+e)//2
            if(isPossible(mid)):
                res=mid
                e=mid-1
            else:
                s=mid+1
        
        return res
'''
Time complexity: O(log(sum(ar)-max(ar))*n)
Space complexity: O(1)
'''
