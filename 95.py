input_text = input("Введите строку: ")
chars = list(input_text)
capitalize_next = True
for i in range(len(chars)):
    char = chars[i]
    if capitalize_next and char.isalpha():
        chars[i] = char.upper()
        capitalize_next = False
    if char in '.!?':
        capitalize_next = True 
    if char.lower() == 'i':
        if (i == 0 or chars[i - 1] in [' ', '.', '!', '?']):
            chars[i] = 'I'
corrected_text = ''.join(chars)
print("Исправленная строка: ", corrected_text)