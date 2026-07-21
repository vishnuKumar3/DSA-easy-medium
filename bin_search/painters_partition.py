'''
https://takeuforward.org/plus/dsa/problems/painters-partition?source=strivers-a2z-dsa-track
'''
class Solution:
    def paint(self, A: int, B: int, C: list[int]) -> int:
        n=len(C)
        def isPossible(num):
            count=0
            s=0
            i=0
            while(i<n):
                val=C[i]
                s+=val
                if(s>=num):
                    if(s==num):
                        i+=1
                    count+=1
                    s=0
                else:
                    i+=1
            if(s!=0):
                if(s<=num):
                    count+=1
                else:
                    count+=2
            return count<=A
        
        s,e=max(C),sum(C)
        res=0
        while(s<=e):
            mid=(s+e)//2
            if(isPossible(mid)):
                res=mid
                e=mid-1
            else:
                s=mid+1
        return res*B
'''
Time complexity: O(log(sum(ar)-max(ar))*n)
Space complexity: O(1)
'''


