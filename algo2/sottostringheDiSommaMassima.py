
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


if __name__ == '__main__':
    esempio1 = [1,1,1,1,-1,-1] # 4
    esempio2 = [1,1,1,1,-1,-1,8] # 10
    esempio3 = [0] # 0
    esempio4 = [] # None
    esempio5 = [1,-1,-1] # 1
    esempio6 = [-1,-2] # -1 ?


    print(sommaMassima(esempio1)==4)
    print(sommaMassima(esempio2)==10)
    print(sommaMassima(esempio3)==0)
    print(sommaMassima(esempio4)==None)
    print(sommaMassima(esempio5)==1)
    print(sommaMassima(esempio6)==-1)