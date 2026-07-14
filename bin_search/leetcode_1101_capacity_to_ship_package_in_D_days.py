'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        def isPossible(num):
            s=0
            d=0
            i=0
            while(i<n):
                val=weights[i]
                s+=val
                if(s>=num):
                    if(s==num):
                        i+=1
                    s=0
                    d+=1
                else:
                    i+=1
            if(s>0 and s<=num):
                d+=1
            if(d<=days):
                return True
            else:
                return False
        
        divisions=n//days+1
        e=divisions*max(weights)
        s=max(weights)
        res=float("+inf")
        print(s,e)
        while(s<=e):
            mid=(s+e)//2
            if(isPossible(mid)):
                res=min(res,mid)
                e=mid-1
            else:
                s=mid+1
        return res
'''
Time complexity: O(log(s)*n) -> s=|max(weights)-len(weights)/days*max(weights)|
Space complexity: O(1)
'''
