BASE_FARE = 4.00 
COST_PER_140M = 0.25  
distance_km = float(input("Введите расстояние поездки в километрах: "))
fare = BASE_FARE + (distance_km * 1000 / 140) * COST_PER_140M
print(f"Итоговая сумма оплаты такси: ${fare:.2f}")