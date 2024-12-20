
negatives = []
zeros = []
positives = []
line = input("Введите целое число (Enter для окончания ввода): ")
while line != "":
    num = int(line)
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)
    line = input("Введите целое число (Enter для окончания ввода): ")
print("Введенные числа: ")
for n in negatives:
    print(n)
for n in zeros:
    print(n)
for n in positiv