from math import floor

def day_of_week(year):
    day_of_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7
    days = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    return days[day_of_week]

year = int(input('Введите год: '))
day = day_of_week(year)
print(f'1 января {year} года приходится на {day}.')