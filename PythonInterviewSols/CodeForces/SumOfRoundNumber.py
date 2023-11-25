t = int(input())

for _ in range(t):
  n = int(input())
  ans = []
  power = 1

  while n > 0:
    if n % 10 > 0:
      ans.append((n % 10) * power)
    n //= 10
    power *= 10

  print(len(ans))
  print(*ans)
