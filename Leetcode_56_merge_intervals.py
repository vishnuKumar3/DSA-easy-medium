'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def fun(val):
            return val[0]
        intervals.sort(key=fun)
        res=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            ret=res[-1]
            current=intervals[i]
            if(current[0]<=ret[1]):
                ret[1]=max(current[1],ret[1])
                res[-1]=ret
            else:
                res.append(current)
        return res
'''
Time complexity: O(nlogn)
Space complexity: O(n) 
'''
