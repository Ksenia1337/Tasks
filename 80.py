def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors
n = int(input("Введите число: "))
if n < 2:
  print("Ошибка")
else:
  print("Простые множители:", prime_factors(n))
