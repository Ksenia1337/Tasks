a = []
for i in range(1, 10001):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0 and i != j:
            total += j
    if total == i:
        a.append(i)
print(a)