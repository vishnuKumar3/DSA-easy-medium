class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def fun(val):
            return val[0]

        n=len(nums)
        for i in range(0,n):
            nums[i]=[nums[i],i]
        l,r=0,n-1
        nums.sort(key=fun)
        while(l<r):
            s=nums[l][0]+nums[r][0]
            if(s>target):
                r-=1
            else:
                if(s==target):
                    return [nums[l][1],nums[r][1]]
                l+=1
        

'''
Time complexity: O(nlogn)
Space complexity: O(1)
'''
