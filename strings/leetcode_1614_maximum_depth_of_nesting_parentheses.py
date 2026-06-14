'''
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
'''
class Solution:
    def maxDepth(self, s: str) -> int:
        n=len(s)
        val=0
        res=0
        for j in range(0,n):
            i=s[j]
            if(i=="("):
                val+=1
            elif(i==")"):
                val-=1
            res=max(res,val)
        
        return res
'''
Time complexity: O(n)
Space complexity: O(1)
'''
            
            
