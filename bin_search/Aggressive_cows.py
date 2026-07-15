'''
https://takeuforward.org/plus/dsa/problems/aggressive-cows?source=strivers-a2z-dsa-track
'''
class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        n=len(arr)
        arr.sort()
        s,e=0,arr[-1]-arr[0]
        def isPossible(distance):
            prev=0
            s1,e1=0,n-1
            total=1
            while(s1<=e1):
                val=arr[s1]
                if(val-arr[prev]>=distance):
                    total+=1
                    prev=s1
                s1+=1
            return total>=k
        
        ret=0
        while(s<=e):
            mid=(s+e)//2
            if(isPossible(mid)):
                ret=mid
                s=mid+1
            else:
                e=mid-1
        return ret

  '''
  Time complexity: O(logN+(N*log(max(arr)-min(arr))))
  Space complexity: O(1)
  '''
