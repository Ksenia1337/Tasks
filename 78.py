while True:
    number = float(input("Введите стартовое число (ноль или отрицательное для выхода): "))
    if number <= 0:
        break
    while (number != 1):
        if (number % 2 == 0):
            number = number / 2
        else:
            number = 3 * number +1
        print(int(number))