import time
def es1(n):
    print("ciao")
    return es1(n-1)

#es1(100)

def fibonacciIterativo(n):
    if n<=1 : return n
    a,b= 0,1
    for i in range(2,n+1):
        a,b= b,a+b
    return b


def fibonacciRicorsivo(n):
    if n<=1 : 
        return n
    return fibonacciRicorsivo(n-1)+fibonacciRicorsivo(n-2)



def fibonacciRicorsivo2(n):
    if n==1 :
        fprima = 0
        fcorrent = 1
    else:
        fprima,fcorrent = fibonacciRicorsivo2(n-1)

    return fcorrent,fprima+fcorrent


print('fibonacci(80)')
a = time.time()
fibonacciIterativo(80)
b = time.time()
print('tempo fibonacciIterativo: '+str(b-a))

c = time.time()
fibonacciRicorsivo(80)
d = time.time()
print('tempo fibonacciRicorsivo: '+str(d-c))

e = time.time()
fibonacciRicorsivo2(80)
f = time.time()
print('tempo fibonacciRicorsivo2: '+str(f-c))
