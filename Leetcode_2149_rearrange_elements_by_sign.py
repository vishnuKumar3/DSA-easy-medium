'''
https://leetcode.com/problems/rearrange-array-elements-by-sign/
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p,neg=0,0
        i=0
        res=[]
        while(i<n):
            if(i%2==0):
                while(p<n):
                    if(nums[p]>=0):
                        res.append(nums[p])           
                        p+=1
                        break
                    p+=1
            else:
                while(neg<n):
                    if(nums[neg]<0):
                        res.append(nums[neg])
                        neg+=1
                        break
                    neg+=1
            i+=1
        return res

'''  
Time complexity: O(n)
Space complexity: O(n)
'''
