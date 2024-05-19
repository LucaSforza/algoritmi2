
def es(A: str, B:str, C:str) -> bool:
    T = [[False]*(len(B)+1) for _ in range((len(A)+1))]
         
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if i==0 and j==0:
                T[i][j] = True
            elif i==0:
                T[i][j] = T[0][j-1] and C[j-1]==B[j-1]
            elif j==0:
                T[i][j] = T[i-1][0] and C[i-1]==A[i-1]
            elif C[i+j-1] == A[i-1]:
                T[i][j] = T[i-1][j]
            elif  C[i+j-1]==B[j-1]:
                T[i][j] = T[i][j-1]
    return T[len(A)][len(B)]

if __name__ == '__main__':
    print(es('aabxxz','abxy','abaaxbxyxz'))