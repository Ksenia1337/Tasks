month = input('Введите месяц ')
if month == 'Январь' or month == 'Март' or month == 'Май' or month == 'Июль' \
   or month == 'Август' or month == 'Октябрь' or month == 'Декабрь':
    print('В этом месяце 31 день')
elif month == 'Февраль':
    print('В этом месяце может быть и 28 и 29 дней')
else:
    print('В этом месяце 30 дней')
