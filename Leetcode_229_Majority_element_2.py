'''
https://leetcode.com/problems/majority-element-ii/
This problem's solution is similar to majority element-1 with slight modification
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1,cnt2,el1,el2=0,0,0,0
        for i in range(0,n):
            val=nums[i]
            if(cnt1==0 and val!=el2):
                el1=val
                cnt1=1
            elif(cnt2==0 and val!=el1):
                el2=val
                cnt2=1
            elif(val==el1):
                cnt1+=1
            elif(val==el2):
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1,cnt2=0,0
        res=[]
        for i in range(0,n):
            val=nums[i]
            if(val==el1):
                cnt1+=1
            elif(val==el2):
                cnt2+=1
        constant=n//3
        if(cnt1>constant):
            res.append(el1)
        if(cnt2>constant):
            res.append(el2)
        return res

'''
Time complexity: O(n)
Space complexity: O(1)
'''
