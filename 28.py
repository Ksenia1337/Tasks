единицы = input("Введите 'дюймы' или 'см': ")
рост = float(input("Введите ваш рост: "))
вес = float(input("Введите ваш вес: "))

if единицы == "дюймы":
    имт = (вес / (рост ** 2)) * 703
elif единицы == "см":
    имт = вес / (рост ** 2)

print(f"Ваш ИМТ: {имт:.2f}")