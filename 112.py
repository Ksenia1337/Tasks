a = list(map(int, input().split()))
print(a)
if len(a) < 4:
    print('неправильный ввод')
else:
    n = int(input())
    mi = [max(a)]
    ma = [min(a)]
    for i in a:
        if i <= mi[-1]:
            mi.append(i)
        if i >= ma[-1]:
            ma.append(i)
    ans = []
    for i in a:
        if mi[-n] < i < ma[-n]:
            ans.append(i)
