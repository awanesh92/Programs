def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    for pw in range(2, 30):
      val = (1 << pw) - 1
      if n % val == 0:
        print(n // val)
        break

if __name__ == "__main__":
  main()
