'''
https://leetcode.com/problems/reverse-pairs/
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[0]

        def countPairs(ar,s,mid,e):
            temp=mid+1
            s1=s
            while(s1<=mid):
                while(temp<=e and ar[s1]>2*ar[temp]):
                    temp+=1
                ans[0]=ans[0]+temp-(mid+1)
                s1+=1

        def divide(ar,s,e):
            if(s<e):
                mid=(s+e)//2
                divide(ar,s,mid)
                divide(ar,mid+1,e)
                countPairs(ar,s,mid,e)
                mergesort(ar,s,mid,e)
        
        def mergesort(ar,s,mid,e):
            temp=[]
            l1,r1=s,mid+1
            l2=s
        
            while(l1<=mid and r1<=e):
                if(ar[l1]<=ar[r1]):           
                    temp.append(ar[l1])
                    l1+=1
                else:
                    temp.append(ar[r1])
                    r1+=1
            while(l1<=mid):
                temp.append(ar[l1])
                l1+=1
            while(r1<=e):
                temp.append(ar[r1])
                r1+=1
            s1=s
            while(s<=e):
                ar[s]=temp[s-s1]
                s+=1
            
        divide(nums,0,n-1)
        return ans[0]
'''
Time complexity: O(nlogn)
Space complexity: O(n)
'''
