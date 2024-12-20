years_old = float(input('Введите возраст вашей собаки в годах '))
if years_old > 0:
    if years_old > 2:
        print(f'На собачьем возрастей ей {((years_old - 2) * 4) + 2 * 10.5}')
    elif years_old <=2:
        print(f'На собачьем возрастей ей {years_old * 10.5}')
else:
    print('Возраст не может быть отрицательным!')
