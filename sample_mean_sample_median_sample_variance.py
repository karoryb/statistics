from bernoulli_distribution_table import sumowanie, f_1

def srednia(x):
    return sumowanie(x)/len(x)


def mediana(f):
    lf = len(f)

    # sortowanie 
    for i in range(lf):
        for j in range(i + 1, lf):
            if f[i] > f[j]:
                f[i], f[j] = f[j], f[i]

    # w zaleznosci czy podana lista bedzie parzysta czy nie obliczanie mediany 
    if lf % 2 != 0:
        med = f[lf//2]
    else:
        pierw_l_srod = lf//2 
        med = f[(pierw_l_srod + pierw_l_srod +1)//2]
    return med

def wariancja(f):
    lista = []
    for i in range(0, len(f)):
        lista.append((f[i] - srednia(f))**2)
    v = sumowanie(lista)
    return v/(len(f)-1)


print('')
print('CZESC TRZECIA')

# przyklad
a = [1, 3, 4, 6, 7, 9, 23]
print('srednia z listy a', srednia(a))
print('mediana z listy a', mediana(a))
print('wariancja z listy a', wariancja(a))

# wykorzystując dane z rozkładu
x = list(range(0, len(f_1(5, 1/2))))
print('srednia', srednia(x))
print('mediana', mediana(f_1(5, 1/2)) )
print('wariancja', wariancja(x))

'''
# porownanie szybkosci dzialania funkcji ex, ex_2  i srednia

import time

tekst = "Czas: {} s, funkcja: {}"
a = f_1(1000, 1/2)
funkcje = [ex, srednia]
for f in funkcje:
    start = time.time()
    x = f(a)
    print(tekst.format(time.time()-start, f))

start = time.time()
x = ex_2(1000, 1/2)
print(tekst.format(time.time()-start, ex_2))

# wniosek --> zblizony czas bliski 0, nieznaczaca roznica pomiędzy funkcjami 
'''