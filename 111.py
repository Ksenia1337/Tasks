data = []
num = int(input("Введите целое число (0 для окончания ввода): "))
while num != 0:
    data.append(num)
    num = int(input("Введите целое число (0 для окончания ввода): "))
data.sort()
for num in range(len(data) - 1, -1, -1):
    print(data[num])
