numbers = []
while True:
    num_str = input("Введите число (или нажмите Enter для завершения): ")
    if num_str == "":
        break
    num = float(num_str)
    numbers.append(num)

if not numbers:
    print("Вы не ввели никаких чисел.")
else:
    mean = sum(numbers) / len(numbers)
    print(f"Среднее значение: {mean}")

    below_mean = []
    equal_mean = []
    above_mean = []

    for num in numbers:
        if num < mean:
            below_mean.append(num)
        elif num == mean:
            equal_mean.append(num)
        else:
            above_mean.append(num)

    print("Числа ниже среднего:")
    for num in below_mean:
        print(num)

    if equal_mean:
        print("Числа равные среднему:")
        for num in equal_mean:
            print(num)

    print("Числа выше среднего:")
    for num in above_mean:
        print(num)