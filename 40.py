noise = float(input('Введите уровень громкости в децибелах от 40 до 130 '))
if 40 <= noise <=130:
    if noise == 130:
        print('Это отбойный молоток')
    if noise == 106:
        print('Это газовая газонокосилка')
    if noise == 70:
        print('Это будильник')
    if noise == 40:
        print('Это тихая комната')
    elif 40 < noise <70:
        print('Что-то между тихой комнатой и будильником')
    elif 71 < noise <106:
        print('Что-то между будильником и газовой газонокосилкой')
    elif 107 < noise <130:
        print('Что-то между газовой газонокосилкой и отбойным молотком')
else:
        print('Вы ввели некорректное значение, перечитайте условие')
