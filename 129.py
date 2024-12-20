numbers = []
while True:
    num_str = input("Введите число (или нажмите Enter для завершения): ")
    if not num_str:
        break
    numbers.append(float(num_str))

if len(numbers) <= 1:
    is_sorted = True
else:
    is_sorted = True
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            is_sorted = False
            break

if is_sorted:
    print("Список отсортирован.")
else:
    print("Список не отсортирован.")