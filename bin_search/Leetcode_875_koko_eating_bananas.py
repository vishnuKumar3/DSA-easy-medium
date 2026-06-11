'''
https://leetcode.com/problems/koko-eating-bananas/
'''
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        maxTotal=0
        for i in piles:
            maxTotal=max(maxTotal,i) #here we are considering maxSpeed as the max count of bananas in all piles because in one hour koko will eat bananas only from one pile. That's why the limit cannot be crossed
        s,e=1,maxTotal
        def isPossible(speed):
            time=0
            for i in piles:
                time+=math.ceil(i/speed)
                if(time>h):
                    return False
            return True
    
        res=e
        while(s<=e):
            mid=(s+e)//2
            if(isPossible(mid)):
                res=min(res,mid)
                e=mid-1
            else:
                s=mid+1
        return res

'''
Time complexity: O(nlog(max(piles)))
Space complexity: O(1)
'''
