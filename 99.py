def isPrime(n):
    """
    Checks if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # Optimized loop
        if n % i == 0:
            return False
    return True

def nextPrime(n):
    """
    Finds the next prime number greater than n.

    Args:
        n: The starting number.

    Returns:
        The first prime number greater than n.
    """
    num = n + 1
    while True:
        if isPrime(num):
            return num
        num += 1

def main():
    value = int(input("Введите целое число: "))
    next_prime = nextPrime(value)
    print(f"Следующее простое число после {value} это {next_prime}")


if __name__ == "__main__":
    main()