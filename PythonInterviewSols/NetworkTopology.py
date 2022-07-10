def solution(n,m,x,y):
  deg=[0]*n
  for i in range(m):
    deg[x[i-1]-1]+=1
    deg[y[i-1]-1]+=1

  r='unknown'

  s=set(deg)
  if s=={2}:
    r='ring'
  elif s=={1,2}:
    r='bus'
  elif s=={1,m}:
    r='star'
  print(f'{r} topology')

Input=lambda :map(int,input().split())
n,m=Input()
x,y=list(),list()
for i in range(m):
  a,b=Input()
  x.append(a)
  y.append(b)
solution(n,m,x,y)