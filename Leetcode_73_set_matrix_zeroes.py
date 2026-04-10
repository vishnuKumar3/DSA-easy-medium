'''
https://leetcode.com/problems/set-matrix-zeroes/description/
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        rowZero,colZero=0,0
        for i in range(0,m):
            for j in range(0,n):
                if(matrix[i][j]==0):
                    if(i==0):
                        rowZero=1
                    if(j==0):
                        colZero=1
                    matrix[i][0]=0
                    matrix[0][j]=0
        print(matrix)
        for i in range(1,m):
            if(matrix[i][0]==0):
                for j in range(0,n):
                    matrix[i][j]=0
        
        for j in range(1,n):
            if(matrix[0][j]==0):
                for i in range(0,m):
                    matrix[i][j]=0
        if(rowZero==1):
            for j in range(0,n):
                matrix[0][j]=0
        if(colZero==1):
            for i in range(0,m):
                matrix[i][0]=0


'''
Time complexity: O(m*n)
Space complexity: O(1)
'''
