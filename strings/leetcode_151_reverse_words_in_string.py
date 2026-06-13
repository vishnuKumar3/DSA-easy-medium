'''
https://leetcode.com/problems/reverse-words-in-a-string/description/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        i=n-1
        end=n-1
        res=""
        while(i>=0):
            if(s[i]==" "):
                i-=1
                end=i
                continue
            while(i>=0 and s[i]!=" "):
                i-=1
            j=i+1
            if(res==""):
                res+=s[j:end+1]
            else:
                res+=" "+s[j:end+1]
        return res
'''
Time complexity: O(n)
Space complexity: O(1)
'''
