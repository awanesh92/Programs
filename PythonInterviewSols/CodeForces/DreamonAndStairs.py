n,m=list(map(int,input().split(" ")))
low_bnd=(n+1)//2
print(low_bnd+m-1,m*m)
result=(low_bnd+m-1)//m*m
print("-1") if result>n else print(result)