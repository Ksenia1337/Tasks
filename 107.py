##
# Максимальное сокращение дробей
#
## Вычислить наибольший общий делитель для двух целых чисел
# @param n – первое число (должно быть ненулевым)
# @param m – второе число (должно быть ненулевым)
# @return наибольший общий делитель двух целых чисел
def gcd(n, m):
 # Инициализируем d как меньшее значение из n и m
 d = min(n, m)
 # Используем цикл while для поиска наибольшего общего делителя n и m
 while n % d != 0 or m % d != 0:
     d = d - 1
 return d
## Сокращаем дробь до предела
# @param num – числитель дроби
# @param den – знаменатель дроби (должен быть ненулевым)
# @return числитель и знаменатель сокращенной дроби
def reduce(num, den):
 # Если числитель равен нулю, сокращенная дробь будет равна 0/1
 if num == 0:
     return (0, 1)
     # Находим наибольший общий делитель числителя и знаменателя
     g = gcd(num, den)
     # Делим числитель и знаменатель на НОД и возвращаем результат
     return (num // g, den // g)
     # Запрашиваем дробь у пользователя и отображаем ее максимально сокращенный вариант

     def main():
         # Запрашиваем числитель и знаменатель у пользователя
         num = int(input("Введите числитель дроби: "))
         den = int(input("Введите знаменатель дроби: "))
         # Вычисляем сокращенную дробь
         (n, d) = reduce(num, den)
         # Выводим результат
         print("Дробь %d/%d может быть сокращена до %d/%d." % (num, den, n, d))

     # Вызов основной функции
     main()