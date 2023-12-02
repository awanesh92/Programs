n,m,k=list(map(int,input().split(" ")))
p=list(map(int,input().split(" ")))
result=0
for _ in range(n):
  a=list(map(int,input().split(" ")))
  for i in a:
    result+=(p.index(i)+1)
    p.remove(i)
    p.insert(0,i)
print(result)