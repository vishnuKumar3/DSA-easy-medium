'''
https://leetcode.com/problems/4sum/
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(0,n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,n):
                if(j>i+1 and nums[j]==nums[j-1]):
                    continue
                k,l=j+1,n-1
                while(k<l):
                    if(nums[i]+nums[j]+nums[k]+nums[l]==target):
                        res.append([
                            nums[i],nums[j],nums[k],nums[l]
                        ])
                        k+=1
                        l-=1
                        while(k<l and nums[k]==nums[k-1]):
                            k+=1
                        while(l>k and nums[l]==nums[l+1]):
                            l-=1
                    elif(nums[i]+nums[j]+nums[k]+nums[l]>target):
                        l-=1
                    else:
                        k+=1
        return res

'''
Time complexity: O(n^3)
space complexity: O(1). We are ignoring the space used for result

'''

