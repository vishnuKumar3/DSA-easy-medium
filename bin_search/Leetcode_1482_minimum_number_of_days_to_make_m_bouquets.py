'''
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
'''
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        def isValid(num):
            count,bok=0,0
            for i in range(0,n):
                val=bloomDay[i]
                if(val>num):
                    count=0
                else:
                    count+=1
                    if(count>=k):
                        bok+=1
                        count=0
                    if(bok>=m):
                        return True
            return False

        s,e=min(bloomDay),max(bloomDay)
        res=float("+inf")
        while(s<=e):
            mid=(s+e)//2
            ret=isValid(mid)
            print(mid,ret)
            if(ret):
                res=min(res,mid)
                e=mid-1
            else:
                s=mid+1

        if(res==float("+inf")):
            return -1
        return res
'''
Space complexity: O(1)
Time complexity: O(n*log(max(bloomDay)-min(bloomDay)+1))
'''
