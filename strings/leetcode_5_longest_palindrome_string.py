'''
https://leetcode.com/problems/longest-palindromic-substring/description/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        i=0
        res=0
        pal=[0,0]
        while(i<n):
            l,r=i-1,i+1
            total=1
            while(l>=0 and r<n):
                if(s[l]==s[r]):
                    total+=2
                else:
                    break
                l-=1
                r+=1
            if(total>res):
                res=total
                pal=[l+1,r-1]
            total=0
            l,r=i-1,i
            while(l>=0 and r<n):
                if(s[l]==s[r]):
                    total+=2
                else:
                    break
                l-=1
                r+=1
            if(total>res):
                res=total
                pal=[l+1,r-1]            
            i+=1 
        return s[pal[0]:pal[1]+1]

'''
Time complexity: O(n^2)
Space complexity: O(1)
'''
