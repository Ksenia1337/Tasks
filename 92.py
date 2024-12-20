ordinal_date = int(input("Введите день в году: "))
year = int(input("Введите год: "))
days_offset = int(input("Введите количество дней для смещения: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29 
new_ordinal_date = ordinal_date + days_offset
while new_ordinal_date > (days_in_month[1] if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else sum(days_in_month)):
    new_ordinal_date -= (days_in_month[1] if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else sum(days_in_month))
    year += 1
month = 0
while new_ordinal_date > days_in_month[month]:
    new_ordinal_date -= days_in_month[month]
    month += 1
day = new_ordinal_date
month += 1 
print(f"Новая дата: {day:02d}.{month:02d}.{year}")