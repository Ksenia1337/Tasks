frequency = float(input("Введите частоту волны: "))

if frequency < 3e9:
    print("Радиоволны")
elif 3e9 <= frequency < 3e12:
    print("Микроволны")
elif 3e12 <= frequency < 4.3e14:
    print("Инфракрасное излучение")
elif 4.3e14 <= frequency < 7.5e14:
    print("Видимое излучение")
elif 7.5e14 <= frequency < 3e17:
    print("Ультрафиолетовое излучение")
elif 3e17 <= frequency < 3e19:
    print("Рентгеновское излучение")
else:
    print("Гамма-излучение")