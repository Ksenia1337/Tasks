def isPrime(n):
 if n <= 1:
   return False
 for i in range(2, n):
     if n % i == 0:
        return False
        return True
def main():
 value = int(input("Введите целое число: "))
 if isPrime(value):
    print(value, "– простое число")
 else:
    print(value, "не является простым числом")
if __name__ == "__main__":
 main()