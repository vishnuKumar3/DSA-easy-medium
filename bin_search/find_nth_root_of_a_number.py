'''
https://takeuforward.org/plus/dsa/problems/find-nth-root-of-a-number?source=strivers-a2z-dsa-track
'''
class Solution:
    def NthRoot(self, n, m):
        s,e=1,m
        while(s<=e):
            mid=(s+e)//2
            ans=1
            i=1
            #we are calculating the power manually because the value may overflow and also we'll stop the product operation if the product exceeds m
            while(i<=n):
                ans*=mid
                if(ans>m):
                    break
                i+=1
        
            if(ans==m):
                return mid
            if(ans>m):
                e=mid-1
            else:
                s=mid+1 
    
        return -1

'''
Time complexity: O(logm)
Space complexity: O(1)
'''
