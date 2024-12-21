from random import randint
kartochka = {'b': [randint(1, 15) for _ in 'BINGO'],
             'i': [randint(16, 30) for _ in 'BINGO'],
             'n': [randint(31, 45) for _ in 'BINGO'],
             'g': [randint(46, 60) for _ in 'BINGO'],
             'o': [randint(61, 75) for _ in 'BINGO']}
print(kartochka)
print('B  I  N  G  O')
for i in range(5):
    print(str(kartochka['b'][i]).ljust(2),
          str(kartochka['i'][i]).ljust(2),
          str(kartochka['n'][i]).ljust(2),
          str(kartochka['g'][i]).ljust(2),
          str(kartochka['o'][i]).ljust(2))
