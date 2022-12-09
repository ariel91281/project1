def get_divisors(num1):
  sum = 0
  for i in range(1, num1 + 1):
    if num1 % i == 0:
      sum += i
  return sum
x = get_divisors(15)
print(x)
print(x+1)

