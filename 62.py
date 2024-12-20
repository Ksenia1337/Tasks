import random
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [i for i in range(1, 37) if i not in red_numbers]
result = random.randint(0, 36)
color = "красное" if result in red_numbers else "черное" if result in black_numbers else "зеленое"
parity = "четное" if result % 2 == 0 and result != 0 else "нечетное"
range_num = "от 1 до 18" if result >= 1 and result <= 18 else "от 19 до 36" if result >= 19 and result <= 36 else "0 или 00"
print(f"Выпавший номер: {result}")
print(f"Цвет: {color}")
print(f"Четность: {parity}")
print(f"Диапазон: {range_num}")