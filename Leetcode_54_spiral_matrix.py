'''
https://leetcode.com/problems/spiral-matrix/
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        constant=101
        i=0
        x,y=0,-1
        while(True):
            direction=directions[i]
            x1,y1=x+direction[0],y+direction[1]
            if(x1<0 or x1>=m or y1<0 or y1>=n or matrix[x1][y1]==constant):
                i=(i+1)%4
                direction=directions[i]
            x1,y1=x+direction[0],y+direction[1]
            if(x1<0 or x1>=m or y1<0 or y1>=n or matrix[x1][y1]==constant):
                break
            x,y=x+direction[0],y+direction[1]
            res.append(matrix[x][y])
            matrix[x][y]=constant
        
        return res
        
'''
Time complexity: O(m*n)
Space complexity: O(1)
'''
