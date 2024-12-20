# Вычисляем стоимость вчерашнего хлеба
BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60
# Запрашиваем данные у пользователя
num_loaves = int(input("Введите количество вчерашних буханок хлеба: "))
# Вычисляем скидку и общую стоимость
regular_price = num_loaves * BREAD_PRICE
discount = regular_price * DISCOUNT_RATE
total = regular_price - discount
# Отобразим результат в нужном формате
print("Номинальная цена: %5.2f" % regular_price)
print("Сумма скидки: %5.2f" % discount)
print("Итого: %5.2f" % total)
