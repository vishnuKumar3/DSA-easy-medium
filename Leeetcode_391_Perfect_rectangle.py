'''
https://leetcode.com/problems/perfect-rectangle/description/
'''
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x,y,a,b=float("+inf"),float("+inf"),float("-inf"),float("-inf")
        totalArea=0
        s=set()
        for rect in rectangles:
            x1,y1,a1,b1=rect
            x=min(x,x1)
            y=min(y,y1)
            a=max(a,a1)
            b=max(b,b1)
            totalArea+=(a1-x1)*(b1-y1)
            if((x1,y1) in s):
                s.discard((x1,y1))
            else:
                s.add((x1,y1))
            if((a1,b1) in s):
                s.discard((a1,b1))
            else:
                s.add((a1,b1))
            if((x1,b1) in s):
                s.discard((x1,b1))
            else:
                s.add((x1,b1))
            if((a1,y1) in s):
                s.discard((a1,y1))
            else:
                s.add((a1,y1))

        overallArea=(a-x)*(b-y)
        if(overallArea!=totalArea):
            return False
        if(len(s)!=4 or (x,y) not in s or (a,b) not in s or (x,b) not in s or (a,y) not in s):
            return False
        return True

  '''
  Time complexity: O(n)
  space complexity: O(n)
  '''
