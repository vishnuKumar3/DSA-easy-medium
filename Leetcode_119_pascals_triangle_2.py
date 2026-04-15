'''
https://leetcode.com/problems/pascals-triangle-ii/description/
Solution explantion: https://youtu.be/bR7mQgwQ_o8
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        res=[1]
        ans=1
        for i in range(1,rowIndex):   
            ans=ans*(rowIndex-i)
            ans=ans//i
            res.append(ans)
        
        return res

'''
Time complexity: O(n)
Space complexity: O(1) -> res variable is just used to store the result, if needed we can directly print values of the required row without res variable
'''
        
