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
    if n<=1 : return n
    return fibonacciRicorsivo(n-1)+fibonacciRicorsivo(n-2)
a = time()
fibonacciRicorsivo(100)
b = time()
print(b-a)


def fibonacciRicorsivo(n):
    if n==1 :
        fprima = 0
        fcorrent = 1
    else:
        fprima,fcorrent = fibonacciRicorsivo(n-1)

    return fcorrent,fprima+fcorrent

fibonacciRicorsivo(100)[1]
