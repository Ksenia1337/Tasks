WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = –11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16
temp = float(input("Температура воздуха (градусы Цельсия): "))
speed = float(input("Скорость ветра (км/ч): "))
wci = WC_OFFSET + \
WC_FACTOR1 * temp + \
WC_FACTOR2 * speed ** WC_EXPONENT + \
WC_FACTOR3 * temp * speed ** WC_EXPONENT
print("Коэффициент охлаждения ветром равен", round(wci))