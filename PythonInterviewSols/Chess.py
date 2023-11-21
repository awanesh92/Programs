global mat,m,n

mat=[[0]*10 for i in range(10)]

def kingmove(x,y):
  mov=[[1,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1],[0,1],[1,0]]
  res=[]
  for i in mov:
    x1=x+i[0]
    y1=y+i[1]
    if 0<=x1<10 and 0<=y1<10:
      res.append((x1,y1))
  return res

mat=[]
print(kingmove(9,9))

def queenmove(x,y):
  res=[]
  for i in range(8):
    res.append(x+i,y)
