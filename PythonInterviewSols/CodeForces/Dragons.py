s,n=list(map(int,input().split(" ")))
result=True
dragon=[]
for _ in range(n):
  x,y=list(map(int,input().split(" ")))
  dragon.append([x,y])
dragon=sorted(dragon,key=lambda x:x[0])
for i in dragon:
  if s>i[0]:
    s+=i[1]
  else:
    result=False
    break
print("YES" if result else "NO")