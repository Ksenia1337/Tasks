n = int(input("Введите первое целое число: "))
m = int(input("Введите второе целое число: "))
d = min(n, m)
while n % d != 0 or m % d != 0:
 d = d - 1
print("Наибольший общий делитель для равен", d)