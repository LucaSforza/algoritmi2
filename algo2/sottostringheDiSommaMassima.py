
def sommaMassima(lista):
    if lista == []:
        return None
    massimo = lista[0]
    curr = 0
    for num in lista:
        if curr+num>massimo:
            curr+=num
            massimo = curr
        elif curr+num>=0:
            curr+=num
        elif curr+num<0:
            curr = 0
    return massimo

esempio1 = [1,1,1,1,-1,-1] # 4
esempio2 = [1,1,1,1,-1,-1,8] # 10
esempio3 = [0] # 0
esempio4 = [] # None
esempio5 = [1,-1,-1] # 1
esempio6 = [-1,-2] # -1 ?


print(sommaMassima(esempio1))
print(sommaMassima(esempio2))
print(sommaMassima(esempio3))
print(sommaMassima(esempio4))
print(sommaMassima(esempio5))
print(sommaMassima(esempio6))