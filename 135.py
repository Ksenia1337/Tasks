limit = int(input("Введите верхнюю границу диапазона: "))
numbers = list(range(limit + 1))
numbers[0] = numbers[1] = 0

p = 2
while p * p <= limit:
    if numbers[p] != 0:
        for i in range(p * p, limit + 1, p):
            numbers[i] = 0
    p += 1

primes = [number for number in numbers if number != 0]
print("Простые числа в диапазоне:", primes)