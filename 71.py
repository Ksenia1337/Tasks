p=3
pis = []
for i in range(15):
    if (i+1) %2==0:
        p= p-(4/((2+2*i)*(3+2*i)*(4+2*i)))
    else:
        p= p+(4/((2+2*i)*(3+2*i)*(4+2*i)))
    pis.append(p)
print(pis)