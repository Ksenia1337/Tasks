rom ex100 import random_password
from ex102 import is_good_password

def random_good_password():
    count = 0
    while True:
        password = random_password()
        count += 1
        if is_good_password(password):
            return password, count

password, count = random_good_password()
print(f'Надежный пароль: {password}')
print(f'Попытки: {count}')