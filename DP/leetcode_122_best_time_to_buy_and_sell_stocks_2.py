'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev=prices[0]
        res=0
        for price in prices:
            if(price>prev):
                res+=price-prev
                prev=price
            else:
                prev=price
        return res
'''
Time complexity: O(n)
Space complexity: O(1)
'''
