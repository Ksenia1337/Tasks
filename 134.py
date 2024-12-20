list1 = [1, 2, 3]
list2 = [4, 5]
list3 = []

# Для первого списка
sublists1 = [[]]  # Инициализируем с пустым подсписком
for i in range(len(list1) + 1):
    for j in range(i + 1, len(list1) + 1):
        sublists1.append(list1[i:j])

print(f"Подсписки списка {list1}: {sublists1}")

# Для второго списка
sublists2 = [[]]  # Инициализируем с пустым подсписком
for i in range(len(list2) + 1):
    for j in range(i + 1, len(list2) + 1):
        sublists2.append(list2[i:j])

print(f"Подсписки списка {list2}: {sublists2}")

# Для третьего списка
sublists3 = [[]]  # Инициализируем с пустым подсписком
for i in range(len(list3) + 1):
    for j in range(i + 1, len(list3) + 1):
        sublists3.append(list3[i:j])

print(f"Подсписки списка {list3}: {sublists3}")