'''
https://leetcode.com/problems/kth-missing-positive-number/
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missed=k-(arr[-1]-len(arr))
        if(missed>0):
            #If the missed items are beyond the end value of arr, add a new end value by adding total missed values
            end=missed+arr[-1]
            arr.append(end+1)
        n=len(arr)
        s,e=0,n-1
        ind=[0]
        while(s<=e):
            mid=(s+e)//2
            #find total number of missed values that are below the value that is at mid index
            val=arr[mid]
            values=mid+1
            missed=val-values
            if(missed>=k):
                ind[0]=mid
                e=mid-1
            else:
                s=mid+1
        prev=ind[0]-1
        if(prev==-1):
            return k
        else:
            val=arr[prev]
            values=prev+1
            missed=val-values            
            ret=(k-missed)+val
            return ret
'''
Time complexity: O(logn)
Space complexity: O(1)
'''
