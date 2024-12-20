cent = 5
total = 0.00
round_down = 0.05
summa = []
while True:
    sum = input("Введите цены товаров (оставьте пустым для выхода): ")
    if sum == "":
         break
    else:
        summa.append(float(sum))
for i in range(len(summa)):
    total += summa[i]
print("Общая сумма: ",total)
rounding = total * 100 % cent
if rounding < cent / 2:
    cash_total = total - rounding / 100
else:
    cash_total = total + round_down - rounding / 100
print("Сумма для оплаты наличными: %.02f" % cash_total)