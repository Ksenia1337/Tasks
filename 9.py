deposit = float(input("Введите сумму первоначального депозита: "))
interest_rate = 0.04
amount_year_1 = deposit * (1 + interest_rate)
amount_year_2 = amount_year_1 * (1 + interest_rate)
amount_year_3 = amount_year_2 * (1 + interest_rate)
print(f"Сумма на счету в конце первого года: {amount_year_1:.2f} руб.")
print(f"Сумма на счету в конце второго года: {amount_year_2:.2f} руб.")
print(f"Сумма на счету в конце третьего года: {amount_year_3:.2f} руб.")
