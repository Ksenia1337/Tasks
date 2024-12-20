a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
x1 = (-b - D ** 0.5) / (2 * a)
x2 = (-b + D ** 0.5) / (2 * a)
if D < 0:
    print("Нет корней")
elif b ** 2 - 4 * a * c == 0:
    print(1)
    print(-b / (2 * a))
else:
    if min(x1, x2) == x1:
        print(2)
        print((-b - D ** 0.5) / (2 * a))
        print((-b + D ** 0.5) / (2 * a))
    else:
        print(2)
        print((-b + D ** 0.5) / (2 * a))
        print((-b - D ** 0.5) / (2 * a))


