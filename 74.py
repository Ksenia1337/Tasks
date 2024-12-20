x = float(input("Введите число: "))
if x < 0:
    print("Число должно быть неотрицательным")
else:
    guess = x / 2.0
    tolerance = 1e-12
    while abs(guess*guess - x) > tolerance:
        guess = (guess + x / guess) / 2
    print("Приблизительный квадратный корень из " + str(x) + ": " + str(guess))