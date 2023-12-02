for _ in range(int(input())):
  st=input()
  if len(st)==2:
    print(st)
    continue
  res=st[:2]
  for i in range(2,len(st),2):
    res+=st[i+1]
  print(res)