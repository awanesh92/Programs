n=int(input())
for _ in range(n):
  m=int(input())
  a=list(map(int,input().split(" ")))
  # print(a)
  even,odd=[],[]
  #even
  for i in range(0,len(a),2):
    if a[i]%2!=0:
      even.append(a[i])
  #Odd
  for i in range(1,len(a),2):
    if a[i]%2!=1:
      odd.append(a[i])
  # print(even,odd)
  if len(odd)!=len(even):
    print("-1")
    continue
  else:
    print(len(odd))