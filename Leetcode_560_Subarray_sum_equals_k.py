'''
https://leetcode.com/problems/subarray-sum-equals-k/
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        s=0
        i=0
        d={0:1}
        while(i<n):
            val=nums[i]
            s+=val
            if(d.get(s-k)!=None):
                count+=d[s-k]
            if(d.get(s)==None):
                d[s]=1
            else:
                d[s]+=1
            i+=1

        return count

'''
Time complexity: O(n)
Space complexity: O(n)
'''
