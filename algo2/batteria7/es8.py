
def es(n: int) -> None:
    M = [[1]*n for _ in range(n)]
    es1(M)
    
def es1(M: list[list[int]],i=0,j=0):
    n = len(M)
    if j == n:
        for row in M:
            print(row)
        print()
        return
    prima = M[i][j]
    for x in range(1,4):
        if i==j==0 or ((i==0 or M[i-1][j]) <= x and (j==0 or M[i][j-1] <= x)):
            M[i][j] = x
            if i + 1== n:
                es1(M,0,j+1)
            else:
                es1(M,i+1,j)
            M[i][j] = prima

if __name__ == '__main__':
    es(2)