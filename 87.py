items = int(input("Введите количество товаров в заказе: "))
if items <= 0:
    total_cost = 0  
elif items == 1:
    total_cost = 10.95 
else:
    total_cost = 10.95 + (items - 1) * 2.95 
print(f"Сумма доставки: ${total_cost:.2f}")