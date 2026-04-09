'''
https://leetcode.com/problems/rotate-image/
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix)
        for i in range(0,m):
            for j in range(0,i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,m):
            j=0
            k=n-1
            while(j<=k):
                matrix[i][j],matrix[i][k]=matrix[i][k],matrix[i][j]
                j+=1
                k-=1
        
'''
Time complexity: O(mn)
Space comlexity: O(1)
'''
