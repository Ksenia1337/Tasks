import random
count = 0
consecutive = 0
last_flip = None
while consecutive < 3:
    flip = 'О' if random.randint(0, 1) == 0 else 'Р'
    count += 1
    if flip == last_flip:
        consecutive += 1
    else:
        consecutive = 1
    last_flip = flip
print("Количество попыток: ", count)