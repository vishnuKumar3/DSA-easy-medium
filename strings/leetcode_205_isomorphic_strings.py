'''
https://leetcode.com/problems/isomorphic-strings/description/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d,d2={},set()
        n=len(s)
        for i in range(0,n):
            v1,v2=s[i],t[i]
            if(d.get(v1)==None):
                d[v1]=v2
                if(v2 in d2):
                    return False
                d2.add(v2)
            else:
                if(d.get(v1)!=v2):
                    return False
        
        return True
'''
Time complexity: O(n)
Space complexity: O(256) -> 256 because there are 256 characters
'''
