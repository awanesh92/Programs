from collections import Counter
for _ in range(int(input())):
  n=int(input())
  res=[0,0,0]
  a1=input().split(" ")
  b1=input().split(" ")
  c1=input().split(" ")
  abc=a1+b1+c1
  d=Counter(abc)
  for i in range(n):
    if d[a1[i]]==1:
      res[0]+=3
    if d[b1[i]]==1:
      res[1]+=3
    if d[c1[i]]==1:
      res[2]+=3
    if d[a1[i]]==2:
      res[0]+=1
    if d[b1[i]]==2:
      res[1]+=1
    if d[c1[i]]==2:
      res[2]+=1
  print(*res)
