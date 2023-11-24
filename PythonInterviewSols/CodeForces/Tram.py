x=int(input())
a,b=[],[]
for i in range(x):
  tmp=list(map(int,input().split()))
  a.append(tmp[0])
  b.append(tmp[1])
result=b[0]
maxs=result
for i in range(1,x-1):
  result=result-a[i]+b[i]
  maxs=max(maxs,result)
print(maxs)
