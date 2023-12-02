a,ta=list(map(int,input().split(" ")))
b,tb=list(map(int,input().split(" ")))
h,m=list(map(int,input().split(":")))

x1=h*60+m
y1=x1+ta

result=0

for x2 in range(5*60,24*60,b):
  y2=x2+tb
  x=max(x1,x2)
  y=min(y1,y2)
  if x<y:
    result+=1

print(result)