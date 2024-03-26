def selezioneAttivita(lista:list[tuple[int,int]]):
    fun = lambda x : x[1]
    fun2 = lambda x,y:y
    lista.sort(key=fun2) # H(log n)
    sol = []
    libero = 0
    for inizio,fine in lista: # H(n)
        if inizio>=libero:
            sol.append((inizio,fine))
            libero = fine
    return sol


from heapq import heappop,heappush
def selezioneAttivita2(lista:list[tuple[int,int]]):
    lista.sort() # H(n log n)
    sol =[[]]
    libera,aula=0,0
    heap = [(libera,aula)]
    for inizio,fine in lista: # H(n)
        if heap[0][0]<inizio:
            libero,aula = heappop(heap) # O(log n)
            sol[aula].append((inizio,fine))
            heappush(heap,(fine,aula)) # O(log n)
        else:
            sol.append([(inizio,fine)])
            heappush(heap,(fine,len(sol)-1)) # O(log n)




lst = [(1,5),(6,11),(12,17),(18,22),(2,9),(10,13),(14,21),(3,8),(15,29),(4,7),(16,19)]
print(selezioneAttivita(lst))