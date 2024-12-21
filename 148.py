from random import randint, shuffle


max_counter = 0
min_counter = 1000
c_counter = 0
for _ in range(1000):
    kal = [['b', b] for b in range(1, 16)]
    for i in [['i', b] for b in range(16, 31)]:
        kal.append(i)
    for i in [['n', b] for b in range(31, 46)]:
        kal.append(i)
    for i in [['g', b] for b in range(46, 61)]:
        kal.append(i)
    for i in [['o', b] for b in range(61, 76)]:
        kal.append(i)
    shuffle(kal)
    kartochka = {'b': [randint(1, 15) for _ in 'BINGO'],
                 'i': [randint(16, 30) for _ in 'BINGO'],
                 'n': [randint(31, 45) for _ in 'BINGO'],
                 'g': [randint(46, 60) for _ in 'BINGO'],
                 'o': [randint(61, 75) for _ in 'BINGO']}
    counter = 0
    while kal:
        counter += 1
        v = kal.pop(0)
        if v[1] in kartochka[v[0]]:
            kartochka[v[0]][kartochka[v[0]].index(v[1])] = 0
        a = False
        for i in range(5):
            if kartochka['b'][i] + kartochka['i'][i] + kartochka['n'][i] + kartochka['g'][i] + \
                    kartochka['o'][i] == 0:
                a = True
        for i in 'bingo':
            if kartochka[i][0] + kartochka[i][1] + kartochka[i][2] + kartochka[i][3] + kartochka[i][4] == 0:
                a = True
        if kartochka['b'][0] + kartochka['i'][1] + kartochka['n'][2] + kartochka['g'][3] + kartochka['o'][4] == 0 or kartochka['b'][4] + kartochka['i'][3] + kartochka['n'][2] + kartochka['g'][1] + kartochka['o'][0] == 0:
            a = True
        if a:
            break
    if counter > max_counter:
        max_counter = counter
    if counter < min_counter:
        min_counter = counter
    c_counter += counter
print(min_counter, max_counter, c_counter / 1000)
