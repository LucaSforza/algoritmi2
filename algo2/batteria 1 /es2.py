
def count_zero(l:list[int]) -> int:
    result = 0
    for i in l:
        if i == 0:
            result+=1
    return result

# O(n^3)
def es2(S: list[int], k:int ) -> int:
    #TODO il caso tutti 0 deve tornare n-1
    n = len(S)
    max_z_cnt = 0
    z_cnt = 0
    numbers = []
    for y in reversed(range(n + 1)):
        for x in range(n + 1):
            if x+(n-y) > n:
                break
            z_cnt += count_zero(S[:x])
            z_cnt += count_zero(S[y:]) 
            numbers.extend(S[:x])
            numbers.extend(S[y:])
            if sum(numbers) <= k:
                if max_z_cnt < z_cnt:
                    max_z_cnt = z_cnt
            z_cnt = 0
            numbers.clear()
    return max_z_cnt

def es2_new(S: list[int], k:int) -> int:
    #TODO il caso tutti 0 deve tornare n-1
    y = len(S)
    max_z_cnt = 0
    summ = 0
    for x in range(len(S)):
        if S[x] == 0:
            max_z_cnt += 1
        summ += S[x]
        if summ > k:
            summ -= S[x]
            x -= 1
            break
    
    z_cnt = max_z_cnt
    for y in reversed(range(len(S))):

        if x == y:
            x -= 1
            if x == -1:
                if max_z_cnt > z_cnt:
                    return max_z_cnt
                return z_cnt
            if S[x] == 0:
                if z_cnt > max_z_cnt:
                    max_z_cnt = z_cnt
                z_cnt -= 1
            summ -= S[x]

        summ += S[y]
        if S[y] == 0:
            z_cnt += 1

        while summ > k:
            x -= 1
            if x == -1:
                if max_z_cnt > z_cnt:
                    return max_z_cnt
                return z_cnt
            if S[x] == 0:
                if z_cnt > max_z_cnt:
                    max_z_cnt = z_cnt
                z_cnt -= 1
            summ -= S[x]
    assert False, "Qualcosa è vermante andato storto"

# ricorsivo filippo
def es2filR(ins:list[int],sogl:int,xIndex:int=0,yIndex:int=0)->int:
    insiemeInEsame = ins[:xIndex]+ins[len(ins)-yIndex:]
    sommaInsiemeInEsame = sum(insiemeInEsame)
    zcout= 0
    if sommaInsiemeInEsame <= sogl and xIndex+yIndex<len(ins):
        maxX = es2filR(ins,sogl,xIndex+1,yIndex)
        maxY = es2filR(ins,sogl,xIndex,yIndex+1)
        maxFigli = max(maxX,maxY)
        zc = insiemeInEsame.count(0)
        zcout = max(zc,maxFigli)
    return zcout

# sol O(n) filippo
def es2filOn(ins:list[int],sogl:int)->int:
    #TODO il caso tutti 0 deve tornare n-1
    maxNumZero = 0
    lenIns = len(ins)
    somma = 0 
    xIndex = 0
    numeroDiZeri = 0
    for x in range(lenIns):
        somma += ins[x]
        if ins[x] == 0:
            numeroDiZeri+=1
        xIndex = x 
        if somma <= sogl and x<lenIns:
            maxNumZero = max(numeroDiZeri,maxNumZero)
        else:
            break

    for y in range(lenIns):
        if xIndex==lenIns-y-1:
            somma -= ins[xIndex]
            if ins[xIndex]==0:
                numeroDiZeri-=1
            xIndex-=1
            if xIndex == -1:
                return maxNumZero
        somma += ins[lenIns-y-1]
        if ins[lenIns-y-1]==0:
                numeroDiZeri+=1
        
        
        if somma <= sogl:
            maxNumZero = max(numeroDiZeri,maxNumZero)
        else:
            somma -= ins[xIndex]
            xIndex-=1
            if xIndex == -1:
                return maxNumZero
            y-=1
        
        

if __name__ == '__main__':
    lista = [1,0,2,8,0,5,1,6,0,0,3]
    k = 8
    print("SOLUZIONI CON INPUT: S = [1,0,2,8,0,5,1,6,0,0,3], k = 8")
    print("Soluzione O(n^3) Luca:    ",es2(lista,k))
    print("Soluzione O(n) Luca: ",es2_new(lista,k))
    print("Soluzione O(n) Filippo: ",es2filOn(lista,k))
    print("Soluzione Ricorsiva <complessità da dimostrare> Filippo: ",es2filR(lista,k))
    print()

    lista = [0,0,0,0,0,0]

    print("SOLUZIONI CON INPUT: S = [0,0,0,0,0,0], k = 8")
    print("Soluzione O(n^3) Luca:    ",es2(lista,k))
    print("Soluzione O(n) di Luca: ",es2_new(lista,k))
    print("Soluzione O(n) Filippo: ",es2filOn(lista,k))
    print("Soluzione Ricorsiva <complessità da dimostrare> Filippo: ",es2filR(lista,k))

    print()
