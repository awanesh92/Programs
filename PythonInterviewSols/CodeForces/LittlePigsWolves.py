n, m = map(int, input().split())
grid = [input() for _ in range(n)]

count = 0
for i in range(n):
  for j in range(m):
    if grid[i][j] == 'W':
      # Check for adjacent pigs
      if i > 0 and grid[i - 1][j] == 'P':
        count += 1
      elif i < n - 1 and grid[i + 1][j] == 'P':
        count += 1
      elif j > 0 and grid[i][j - 1] == 'P':
        count += 1
      elif j < m - 1 and grid[i][j + 1] == 'P':
        count += 1

print(count)
