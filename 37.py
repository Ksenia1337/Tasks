letter = input('Введите букву латинского алфавита ')
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(f'Буква {letter} гласная ')
elif letter == 'y':
    print(f'Буква {letter} может быть и гласной и согасной')
else:
    print(f'Буква {letter} согласная')
