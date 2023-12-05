for _ in range(int(input())):
  curr=[(0,0)]
  a=[]
  for _ in range(int(input())):
    a1,b1=list(map(int,input().split(" ")))
    a.append((a1,b1))
  a.sort()
  flag=True
  result=''
  for i in range(len(a)):
    r=a[i][0]-curr[0][0]
    u=a[i][1]-curr[0][1]
    if r<0 or u<0:
      flag=False
      break
    result+='R'*r
    result+='U'*u
    curr.pop()
    curr.append(a[i])
  if flag:
    print("YES")
    print(result)
  else:
    print("NO")
  # print(a)