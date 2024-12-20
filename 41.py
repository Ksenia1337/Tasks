side_1 = float(input('Длина первой стороны '))
side_2 = float(input('Длина второй стороны '))
side_3 = float(input('Длина третьей стороны '))
if side_1 == side_2 and side_2 == side_3:
    type_triugolnik = 'равносторонний'
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    type_triugolnik = 'равнобедренный'
else:
    type_triugolnik = 'разносторонний'
print(f'Этот треугольник {type_triugolnik}')
