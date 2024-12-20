user_input = input("Введите строку: ")
words = []
current_word = ""

for char in user_input:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9' or char == "'" or char == '-':
        current_word += char
    elif current_word:
        words.append(current_word)
        current_word = ""

if current_word:
    words.append(current_word)

print(words)