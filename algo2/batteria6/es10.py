def es(A: list[int],s: int) -> int:
    
    T = [[0]*len(A) for _ in range(s+1)]
    
    for i in range(s+1):
        for j in range(len(A)):
            if i == 0 or A[j] > i:
                T[i][j] = 0
            elif A[j] == i:
                T[i][j] = 1
            elif j == 0:
                T[i][j] = 0
            elif T[i-A[j]][j-1] == 0:
                T[i][j] = T[i][j-1]
            else:
                T[i][j] = max(T[i][j-1],T[i-A[j]][j-1]+1)
    return max(T[s])

#TODO: rivedere              

if __name__ == '__main__':
    A1 = [5,2,2,6,1,7,3,5,11,3,6]
    A2 = [3,3,5,13,3,5]
    s1 = 25
    s2 = 28
    print(es(A1,s1))
    print(es(A2,s2))