from collections import Counter
for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  n=Counter(a)
  l=[i[0] for i in n.items() if i[1]>1]
  # print(l,n,a)
  if l:
    print("NO")
  else:
    print("YES")