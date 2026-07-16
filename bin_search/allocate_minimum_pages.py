'''
https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
https://takeuforward.org/data-structure/allocate-minimum-number-of-pages
'''
class Solution:
    def findPages(self, arr, k):
        # code here
        n=len(arr)
        if(n<k):
            return -1
        s,e=max(arr),sum(arr)
        def isPossible(num):
            prev=0
            s=0
            count=0
            while(prev<n):
                val=arr[prev]
                s+=val
                if(s<=num):
                    prev+=1
                else:
                    count+=1
                    s=0
            if(s!=0 and s<=num):
                count+=1
            return count<=k
                    
        
        res=[0]
        while(s<=e):
            mid=(s+e)//2
            if(isPossible(mid)):
                res[0]=mid
                e=mid-1
            else:
                s=mid+1
            
        return res[0]
'''
Time complexity: O(n*log(sum(ar)-max(ar))
Space complexity: O(1)
'''
