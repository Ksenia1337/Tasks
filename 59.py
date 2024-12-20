day_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("Введите год "))
month = int(input("Введите месяц "))
day = int(input("Введите день "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day_per_month[1] = 29
if day != day_per_month[month - 1]:
    day += 1
elif month != 12:
    day = 1;
    month += 1;
else:
    day = month = 1;
    year += 1
print(f'{day}.{month}.{year}')