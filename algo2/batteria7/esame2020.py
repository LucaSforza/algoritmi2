
def es(M: list[list[int]],i=0,j=0,sol=[]) -> None:
    if i == len(M):
        print(sol)
        return
    if i == 0:
        for k in range(len(M[0])):
            sol.append(M[i][k])
            es(M,i+1,k,sol)
            sol.pop()
        return
    if j!=0:
        sol.append(M[i][j-1])
        es(M,i+1,j-1,sol)
        sol.pop()
    sol.append(M[i][j])
    es(M,i+1,j,sol)
    sol.pop()
    if j!= len(M)-1:
        sol.append(M[i][j+1])
        es(M,i+1,j+1,sol)
        sol.pop()

if __name__ == '__main__':
    M = [
        [12, 10, 3, 14, 9],
        [0, 1, 13, 15, 13],
        [8, 10, 1, 2, 7],
        [7, 11, 10, 5, 7],
        [18, 4, 6, 10, 0],
    ]
    es(M)