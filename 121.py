import random

lottery_numbers = set()
while len(lottery_numbers) < 6:
    lottery_numbers.add(random.randint(1, 49))

print("Случайные номера для вашего билета:")
for num in sorted(lottery_numbers):
    print(num)