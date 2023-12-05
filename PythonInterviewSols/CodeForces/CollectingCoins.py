for _ in range(int(input())):
  xn=list(map(int,input().split(" ")))
  n=xn[-1]
  a,b,c=sorted(xn[:-1])
  # print(a,b,c)
  n-=(2*c-b-a)
  if n<0 or n%3!=0:
    print("NO")
  else:
    print("YES")