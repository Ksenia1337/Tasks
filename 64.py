original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = 0.60  # Скидка 60%
for original_price in original_prices:
    discount_amount = original_price * discount  # Сумма скидки
    new_price = original_price - discount_amount  # Новая цена
    print(original_price, discount_amount, new_price)
