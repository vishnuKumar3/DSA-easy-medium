'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        i=n-1
        large=float("-inf")
        res=0
        while(i>=0):
            val=prices[i]
            large=max(large,val)
            diff=large-val
            res=max(res, diff)
            i-=1
        return res

'''
Time complexity: O(n)
Space complexity: O(1)
'''
