n,x=map(int,input().split(" "))
m=list(map(int,input().split(" ")))

for i in range(x):
  # print(m[i])
  if i==0:
    result=m[0]-1
  elif m[i]>=m[i-1]:
    result+=m[i]-m[i-1]
  else:
    result+=n-m[i-1]+m[i]
  # print(result)
print(result)