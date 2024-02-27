from math import sqrt

def is_prime(n: int) -> bool:
    for i in range(2,int(round(sqrt(n) + 1))):
        if n % i == 0:
            return False
    return True

def is_semiprime_complex(n: int) -> bool:
    
    for i in range(2,int(round(sqrt(n)+1))):
        if is_prime(i):
            q = n/i
            qa = int(q)
            if q - qa == 0:
                if is_prime(q):
                    return True
    return False

def is_semiprime(n: int) -> bool:
    trovato = False
    for i in range(2,int(round(sqrt(n)+1))):
        if n % i == 0:
            if not trovato:
                trovato = True
            else:
                return False
            
    return trovato
            

if __name__ == '__main__':
    print(is_semiprime_complex(int(15)))
    print(is_semiprime(15))