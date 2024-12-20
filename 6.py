order_amount = float(input("Введите сумму заказа в ресторане: "))
tax = 0.10
tax_amount = order_amount * tax
tip_amount = order_amount * 0.18
total_amount = order_amount + tax_amount + tip_amount
print(f"Налог: {tax_amount:.2f}")
print(f"Чаевые: {tip_amount:.2f}")
print(f"Итого: {total_amount:.2f}")
