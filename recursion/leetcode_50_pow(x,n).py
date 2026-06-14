'''
https://leetcode.com/problems/powx-n/
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        n1=n
        if(n<0):
            n1=-1*n
        def solve(x,n):
            if(n==0):
                return 1
            else:
                if(n%2==0):
                    return solve(x*x,n//2)
                else:
                    return x*solve(x,n-1)
        ret=solve(x,n1)
        if(n<0):
            return 1/ret
        return ret
'''
Time complexity: O(logn)
Space complexity: O(1)
'''
