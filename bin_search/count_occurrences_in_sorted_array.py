'''
https://takeuforward.org/data-structure/count-occurrences-in-sorted-array
'''

def fun(nums, x):
    n=len(nums)
    s,e=0,n-1
    floor,ceil=-1,-1 #if there is no ceil and floor, then we are returning -1 as the value
    while(s<=e):
        mid=(s+e)//2
        if(nums[mid]>x):
            ceil=mid
            e=mid-1
        else:
            s=mid+1
    
    s,e=0,n-1
    while(s<=e):
        mid=(s+e)//2
        if(nums[mid]<x):
            floor=mid
            s=mid+1
        else:
            e=mid-1    
    
    if(ceil==-1 or floor==-1):
        print(0)
    else:
        print((ceil-floor)-1)
  

fun([3,4,4,5,7,8,8,10],5)
fun([3,4,4,7,8,8,10], 8)
fun([1,2,3,4],5)

'''
Time complexity: O(logn)
Space complexity: O(1)
'''
