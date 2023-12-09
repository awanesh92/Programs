# Function to precompute the array
def precompute(s):
  n = len(s)
  count = [0] * n

  for i in range(1, n):
    count[i] = count[i - 1] + (s[i] == s[i - 1])

  return count

# Function to answer a single query
def answer_query(count, li, ri):
  return count[ri - 1] - count[li - 1]

# Main function to read input and process queries
def main():
  s = input().strip()
  count = precompute(s)

  m = int(input().strip())
  for _ in range(m):
    li, ri = map(int, input().split())
    result = answer_query(count, li, ri)
    print(result)

# Run the main function
if __name__ == "__main__":
  main()
