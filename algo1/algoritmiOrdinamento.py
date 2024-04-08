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
merge Sort

'''
def mergeSortIter(lista,a,b):
    n = len(lista)
    l = 1
    while l<n:
        i = 0
        while i-l<n:

            fondi(lista,i,i+l-1,i+2*l-1)
            i+=2*l
        l*=2

def mergeSortR(lista,i,j):
    if i<j:
        m = (i+j)//2
        mergeSortR(lista,i,m)
        mergeSortR(lista,m+1,j)
        out = fondi(lista,i,m,j)
        return out

def fondi(lista,a,m,b):
    i = a
    j = m+1
    listOut = []
    while i<=m and j<=b:
        if lista[i]<=lista[j]:
            listOut.append(lista[i])
            i+=1
        else:
            listOut.append(lista[j])
            j+=1
    return listOut

l1 = [2,4,6]
l2 = [1,3,5,7]
print(fondi(l1,l2))
# da sistemare

# esempio1 = [9,1,8,2,7,3,6,4,5]
# print(mergeSortR(esempio1,0,len(esempio1)-1))


'''
Quick Sort
'''

def quickSort(lista,a,b):
    S,C,D = [],[],[]
    if len(lista)==0:
        return lista
    p=lista[a]
    for i in range(len(lista)):
        if lista[i]<p: S.append(lista[i])
        elif lista[i]==p: C.append(lista[i])
        else: D.append(lista[i])
    return quickSort(S,0,len(S)-1)+C+quickSort(D,0,len(D)-1)

# esempio1 = [9,1,8,2,7,3,6,4,5]
# print(quickSort(esempio1,0,len(esempio1)-1))

