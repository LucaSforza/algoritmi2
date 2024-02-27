from math import sqrt,ceil

# O(n^1/2)
def is_prime(n: int) -> bool:
    for i in range(2,int(round(sqrt(n) + 1))):
        if n % i == 0:
            return False
    return True

def is_primeR(n: int,start:int=2)->bool:
    if start>ceil(sqrt(n)):
        return True
    if n % start != 0:
        return is_primeR(n,start+1)
    else:
        return False

# O(n^3/2)
def is_semiprime_complex(n: int) -> bool:
    
    for i in range(2,int(round(sqrt(n)+1))):
        if is_prime(i):
            q = n/i
            qa = int(q)
            if q - qa == 0:
                if is_prime(q):
                    return True
    return False

# O(n^1/2)
def is_semiprime(n: int) -> bool:
    found = False
    for i in range(2,int(round(sqrt(n)+1))):
        if n % i == 0:
            if not found:
                found = True
            else:
                return False
            
    return found
            

if __name__ == '__main__':
    # number = int(input("Selezionare input: "))
    # print("Prima soluzione O(n^3/2):  ", is_semiprime_complex(number))
    # print("Seconda soluzione O(n^1/2):", is_semiprime(number))
    print(is_primeR(11))