'''
https://leetcode.com/problems/count-good-numbers/
'''
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        const=10**9+7
        def power(x,n):
            if(n==0):
                return 1
            else:
                if(n%2==0):
                    return power((x*x)%const,n//2)
                else:
                    return (x*power(x,n-1))%(const)

        even=math.ceil(n/2)
        odd=n-even
        res=power(5,even)*power(4,odd)
        res=res%(const)
        return int(res)
'''
Time complexity: O(logn)
Space complexity: O(1)
'''
