num = float(input())
if num == 0.0:
    print('Низкий уровень', 0, '$')
elif num == 0.4:
    print('Удовлетворительный уровень', 960, '$')
elif num >= 0.6 and num <= 1:
    print('Высокий уровень', num * 2400, '$')
else:
    print('Не может быть такого значения')
