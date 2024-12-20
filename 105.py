hex_char = input("Введите шестнадцатеричный символ: ")
hex_char = hex_char.upper()
# Переводим значение из одной системы счисления в другую. Диапазон систем – от 2 до 16
#
from hex_digit import *
## Переводим число из десятичной системы в произвольную
# @param num – число в десятичной системе для преобразования
# @param new_base – основание для выходного результата
# @return строка в новой системе счисления
def dec2n(num, new_base):
 # Формируем представление числа в новой системе счисления, сохраняя в result
 result = ""
 q = num
 # Первый запуск тела будущего цикла
 r = q % new_base
 result = int2hex(r) + result
 q=q // new_base
 # Продолжаем цикл, пока q не станет равен нулю
 while q > 0:
     r = q % new_base
 result = int2hex(r) + result
 q = q // new_base
 # Возвращаем результат
 return result
## Переводим число из произвольной системы
# в десятичную
# @param num – число в системе по основанию b,
# сохраненное в виде строки
# @param b – основание преобразуемого числа
# @return число в десятичной системе счисления
def n2dec(num, b):
 decimal = 0
 # Обрабатываем каждую цифру по основанию b
 for i in range(len(num)):
     decimal = decimal * b
     decimal = decimal + hex2int(num[i])
 # Возвращаем результат
 return decimal

 # Преобразуем число между произвольными системами счисления
 def main():
     # Запрашиваем у пользователя исходную систему счисления и число
     from_base = int(input("Исходная система счисления (2–16): "))
     if from_base < 2 or from_base > 16:
         print("Допустимый диапазон систем счисления: от 2 до 16.")
     print("Выходим...")
     quit()
     from_num = input("Введите число по этому основанию: ")
     # Преобразуем в десятичное число и отображаем результат
     dec = n2dec(from_num, from_base)
     print("Результат: %d по основанию 10." % dec)
     # Преобразуем в число с новым основанием и отображаем результат
     to_base = int(input("Введите требуемую систему счисления (2–16): "))
     if to_base < 2 or to_base > 16:
         print("Допустимый диапазон систем счисления: от 2 до 16.")
     print("Выходим...")
     quit()
     to_num = dec2n(dec, to_base)
     print("Результат: %s по основанию %d." % (to_num, to_base))

 # Вызов основной функции
 main()