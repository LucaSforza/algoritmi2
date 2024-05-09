
# si comporta bene se gli elementi all'interno del vettore da ordinare sono equidistribuiti 
# (uniformemente distribuiti)


def bucketSort(lista,k):
    b = [[] for _ in range(k)] #H(k) k è al massimo n 
    m = max(lista)  #H(n)
    for x in lista: #H(n)
        i = x*k//(m+1)
        b[i].append(x)
    for i in range(k):
        b[i].sort()
    c = []
    for i in range(k):
        c.extend(b[i])
    return c

list1 = [4, 3, 2, 1]
# Expected: [1, 2, 3, 4]

list2 = [64, 34, 25, 12, 22, 11, 90]
# Expected: [11, 12, 22, 25, 34, 64, 90]

list3 = [10, 7, 8, 9, 1, 5]
# Expected: [1, 5, 7, 8, 9, 10]

print(bucketSort(list1,2)==[1, 2, 3, 4])
print(bucketSort(list2,2)==[11, 12, 22, 25, 34, 64, 90])
print(bucketSort(list3,2)==[1, 5, 7, 8, 9, 10])

