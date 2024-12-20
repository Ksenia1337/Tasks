a = input("Введите длину первой стороны: ")
b = input("Введите длину второй стороны: ")
c = input("Введите длину третьей стороны: ")
if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit() and c.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)
    c = float(c)
    if a <= 0 or b <= 0 or c <= 0:
        print("Длины сторон должны быть положительными")
    elif a + b > c and a + c > b and b + c > a:
        print("Треугольник может быть построен")
    else:
        print("Треугольник не может быть построен")
else:
    print("Введите числовые значения")