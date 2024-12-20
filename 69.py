years = input("Введите возраст посетителя: ")
cost = 0
while years != '':
    if 3 < int(years) < 12:
        cost += 14
    elif 13 < int(years) < 65:
        cost += 23
    elif int(years) > 65:
        cost += 18
    else:
        cost += 0
    years = input("Введите возраст посетителя: ")
print("Общая стоимость: $", format(cost, '.2f'), sep='')