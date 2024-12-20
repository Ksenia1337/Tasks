user_input = input("Введите строку: ").strip()
if len(user_input) == 0:
    print("Введенное значение НЕ является целым числом")
else:
    if user_input[0] in ('+', '-'):
        is_integer = len(user_input) > 1 and user_input[1:].isdigit()
    else:
        is_integer = user_input.isdigit()
    if is_integer:
        print("Введенное значение можно воспринимать как целое число")
    else:
        print("Введенное значение НЕ является целым числом")