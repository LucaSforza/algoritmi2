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


if __name__ == '__main__':
    lista = [1,0,2,8,0,5,1,6,0,0,3]
    k = 8
    print("SOLUZIONI CON INPUT: S = [1,0,2,8,0,5,1,6,0,0,3], k = 8")
    print("Soluzione O(n) Filippo: ",es2filOn(lista,k))
    print("Soluzione Ricorsiva <complessità da dimostrare> Filippo: ",es2filR(lista,k))
    print()

    lista = [0,0,0,0,0,0]

    print("SOLUZIONI CON INPUT: S = [0,0,0,0,0,0], k = 8")
    print("Soluzione O(n) Filippo: ",es2filOn(lista,k))
    print("Soluzione Ricorsiva <complessità da dimostrare> Filippo: ",es2filR(lista,k))

    print()
