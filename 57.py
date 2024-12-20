minutes_used = int(input("Введите количество израсходованных минут: "))
sms_used = int(input("Введите количество отправленных смс: "))
base_minutes = 50
base_sms = 50
base_cost = 15.00
extra_minute_cost = 0.25
extra_sms_cost = 0.15
tax_rate = 0.05
extra_minutes = max(0, minutes_used - base_minutes)
extra_sms = max(0, sms_used - base_sms)
extra_minutes_cost = extra_minutes * extra_minute_cost
extra_sms_cost = extra_sms * extra_sms_cost
extra_total_cost = extra_minutes_cost + extra_sms_cost
base_total_cost = base_cost
subtotal = base_total_cost + extra_total_cost
tax = subtotal * tax_rate
total_cost = subtotal + tax
print(f"Базовая сумма тарификации (без учета налога): ${base_total_cost:.2f}")
print(f"Сумма за дополнительные минуты и сообщения (без учета налога): ${extra_total_cost:.2f}")
print(f"Налог на всю сумму: ${tax:.2f}")
print(f"Итоговая сумма к оплате (с учетом налога): ${total_cost:.2f}")