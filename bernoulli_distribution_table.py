from functools import reduce


def f_1(n, p):
    w = [1]
    prob= []
    for k in range(1, n+1):
        w.append(w[-1] * (n - k + 1)//k)
    for i in range(len(w)):
        pr = w[i] * p **i*(1-p)**(n-i)
        prob.append(pr)
    return prob

wyn = [1]
def f_2(n, wyn, p):
    prob= []
    for k in range(1, n+1):
        wyn.append(wyn[-1] * (n - k + 1)//k)
    for i in range(len(wyn)):
        pr = wyn[i] * p **i*(1-p)**(n-i)
        prob.append(pr)
    return prob


def mnoz(a, b):
    return a * b

def f_3(n, k, p):
    sn = lambda n,k: reduce(mnoz, range(n, k+1))
    w = sn(k+1, n) // sn(1, n-k)
    prob = w * p**k * (1-p)**(n-k)
    return [prob]

def f_4(n, p, k = 0, o=[]):
    return f_4(n, p, k+1, o + f_3(n, k, p)) if k<n else o


def sum(a, b):
    return a + b

def silnia(n):
    x = 1
    for i in range(1, n+1):
        x *=i
    return x

def p_5(n):
    w = []
    o = []
    oo = []
    for a in range(n+1):
        for i in range(n+1):
            sn = silnia(n) // (silnia(i) * silnia(n-i))
            w.append(sn)
        wyn = w[a]
        o.append(wyn)
        oo.append(w[a])       
    return oo 

def sumowanie(d):
    w = reduce(sum, d)
    return w
 
def f_5(g, s):
    f = []
    for i in range(len(g)):
        f.append(g[i]/s)
    return f



def p_6(n,p,k):
    return (((n-k+1)*p) / (k*(1-p))) * p_6(n, p, k-1) if k!=0 else (1-p)**n

def f_6(n, p, t=[], k=0):
    return f_6(n, p, t +[p_6(n, p, k)], k+1) if k<n else t


def f_7(n,p):
    wyn = (1-p) ** n
    k = 0
    while (k<n):
        yield wyn
        wyn *= ((n-k) *p) / ((k+1) * (1-p))
        k+=1




print('f_1', f_1(5, 1/2))
print('f_2', f_2(5, wyn, 1/3))
print('f_3', f_3(5, 3, 1/3))
print('f_4', f_4(5, 1/3)) 
print('f_5', f_5(p_5(5), sumowanie(p_5(5))))
print('f_6', f_6(5, 1/3))
print('f_7')
for x in f_7(5, 1/2):
    print(x)

'''
# sprawdzenie szybkosci poszczegolnych funkcji z czesci pierwszej 

import time

tekst = "Czas: {} s, funkcja: {}"
n = 200
p = 1/2
funkcje = [f_1, f_4, f_6]
for f in funkcje:
    start = time.time()
    x = f(n, p)
    print(tekst.format(time.time()-start, f))


start = time.time()
x = f_2(n, wyn, p)
print(tekst.format(time.time()-start, f_2))

start = time.time()
x = f_5(p_5(n), sumowanie(p_5(n)))
print(tekst.format(time.time()-start, f_5))

# bez f_3 i f_7 bo ona zwraca tylko jedna wartosc a nie wszystkie

#wnioski --> w sprawozdaniu
'''

