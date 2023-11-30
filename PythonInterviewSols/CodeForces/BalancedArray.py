n=int(input())
for _ in range(n):
  x=int(input())
  if x%4!=0:
    print("NO")
    continue
  print("YES")
  lst=list(map(str,[i * 2 for i in range(1,x//2+1)]+[i*2-1 for i in range(1,x//2)]+[3*x//2-1]))
  print(" ".join(lst))