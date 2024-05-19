def es(x: str, y:str) -> int:
    
    T = [[-1]*(len(y)+1) for _ in range(len(x)+1)]
    
    return minima(x,0,y,0,T)

def minima(
    x: str,
    i: int,
    y:str,
    j: int,
    T: list[list[str]]
) -> int:
    """più corta sequenza che contiene due sequenze"""
    if T[i][j] > 0:
        return T[i][j]
    if i == len(x):
        T[i][j] = len(y)-j-1
        return len(y)-j-1
    if j == len(y):
        T[i][j] = len(x)-i-1
        return len(x)-i-1
    if x[i] != y[j]:
        lx = minima(x,i+1,y,j,T)
        ly = minima(x,i,y,j+1,T)
        if lx < ly:
            T[i][j] = lx + 1
            return 1+lx
        T[i][j] = ly+1
        return 1+ly
    else:
        l = minima(x,i+1,y,j+1,T)
        T[i][j] = 1+l
        return 1+l

if __name__ == '__main__':
    print(es("alberi","libri"))