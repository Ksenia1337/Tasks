import math
t1 = float(input("Введите широту первой точки (в градусах): "))
g1 = float(input("Введите долготу первой точки (в градусах): "))
t2 = float(input("Введите широту второй точки (в градусах): "))
g2 = float(input("Введите долготу второй точки (в градусах): "))
t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)
distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(f"Расстояние между точками: {distance:.2f} километров.")
