

def findMax(lista,i,j,mas=0):
    if i+1 == j:
        m = max(lista[i],lista[j])
        mas = max(mas,m)
    else:
        m = i+((j-i)//2)
        if lista[i]>lista[m]:
            mas  = findMax(lista,i,m,mas)

        if lista[m]>lista[j]:
            mas = findMax(lista,m,j,mas)
    return mas

def es9(lista):
    return findMax(lista,0,len(lista)-1)

esempio1 = [3,4,5,1,2]
esempio2 = [3,4,5,6,7,8,9,1,2]
esempio3 = [9,10,15,18,21,26,28,1,3,5,7]

print(es9(esempio1))
print(es9(esempio2))
print(es9(esempio3))