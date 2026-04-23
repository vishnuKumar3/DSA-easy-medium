'''
https://takeuforward.org/plus/dsa/problems/find-the-repeating-and-missing-number?source=strivers-a2z-dsa-track
'''
def fun(ar):
  #let's assume repeated number is x and missing number is y
  n=len(ar)
  sn=int((n*(n+1))/2) #sum of n natural numbers
  s2n=int((n*(n+1)*(2*n+1))/6) #sum of squares of n natural numbers
  sAr=sum(ar) #sum of given array
  s2Ar=0
  #find sum of squares of given array
  for i in ar:
    s2Ar+=i*i
  
  val1=sAr-sn #x-y
  val2=s2Ar-s2n #(x-y)(x+y)
  val3=int(val2/val1) #x+y
  x=int((val1+val3)/2) #x+y+(x-y)/2 = x
  y=x-val1
  print(f"repeated:{x}, missing:{y}")
  
  
  
fun([3, 5, 4, 1, 1])
fun([1, 2, 3, 6, 7, 5, 7])

'''
Time complexity: O(n)
Space complexity: O(1)
'''
