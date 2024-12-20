day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения: ").lower()
if (month == "март" and day >= 21) or (month == "апрель" and day <= 19):
    sign = "Овен"
elif (month == "апрель" and day >= 20) or (month == "май" and day <= 20):
    sign = "Телец"
elif (month == "май" and day >= 21) or (month == "июнь" and day <= 21):
    sign = "Близнецы"
elif (month == "июнь" and day >= 22) or (month == "июль" and day <= 22):
    sign = "Рак"
elif (month == "июль" and day >= 23) or (month == "август" and day <= 22):
    sign = "Лев"
elif (month == "декабрь" and day >= 22) or (month == "январь" and day <= 19):
    sign = "Козерог"
elif (month == "январь" and day >= 20) or (month == "февраль" and day <= 18):
    sign = "Водолей"
elif (month == "февраль" and day >= 19) or (month == "март" and day <= 20):
    sign = "Рыбы"
elif (month == "август" and day >= 23) or (month == "сентябрь" and day <= 22):
    sign = "Дева"
elif (month == "октябрь" and day >= 23) or (month == "ноябрь" and day <= 21):
    sign = "Скорпион"
else:
    sign = "Стрелец"
print(sign)