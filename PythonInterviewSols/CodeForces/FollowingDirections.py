for _ in range(int(input())):
  n=int(input())
  s=input()
  x,y=0,0
  flag=True
  for i in s:
    if i=='U':
      y+=1
    elif i=='D':
      y-=1
    elif i=='L':
      x-=1
    elif i=='R':
      x+=1
    if x==1 and y==1:
      flag = False
      break
  if not flag:
    print("YES")
  else:
    print("NO")