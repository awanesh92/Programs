import math
limit=1000000
def sieve_of_eratosthenes(limit):
  primes = [True] * limit
  primes[0] = primes[1] = False
  for i in range(2, limit):
    if primes[i]:
      for j in range(i*i, limit , i):
        primes[j] = False
  return primes

def is_t_prime(num, primes):
  if num ==4:
    return True
  elif num<4 or num%2==0:
    return False
  sqrt_num=num**0.5
  if sqrt_num==int(sqrt_num):
    if primes[int(sqrt_num)]:
      return True
  return False

def main():
  primes = sieve_of_eratosthenes(limit)
  n = int(input())
  numbers = list(map(int, input().split()))
  # print(primes)
  for num in numbers:
    if is_t_prime(num, primes):
      print("YES")
    else:
      print("NO")

if __name__ == "__main__":
  main()
