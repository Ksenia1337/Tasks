a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
min_value = min(a, b, c)
max_value = max(a, b, c)
median = (a + b + c) - min_value - max_value
print("Медиана: ", median)