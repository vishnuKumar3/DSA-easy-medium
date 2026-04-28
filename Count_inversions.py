'''
https://takeuforward.org/data-structure/count-inversions-in-an-array
'''
#used merge sort to calculate inversions
count=[0]
def countInversions(ar,s,mid,e):
  temp=[]
  l,r=s,mid+1
  while(l<=mid and r<=e):
    if(ar[l]<=ar[r]):
      temp.append(ar[l])
      l+=1
    else:
      temp.append(ar[r])
      count[0]=count[0]+mid-l+1
      r+=1
  while(l<=mid):
    temp.append(ar[l])
    l+=1
  
  while(r<=e):
    temp.append(ar[r])
    r+=1
  
  st=s
  while(s<=e):
    ar[s]=temp[s-st]
    s+=1
  

def divide(ar,s,e):
  if(s<e):
    mid=(s+e)//2
    divide(ar,s,mid)
    divide(ar,mid+1,e)
    countInversions(ar,s,mid,e)
    

divide([5,3,2,1,4],0,4)
print(count[0])
count=[0]
divide([5,4,3,2,1],0,4)
print(count[0])
count=[0]
divide([1,2,3,4,5],0,4)
print(count[0])

'''
Time complexity: O(nlogn)
Space complexity: O(n)
'''





  
