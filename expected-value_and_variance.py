from bernoulli_distribution_table import sumowanie, f_1
from functools import reduce
#na podstawie przekazanej tabeli prawdopodobieństw
    
def ex(f):
    wyn = []
    for i in range(0, len(f)):
        w = i* f[i]
        wyn.append(w)
    #print(wyn)
    return sumowanie(wyn)


def ex2(f):
    wyn = []
    for i in range(0, len(f)):
        w = i**2* f[i]
        wyn.append(w)
    return sumowanie(wyn)


def var(f):
    v = ex2(f) - ex(f)**2
    return v


#na podstawie znajomości jego parametrów

def ex_2(n, p):
    w = [1]
    prob= []
    for k in range(1, n+1):
        w.append(w[-1] * (n - k + 1)//k)
    for i in range(len(w)):
        pr = w[i] * p **i*(1-p)**(n-i)
        prob.append(pr)
    wyn = []
    for i in range(0, len(prob)):
        w = i* prob[i]
        wyn.append(w)
    return sumowanie(wyn)


def ex2_2(n, p):
    w = [1]
    prob= []
    for k in range(1, n+1):
        w.append(w[-1] * (n - k + 1)//k)
    for i in range(len(w)):
        pr = w[i] * p **i*(1-p)**(n-i)
        prob.append(pr)
    wyn = []
    for i in range(0, len(prob)):
        w = i**2* prob[i]
        wyn.append(w)
    return sumowanie(wyn)


def var_2(n, p):
    v = ex2_2(n, p) - ex_2(n, p)**2
    return v

print('')
print('CZESC DRUGA')

print('sposob 1')

print('ex (wartosc oczekiwana)', ex(f_1(5, 1/2)))
print('ex2', ex2(f_1(5, 1/2)))
print('var', var(f_1(5, 1/2)))


print('sposob 2')

print('ex_2 (wartosc oczekiwana)', ex_2(5, 1/2))
print('ex2_2', ex2_2(5, 1/2))
print('var_2', var_2(5, 1/2))



'''
import time

# sprawdzenie co jest szybsze, sposob pierwszy czy drugi

funkcje = [ex, ex2, var]
funkcje_2 = [ex_2, ex2_2, var_2]
fun = f_1(1000, 1/12)
n = 1000
p = 1/2
tekst = "Czas: {} s, funkcja: {}"
for f in funkcje:
    start = time.time()
    print(f(fun))
    print(tekst.format(time.time()-start, f))
for f in funkcje_2:
    start = time.time()
    print(f(n, p))
    print(tekst.format(time.time()-start, f))


# wynik --> sposob drugi wolniejszy ale nieznacznie 
'''

