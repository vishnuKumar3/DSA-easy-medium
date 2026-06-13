'''
https://leetcode.com/problems/longest-common-prefix/
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n1=len(strs[0])
        n2=len(strs[-1])
        res=""
        for i in range(0,n1):
            if(strs[0][i]==strs[-1][i]):
                res+=strs[0][i]
            else:
                break
        return res
'''
Time complexity: O(nlogn+m) -> m determines the length of common prefix
Space complexity: O(1)
'''
