'''
https://takeuforward.org/plus/dsa/problems/find-square-root-of-a-number?source=strivers-a2z-dsa-track
'''
class Solution:
    def floorSqrt(self, n: int) -> int:
        s,e=1,n
        res=1
        while(s<=e):
            mid=(s+e)//2
            power=mid*mid
            if(power<=n):
                s=mid+1
                res=max(res,mid)
            else:
                e=mid-1
        return res

'''
Time complexity: O(logn)
Space complexity: O(1)
'''
