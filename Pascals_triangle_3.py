'''
Find the value that present in the given row and col of a pascal's triangle
'''
def fun(row,col):
  #here row and col are 1-indexed
  ans=1
  for i in range(1,col):
    ans=ans*(row-i)
    ans/=i
  return int(ans)

print(fun(3,2))

'''
Time complexity: O(col)
Space complexity: O(1)
'''
