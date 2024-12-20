number_kPa = float(input('Введите значение давления в кПа '))
number_PSI = number_kPa * 0.14503773773022 # 1 kPa = 0.14503773773022 PSI
print(f'В {number_kPa} кПа содержится {number_PSI} ПСИ')
