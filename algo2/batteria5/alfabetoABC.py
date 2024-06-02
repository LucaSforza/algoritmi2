
C = ['abc','acb','bac','bca','cab','cba','aba','aca','bab','bcb','cac','cbc']

def es(n: int) -> int:
    T = [[1]*12 for _ in range(n+1)]

    for i in range(2,n+1):
        for j,c in enumerate(C):
            count = 0
            for y,c1 in enumerate(C):
                if c1[0] != c[0] and c1[1] != c[1] and c1[2] != c[2]:
                    count += T[i-1][y]
            T[i][j] = count
    
    return sum(T[n])
    
if __name__ == '__main__':
    print(es(8))