c='codeforces'
for _ in range(int(input())):
  n=input()
  l=len(n)
  res=0
  for i in range(l):
    if n[i]!=c[i]:
      res+=1
  print(res)