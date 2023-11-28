n = int(input())
prices = list(map(int, input().split()))
q = int(input())

# Sort the prices array
prices.sort()

for _ in range(q):
  m = int(input())

  # Binary search to find the position where Vasiliy can buy a bottle
  left, right = 0, n
  while left < right:
    mid = (left + right) // 2
    if prices[mid] <= m:
      left = mid + 1
    else:
      right = mid

  # Output the number of shops where Vasiliy can buy a bottle
  print(left)
