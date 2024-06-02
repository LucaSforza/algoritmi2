
def piastrellamento(n: int) -> int:
    T = [1]*(n+1)
    T[2] = 2
    T[3] = 7
    T[4] = 15
    for i in range(4,n+1):
        T[i] = T[i-1] + T[i-2] + 4*T[i-3] + 2*T[i-4]
    return T[n]

if __name__ == '__main__':
    for j in range(5,10):
        print(piastrellamento(j)) 