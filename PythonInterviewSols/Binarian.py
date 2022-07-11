def solution(A):
  s=set()
  for a in A:
    while a in s:
      s.remove(a)
      a+=1
    s.add(a)
  s=sorted(s,reverse=True)
  return len(s)

A=list(map(int,input().split()))
print(solution(A))