cents_toonie = 200
cents_loonie = 100
cents_quarter = 25
cents_dime =10
cents_nickel = 5
cents = int(input('Введите сумму в центах '))
print(cents // cents_toonie, '2-долларовых монет') # Количество 2-долларовых монет = деления суммы на 200
cents = cents % cents_toonie # Смотрим остаток и считаем дальше
print(cents // cents_loonie, '1-долларовых монет')
cents = cents % cents_loonie
print(cents // cents_quarter, '25–центовых монет')
cents = cents % cents_quarter
print(cents // cents_dime, '10–центовых монет')
cents = cents % cents_dime
print(cents // cents_nickel, '5–центовых монет')
cents = cents % cents_nickel
print('Остаток', cents) # Oстаток в центах
