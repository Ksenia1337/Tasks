words = []
word = input("Введите слово (Enter для окончания ввода): ")
while word != "":
    if word not in words:
        words.append(word)
    word = input("Введите слово (Enter для окончания ввода): ")
print(words)