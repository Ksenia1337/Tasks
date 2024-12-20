phrase = (input("Введите фразу для проверки: ")).lower() # сразу в нижний регистр
new_phrase = ''
for char in phrase:  # перебираем все символы, оставляем только буквы
    if char.isalpha():
        new_phrase += char
result = "Палиндром"
for i in range(0, int(len(new_phrase)/2)):
    if new_phrase[i] != new_phrase[len(new_phrase)-i-1]:
        result = 'Не является палиндромом'
        break
print(result)