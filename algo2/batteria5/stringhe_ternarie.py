

def stringhe_ternarie(n: int) -> int:
    T = [[1,1,1] for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(3):
            if j == 1:
                T[i][j] = sum(T[i-1])
            else:
                T[i][j] = T[i-1][1] + T[i-1][j]
    return sum(T[n])

def stringhe_quaternarie(n: int) -> int:
    """
        Dato n > 0 restituire le stringhe nell'alfabeto {0,1,2,3}
        t.c. non ci siano dispari adicacenti
    """
    T = [[1,1,1,1] for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(4):
            if j % 2 == 0:
                T[i][j] = sum(T[i-1])
            else:
                T[i][j] = T[i-1][0]+T[i-1][2]
    return sum(T[n])

def stringhe_decimali(n: int) -> int:
    """ Vogliamo il numero di sequenze decimali di lunghezza n in cui
non appaiono cifre pari adiacenti. Progettare un algoritmo che prende come
parametro l’intero n e, in tempo O(n), restituisce il numero delle sequenze cui
siamo interessati.

T[i][j] = numero di cifre decimali che terminano con j
    0<=j<10

    caso base: se i = 1 allora T[i][j] = 1
"""
    T = [[1 for _ in range(10)] for _ in range(n+1)]
    
    for i in range(2,n+1):
        for j in range(10):
            if j % 2 == 1:
                T[i][j] = sum(T[i-1])
            else:
                T[i][j] = 0
                for k,c in enumerate(T[i-1]):
                    if k % 2 == 1:
                        T[i][j] += c
    return sum(T[n])

if __name__ == '__main__':
    print(stringhe_ternarie(9))
    print(stringhe_quaternarie(9))
    print(stringhe_decimali(5))