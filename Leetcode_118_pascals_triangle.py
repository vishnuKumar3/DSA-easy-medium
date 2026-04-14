'''
https://leetcode.com/problems/pascals-triangle/
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        res=[[1]]
        i=2
        prevLength=1
        while(i<=n):
            curLength=1
            row=[1]
            prev=res[-1]
            if(prevLength>=2):
                j=1
                while(j<prevLength):
                    curLength+=1
                    row.append(prev[j]+prev[j-1])
                    j+=1 

            row.append(1)
            curLength+=1
            prevLength=curLength
            res.append(row)
            i+=1
        return res

'''
Time complexity: O(n^2)
Space complexity: O(n^2)
'''

            
