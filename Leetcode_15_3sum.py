'''
https://leetcode.com/problems/3sum/
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(0,n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1
            while(j<k):
                if(nums[i]+nums[j]+nums[k]==0):
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(k>j and nums[k]==nums[k+1]):
                        k-=1
                elif(nums[i]+nums[j]+nums[k]>0):
                    k-=1
                else:
                    j+=1
        return res

'''
Time complexity: O(nlogn)
Space complexity: O(1), we are ignoring the space that we are using for storing result
'''
