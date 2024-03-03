from math import sqrt

def isPrime(n:int)->bool:
    for num in range(2, round(sqrt(n))+1):
        if n % num == 0:
            return False
    return True


def generatePrime(n:int)->list[int]:
    primeList = []
    for num in range(2, round(sqrt(n))+1):
        if isPrime(num):
            primeList.append(num)
    return primeList


print(generatePrime(50))


