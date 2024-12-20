import math
a = int(input("Введите первое целое число (a): "))
b = int(input("Введите второе целое число (b): "))
sum_result = a + b
difference_result = a - b
product_result = a * b
if b != 0:
    division_result = a / b
    remainder_result = a % b
log_result = math.log10(a)
power_result = a ** b
print(f"Сумма a и b: {sum_result}")
print(f"Разница между a и b: {difference_result}")
print(f"Произведение a и b: {product_result}")
print(f"Частное от деления a на b: {division_result}")
print(f"Остаток от деления a на b: {remainder_result}")
print(f"Десятичный логарифм числа a: {log_result}")
print(f"Результат возведения числа a в степень b: {power_result}")
