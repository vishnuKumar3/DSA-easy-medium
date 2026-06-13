'''
https://leetcode.com/problems/remove-outermost-parentheses/
'''
from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        q=deque()
        points=set([0])
        i=0
        n=len(s)
        for j in range(0,n):
            i=s[j]
            if(i=="("):
                q.append(i)
            else:
                q.pop()
            if(len(q)==0):
                points.add(j)
                points.add(j+1)
        res=""
        for i in range(0,n):
            if(i in points):
                continue
            val=s[i]
            res+=val
        return res

'''
Time complexity: O(n)
Space complexity: O(n)
'''
        
