#996A
n=int(input())
notes=[1,5,10,20,100]
result=0
for i in notes[::-1]:
  result+=(n//i)
  n%=i
print(result)