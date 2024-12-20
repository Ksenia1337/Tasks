import random

def random_license_plate():
    if random.randint(0, 1) == 0:
        # старый формат
        letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))
        numbers = ''.join(random.choice('0123456789') for _ in range(3))
        return letters + numbers
    else:
        # новый формат
        numbers = ''.join(random.choice('0123456789') for _ in range(4))
        letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))
        return numbers + letters

print(random_license_plate())