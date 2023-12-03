for _ in range(int(input())):
  n,k=list(map(int,input().split(" ")))
  a=list(map(int,input().split(" ")))
  b=list(map(int,input().split(" ")))
  result=0
  a=sorted(a)
  b=sorted(b,reverse=True)
  # print(a,b)
  for i in range(n):
    if i<k:
      result+=max(a[i],b[i])
    else:
      result+=a[i]
  print(result)