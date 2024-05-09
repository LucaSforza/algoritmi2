'''
stampare tutte le stringhe binarie
'''

def es1(n,sol,i=0):
    if i == n:
        print(sol)
        return
    sol.append('0')
    es1(n,sol,i+1)
    sol.pop()
    sol.append('1')
    es1(n,sol,i+1)
    sol.pop()
    return 

esemp1 = '0101001001110100100'
#es1(len(esemp1),[])


'''
stampare tutte le stringhe binarie lunghe n dove sono contenuti c 1
'''
# Funzione di taglio
# faccio i soldi dal taglio come una parruchiera Funzione di taglio
def es2(n,sol,c,i=0):
    if i == n:
        print(sol)
        return
    sol.append('0')
    es1(n,sol,i+1)
    sol.pop()
    sol.append('1')
    es1(n,sol,i+1)
    sol.pop()
    #if sol.count('1')<=c:    n - (i - tot1) >= c-tot1

    return 

esemp1 = '0101001001110100100'
#es1(len(esemp1),4,[])


'''
ho strinche ternatie e voglio strinche lunghe n dove il numero delle b è maggiore degli alti simboli
'''
'''
bbb
bba
bbc
abb
cbb
bab
bcb
'''

def es3(n,sol,i=0,na=0,nc=0):
    if i==n:
        print(sol)
        return
    if n-nc-(na+1)>na+nc+1:
        sol.append('a')
        es3(n,sol,i+1,na+1,nc)
        sol.pop()    
    sol.append('b')
    es3(n,sol,i+1,na,nc)
    sol.pop()
    if n-na-(nc+1)>nc+na+1:
        sol.append('c')
        es3(n,sol,i+1,na,nc+1)
        sol.pop()
    return
'''
stringhe lunghe n 
alfabeto da 0 a k
somma della sottostringa deve fare t
'''



'''
progettare un algoritmo che data una stringa x lunga n stampa tutte le stringhe crescenti ottenibili cancekllando con un asterisco un numero 
'''

def es5(lista:list[int],sol:list[int],m, i = 0):
    if i+1 == len(lista):
        print(sol)
        return
    if lista[i]>=m:
        sol.append(lista[i])
        es5(lista,sol,lista[i],i+1)
        sol.pop()
    sol.append('*')
    es5(lista,sol,m,i+1)
    sol.pop()
    return 

esempio1 = [1,4,3,6,8,4,3,6,7,6,3,5,7,3,]
#es5(esempio1,[],esempio1[0])
def es1lez(n,sol,i=0,j=0):
    if i == n:
        for k in range(n):
            print(sol[i])
        print()
        return
    sol[i][j]=0
    if j < n-1:
        es1lez(n,sol,i,j+1)
    else:
        es1lez(n,sol,i+1,0)
    sol[i][j]=1
    if j < n-1:
        es1lez(n,sol,i,j+1)
    else:
        es1lez(n,sol,i+1,0)
    return

def eslez(n):
    sol = [[0]*n for _ in range(n)]
    es1lez(n,sol)
    return
