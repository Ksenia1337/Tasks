num_1 = int(input('Введите первое целое число '))
num_2 = int(input('Введите второе целое число '))
num_3 = int(input('Введите третье целое число '))
minn = min(num_1, num_2, num_3) # Мин число
maxx = max(num_1, num_2, num_3) # Макс число
mid = num_1 + num_2 + num_3 - minn - maxx # Средн число
print("Числа в порядке возрастания:")
print(minn)
print(mid)
print(maxx)
