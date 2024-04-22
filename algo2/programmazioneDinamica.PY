'''
input:
    - lista di interi dove ogni intero è la grandezza di un file
    - c capienza del singolo hard disk


'''

def findSol(file,c):
    n = len(file+1)
    T = [[0]*(c+1) for _ in range(n)]
    for i in range(1,n):
        for j in range(1,c+1):
            if j<file[i-1]:  # se non sta nella capienza non lo metto proprio 
                T[i][j]=T[i-1][j]
            else: # se ci sta cerco di metterlo nella soluzione migliore precedentemente  calcolata
                T[i][j]= max(T[i-1][j],file[i-1]+T[i-1][j-file[i-1]])
    return T[n][c]


'''
dato un numero n voglio sapere quante sono le stringhe binarie lunghe n che non contengono 2 zeri consecutivi 

'''

def nString(n):
    T = [1]*(n+1)
    T[1]=2
    for i in range(2,n+1):
        T[i] = T[i-1]+T[i-2]

'''
dato un numero n voglio sapere quante sono le stringhe binarie lunghe n che non contengono 3 zeri consecutivi 

'''






'''
date n persone in quanti modi posso metterli in stanze o da uno o da due riempendole
'''

def riempiStanze(n):
    T = [1]*(n+1)
    for i in range(2,n+1):
        T[i]=T[i-1]+(i-1)*T[i-2]
        return T[n]

'''
ho un vettore di interi positivi voglio sapere la somma massima di elementi non consecutivi
'''







'''
fibonacci chiuso ??
'''

import math

def fibonacci(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi**n - psi**n) / sqrt_5)

print(fibonacci(7))