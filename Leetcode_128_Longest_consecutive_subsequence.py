'''
https://leetcode.com/problems/longest-consecutive-sequence/
'''
#Approach-1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        s=set()
        res=0
        for i in nums:
            s.add(i)
        for i in s:
            if(i-1 not in s):
                l=1
                st=i
                while(st+1 in s):
                    l+=1
                    st+=1
                res=max(res, l)
        
        return res
'''
Time complexity: O(n)
Space complexity: O(n)
'''
#Approach-2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for i in nums:
            d[i]=1
        dp={}
        def fun(val):
            if(d.get(val)==None):
                return 0
            elif(dp.get(val)!=None):
                return dp[val]
            else:
                ret=1+fun(val+1)
                dp[val]=ret
                return ret
        
        res=0
        for i in nums:
            res=max(res, fun(i))
        
        return res
'''
Time complexity: O(n)
Space complexity: O(2n) -> O(n)
'''

