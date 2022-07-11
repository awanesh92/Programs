def solution():
    x=int(input())
    original = list(map(int,input().split()))
    target = list(map(int,input().split()))
    d=[0]*(x+2)

    for i in range(x):
      d[i+1]=target[i]-original[i]

    cnt=0
    for i in range(len(d)-1):
      if d[i]<0:
        return False
      if d[i]!=d[i+1]:
        cnt+=1
    return cnt<=2


for _ in range(int(input())):
  result=solution()
  if result:
    print("YES")
  else:
    print("NO")