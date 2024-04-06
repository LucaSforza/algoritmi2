# H(n^2)
# insertionSort    selectionSort    bubleSort

# H(n logn)
# mergeSort  quickSort   heapSort

'''
selsction sort 
cerca il minimo nella lista disordinata e quando lo trova lo sposta all'inizio della lista 
H(n)*O(n) = O(n^2)
'''

def selectionSort(lista:list[int])->list[int]:
    n = len(lista)-1
    for i in range(n-1): # H(n)
        min = i
        for j in range(i+1,n): # O(n)
            if lista[min]>lista[j]:
                min = j
        lista[i],lista[min]=lista[min],lista[i]


'''
insertion Sort
cerca il minimo nella lista disordinata e quando lo trova lo sposta all'inizio della lista 
H(n)*O(i) = O(n^2)
'''
def insertionSort(A:list[int])->list[int]:
    n = len(A)
    for i in range(1,n): # H(n)
        x = A[i]
        j = i-1
        while j>=0 and A[j]>x: # O(i)
            A[j+1]=A[j]
            j = j-1
        A[j+1]=x

'''
buble Sort
confronta il primo elemento con il secondo se e maggiore li scambia, 
poi lo confronta con tutti gli altri
'''

def bubleSort(A:list[int])->list[int]:
    n = len(A)
    for i in range(n-1): #H(n)
        for j in range(n-1-i): # O(n)
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return

'''

'''
