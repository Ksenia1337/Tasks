from math import tan, pi
s = float(input('Введите длину стороны: '))
n = float(input('Введите количество сторон: '))
print(f'Площадь правильного многоугольника: {(n * s * s) / (4 * tan(pi / n))}.')
