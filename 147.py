kartochki = [{'b': [0, 5, 14, 9, 13], 'i': [0, 18, 21, 26, 23], 'n': [0, 38, 37, 36, 42], 'g': [0, 52, 59, 57, 60], 'o': [0, 74, 62, 74, 64]},
             {'b': [7, 8, 14, 3, 4], 'i': [0, 0, 0, 0, 0], 'n': [31, 44, 40, 43, 35], 'g': [53, 51, 55, 46, 55], 'o': [66, 70, 61, 70, 74]},
             {'b': [0, 7, 13, 3, 3], 'i': [26, 0, 19, 16, 16], 'n': [42, 45, 0, 34, 33], 'g': [58, 58, 56, 0, 53], 'o': [61, 66, 64, 61, 0]},
             {'b': [4, 4, 5, 5, 4], 'i': [19, 24, 17, 26, 30], 'n': [32, 45, 43, 41, 43], 'g': [53, 59, 55, 47, 57], 'o': [69, 65, 66, 74, 68]}]
for u in range(len(kartochki)):
    a = False
    for i in range(5):
        if kartochki[u]['b'][i] + kartochki[u]['i'][i] + kartochki[u]['n'][i] + kartochki[u]['g'][i] + kartochki[u]['o'][i] == 0:
            a = True
    for i in 'bingo':
        if kartochki[u][i][0] + kartochki[u][i][1] + kartochki[u][i][2] + kartochki[u][i][3] + kartochki[u][i][4] == 0:
            a = True
    if kartochki[u]['b'][0] + kartochki[u]['i'][1] + kartochki[u]['n'][2] + kartochki[u]['g'][3] + kartochki[u]['o'][4] == 0 or kartochki[u]['b'][4] + kartochki[u]['i'][3] + kartochki[u]['n'][2] + kartochki[u]['g'][1] + kartochki[u]['o'][0] == 0:
        a = True
    print(a)
