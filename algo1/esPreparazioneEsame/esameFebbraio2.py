
def ricor(n,M,colCnt,idx):
    if idx == (n*n):
        print(M)
        return
    M[idx] = 1
    ricor(n,M,colCnt,idx+1)
    if colCnt[idx%n]<n/2:
        M[idx] = 0
        colCnt[idx%n]+=1
        ricor(n,M,colCnt,idx+1)
        colCnt[idx%n]-=1

    return

def genMat(n):
    colCnt = [0]*n
    M = [None]*(n*n)
    ricor(n,M,colCnt,0)
    return


#genMat(2)


def zeriMinUgualiuni(n:int):
    M = [[None for _ in range(n)] for _ in range(n)]
    colCounter = [0]*n
    zeriMinUgualiuniBack(n,M,0,0,colCounter)
    return

def zeriMinUgualiuniBack(n,M,i,j,colz):
    if i == n:
        for i in range(n):
            print(M[i])
        print()
        return
    
    if colz[j] < n//2:
        M[i][j] = 0
        colz[j] += 1
        if j < n-1:
            zeriMinUgualiuniBack(n,M,i,j+1,colz)
        else:
            zeriMinUgualiuniBack(n,M,i+1,0,colz)
    
    M[i][j] = 1
    if j < n-1:
        zeriMinUgualiuniBack(n,M,i,j+1,colz)
    else:
        zeriMinUgualiuniBack(n,M,i+1,0,colz) 

zeriMinUgualiuni(2)