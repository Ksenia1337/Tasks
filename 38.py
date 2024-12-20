sides = int(input('Введите количество сторон фигуры от 3 до 10 '))
name = ''
if sides == 3:
 name = 'треугольник'
elif sides == 4:
 name = 'прямоугольник'
elif sides == 5:
 name = 'пятиугольник'
elif sides == 6:
 name = 'шестиугольник'
elif sides == 7:
 name = 'семиугольник'
elif sides == 8:
 name = 'восьмиугольни'
elif sides == 9:
 name = 'девятиугольник'
elif sides == 10:
 name = 'десятиугольник'
if name == '':
 print('Перечитайте условие и введите корректное число')
else:
 print(f'Эта фигура {name}')
