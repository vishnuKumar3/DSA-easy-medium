'''
https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
'''
class Solution:
    def minMaxDist(self, stations, k):
        n=len(stations)
        def isPossible(distance):
            i=1
            ret=0
            while(i<n):
                gap=stations[i]-stations[i-1]
                total=int(gap/distance)
                if(gap%distance==0):
                    total-=1
                ret+=total
                i+=1
            if(ret<=k):
                return True
            else:
                return False
        
        s=0
        e=0
        for i in range(1,n):
           e=max(e,stations[i]-stations[i-1]) 
        large=10**-6
        while(e-s>large):
            mid=(s+e)/2
            if(isPossible(mid)):
                e=mid
            else:
                s=mid
        return e
'''
Time complexity: O(n*log(maxDistance-10**-6))
Space compleity: O(1)
'''

            
                
                
