'''
calcolare tutte le stringhe binarie lunghe 2n dove la somma delle prime n cifre è uguale alla somma delle 
seconde n cifre 
''' 
import math
def es1(n):
    t = [1]*(n+1)
    somma = 0
    for i in range(1,n+1):
        t[i] = t[i-1]*i
    for i in range(n+1):
        somma += (t[n]//t[n-i]*t[i])**2

def esmio(n,card_alfabeto):
    t = [None]*(n+1)
    prec = n
    t[0]=1
    t[n]=1
    mezzo = math.ceil(n/2)
    for i in range(1,mezzo+1):
        t[i] = t[i-1]*(prec)
        prec-=1
    # for i in range(0,mezzo):
    #     t[mezzo+i]=t[mezzo-i-1]
    print(t)
    # for i in range(n):
    #     ris+=t[i]*t[i]
    # return ris

# print(esmio(3,2))
# print(esmio(4,2))

def provrico(n,ls,t,somma=0):
    if n==ls:
        t[somma]+=1
        return
    provrico(n,ls+1,t,somma+1)
    provrico(n,ls+1,t,somma)
    return 

def esr(n):
    t = [0]*(n+1)
    provrico(n,0,t)
    ris = 0
    for i in range(n+1):
        ris+=t[i]**2
    print(t)
    return ris


print(esr(4))

        

    



