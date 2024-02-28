
def count_zero(l:list[int]) -> int:
    result = 0
    for i in l:
        if i == 0:
            result+=1
    return result

# O(n^3)
def es2(S: list[int], k:int ) -> int:
    n = len(S)
    max_z_cnt = 0
    z_cnt = 0
    numbers = []
    for y in range(n):
        for x in range(n):
            if x+y >= n:
                break
            z_cnt += count_zero(S[:x])
            if y != 0:
                z_cnt += count_zero(S[-y:]) 
            numbers.extend(S[:x])
            if y != 0:
                numbers.extend(S[-y:])
            if sum(numbers) <= k:
                if max_z_cnt < z_cnt:
                    max_z_cnt = z_cnt
            z_cnt = 0
            numbers.clear()
    return max_z_cnt

def es2_new(S: list[int], k:int) -> int:
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

        if summ > k:
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
        

'''
Abbiamo una sequenza S di n interi ed una soglia k. Possiamo selezionare x elementi 
a sinistra di S e y elementi a destra di S a patto che risulti x+y <= n e la somma 
degli interi selezionati non superi k. Vogliamo sapere qul'e il numero massimo di 0 in S 
che e possibile selezionare.
Progettare un algoritmo che prende come parametri la sequenza S e la soglia k e restituisce
il valore massimo tra quelli delle diverse selezioni ammissibili.
Ad esempio: Per S = 1,0,2,8,0,5,1,6,0,0,3 e k = 8 la risposta deve essere 3 
(e si ottiene con x = 2 e y = 3).
• L’algoritmo deve avere complessit`a O(n3).
• L’algoritmo deve avere complessit`a O(n2).
• L’algoritmo deve avere complessit`a O(n log n). • L’algoritmo deve avere complessit`a O(n)
'''

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
    print("Soluzione O(n^3) Luca:    ",es2(lista,k))
    print("Soluzione <complessità da dimostrare> Filippo: ",es2filR(lista,k))
    print("Soluzione O(n) di Luca: ",es2_new(lista,k))
