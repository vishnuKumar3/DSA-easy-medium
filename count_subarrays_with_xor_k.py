'''
https://takeuforward.org/data-structure/count-the-number-of-subarrays-with-given-xor-k
'''
def fun(ar,k):
  d={0:1}
  track=0
  count=0
  for i in ar:
    track=track^i
    req=track^k
    if(d.get(req)!=None):
      count+=d[req]
    if(d.get(track)==None):
      d[track]=0
    d[track]+=1
  
  print(count)      
    

fun([4,2,2,6,4],6)
fun([5,6,7,8,9],5)
  
'''
Time complexity: O(n)
Space complexity: O(n)
'''
