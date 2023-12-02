n, k = map(int, input().split())
a = list(map(int, input().split()))

# Compute the initial sum of the first segment
current_sum = sum(a[:k])
min_sum = current_sum
min_index = 0

for i in range(1, n - k + 1):
  current_sum = current_sum - a[i - 1]
  current_sum = current_sum + a[i + k - 1]

  if current_sum < min_sum:
    min_sum = current_sum
    min_index = i

print(min_index + 1)
