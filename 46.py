letter = input("Введите букву: ").lower()
number = int(input("Введите цифру: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = range(1, 9)

if letter not in letters:
    print("Нет в списке, используйте A-H")
elif number not in numbers:
    print("Нет в списке, используйте 1-8")
else:
    letter_index = letters.index(letter)
    number_index = numbers.index(number)
    if letter_index % 2 == number_index % 2:
        print('Black')
    else:
        print('White')