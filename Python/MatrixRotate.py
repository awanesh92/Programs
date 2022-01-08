import pprint
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rotatematrix(n,k):
  l=len(n)
  temp=n.copy()
  for i in range(l):
    temp[(i+k)%l]=n[i]
  return temp

result=[]
for i in range(len(mat)):
  if i%2==0:
    result.append(rotatematrix(mat[i],1))
  else:
    result.append(rotatematrix(mat[i],len(mat[i])-1))

pprint.pprint(result)