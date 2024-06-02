
def es(M: list[list[int]]) -> int:
    T = [[0]*len(M[0]) for _ in range(len(M))]
    
    for i in range(len(M)):
        for j in range(len(M[0])):
            min1 = 1
            min2 = 1
            if i != 0 and M[i-1][j] + 1 == M[i][j]:
                min1 = T[i-1][j] + 1
            if j != 0 and M[i][j-1] + 1 == M[i][j]:
                min2 = T[i][j-1] + 1
            T[i][j] = max(min1,min2)
            
    for i in reversed(range(len(M))):
        for j in reversed(range(len(M[0]))):
            min1 = 1
            min2 = 1
            if i != len(M)-1 and M[i+1][j] + 1 == M[i][j]:
                min1 = T[i+1][j] + 1
            if j != len(M[0])-1 and M[i][j+1] + 1 == M[i][j]:
                min2 = T[i][j+1] + 1
            T[i][j] = max(T[i][j],min1,min2)
    maxx = 0
    for l in T:
        for x in l:
            maxx = max(maxx,x)
    return maxx

if __name__ == '__main__':
    M1 = [
        [3,6,2],
        [7,1,9],
        [4,8,5],
    ]
    M2 = [
        [9,7,6],
        [8,2,5],
        [1,3,4],
    ]
    
    print(es(M1))
    print(es(M2))