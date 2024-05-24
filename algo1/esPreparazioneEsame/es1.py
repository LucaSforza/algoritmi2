
def best_combinazione_capienza(a,capienza,salvati,i=0):
    
    if a == [] or capienza == 0:
        return []
    elelemto = a[0]
    if capienza - elelemto>=0:
        
        prendo,pesop = best_combinazione_capienza(a[1:],capienza-elelemto,i+1)
    lascio,pesol = best_combinazione_capienza(a[1:],capienza,i+1)

    if pesop>pesol:
        prendo.append(i)
        return prendo,pesop+elelemto
    else:
        lascio.append(i)
        return lascio,pesol+elelemto

if __name__=='__main__':
    a = [82,15,40,95,31,50,40,28]
    c = 100
    print(best_combinazione_capienza(a,c,[]))