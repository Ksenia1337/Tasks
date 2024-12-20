n = float(input("Введите число: "))
if n == 0:
    print("Первым числом не может быть ноль")
else:
    numbers = []
    while n != 0:
        numbers.append(n)
        n = float(input("Введите число: "))
    if numbers:
        average = sum(numbers) / len(numbers)
        print("Среднее значение:", average)
    else:
        print("Числа не введены")