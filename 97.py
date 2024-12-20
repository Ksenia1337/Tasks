user_input = input("Введите математический оператор (+, -, *, /, ^): ").strip()
if user_input == '+' or user_input == '-':
    priority = 1
elif user_input == '*' or user_input == '/':
    priority = 2
elif user_input == '^':
    priority = 3
else:
    priority = -1
if priority != -1:
    print(f"Приоритет оператора '{user_input}': {priority}")
else:
    print("Введен неверный оператор")