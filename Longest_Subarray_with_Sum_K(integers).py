'''
Given an array arr[] containing integers and an integer k, 
your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. 
If there is no subarray with sum equal to k, return 0.

Test cases:
Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. 
The length of the longest subarray with a sum of 15 is 6.
'''

class Solution:
    def longestSubarray(self, arr, k):  
        d={0:-1}
        n=len(arr)
        i=0
        s=0
        res=0
        while(i<n):
            s+=arr[i]
            low=s-k
            if(d.get(low)!=None):
                res=max(res,i-d[low])
            if(d.get(s)==None):
                d[s]=i
            
            i+=1
        
        return res

'''
Time complexity: O(n)
Space complexity: O(n)
'''
