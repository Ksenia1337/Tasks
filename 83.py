from random import randrange
nums = 100
mx_value = randrange(1, nums + 1)
print(mx_value)
num_updates = 0
for i in range(1, nums):
 current = randrange(1, nums + 1)
 if current > mx_value:
     mx_value = current
     num_updates = num_updates + 1
     print(current)
 else:
     print(current)
print("Максимальное значение в ряду:", mx_value)
print("Количество смен максимального значения:", num_updates)