def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30
month = int(input("Введите номер месяца: "))
year = int(input("Введите год: "))
days = days_in_month(month, year)
print(f"Количество дней в месяце {month} года {year}: {days}")