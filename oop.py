def fibonacci(n):
    # when n is negative print error
  if n < 0:
    print("n is negative")

  if n == 2:
    return n

  a, b = 1, 1

  for num in range(2, n):
    a, b = b, a + b

  return b


for x in range(10):
    print(fibonacci(x))