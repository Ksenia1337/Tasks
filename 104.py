hex_char = input("Введите шестнадцатеричный символ: ")
hex_char = hex_char.upper()  
if hex_char in '0123456789ABCDEF':
    decimal_value = int(hex_char, 16)  
    print("Десятичное значение:", decimal_value)
else:
    print("Недопустимый символ")
decimal_number = int(input("Введите десятичное число: "))
if 0 <= decimal_number <= 15:
    hex_value = format(decimal_number, 'X')  
    print("Шестнадцатеричное значение:", hex_value)
else:
    print("Число должно быть в диапазоне от 0 до 15")