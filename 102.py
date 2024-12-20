user_password = input("Введите пароль для проверки: ")
if len(user_password) < 8:
    print("Пароль недостаточно надежный.")
else:
    has_upper = False  
    has_lower = False 
    has_digit = False   
    for char in user_password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    if has_upper and has_lower and has_digit:
        print("Пароль надежный")
    else:
        print("Пароль недостаточно надежный")