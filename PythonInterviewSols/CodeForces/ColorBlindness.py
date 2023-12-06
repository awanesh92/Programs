for _ in range(int(input())):
  n=int(input())
  a=input()
  b=input()
  flag=True
  for i in range(n):
    if a[i]==b[i]:
      continue
    if a[i]!=b[i] and (a[i] in ['B','G'] and b[i] in ['B','G']) :
      continue
    else:
      flag=False
      break

  if(flag):
    print("YES")
  else:
    print("NO")