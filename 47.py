mon = input()
day = int(input())
if mon.lower() == 'апрель' or mon.lower() == 'май' or mon.lower() == 'март' and day > 19 or mon.lower() == 'июнь' and day < 21:
    print('Весна')
elif mon.lower() == 'июль' or mon.lower() == 'август' or mon.lower() == 'июнь' and day > 21 or mon.lower() == 'сентябрь' and day < 22:
    print('Лето')
elif mon.lower() == 'октябрь' or mon.lower() == 'ноябрь' or mon.lower() == 'сентябрь' and day > 22 or mon.lower() == 'декабрь' and day < 21:
    print('Осень')
else:
    print('Зима')