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


ins1 = [1,0,2,8,0,5,1,6,0,0,3]
print(es2filR(ins1,8))
