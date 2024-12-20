numbers = []
while True:
    num_str = input("Введите число (или нажмите Enter для завершения): ")
    if not num_str:
        break
    numbers.append(float(num_str))


if not numbers:
     print("Список отсортирован.")
else:

    is_increasing = True
    for i in range(1, len(numbers)):
       if numbers[i] < numbers[i-1]:
          is_increasing = False
          break

    is_decreasing = True
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
          is_decreasing = False
          break

    if is_increasing or is_decreasing:
        print("Список отсортирован.")
    else:
        print("Список не отсортирован.")
        