plus=lambda a,b:a+b
minus=lambda a,b:a-b
for _ in range(int(input())):
  a,b,c=list(map(int,input().split(" ")))
  if plus(a,b)==c:
    print("+")
  if minus(a,b)==c:
    print("-")