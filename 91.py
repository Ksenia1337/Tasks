day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29 
ordinal_day = sum(days_in_month[:month - 1]) + day
print("Порядковый номер дня: ", ordinal_day)