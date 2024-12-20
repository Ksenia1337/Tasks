from math import sqrt
s_1 = float(input('Введите длину первого катета: '))
s_2 = float(input('Введите длину второго катета: '))
s_3 = float(input('Введите длину третьего катета: '))
s = (s_1 + s_2 + s_3) / 2
print(f'Площадь треугольника: {sqrt(s * (s - s_1) * (s - s_2) * (s - s_3))}.')
