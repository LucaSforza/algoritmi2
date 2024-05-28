class Punto:
    def __init__(self,key = None , next = None):
        self.key = key
        self.next = next

def es_31_01_2023(l:Punto,somma=0):
    if l==None:
        return None
    elif somma==l.key:
        return l
    else:
        out = es_31_01_2023(l.next,somma+l.key)

    return out

if "__main__" == __name__:
    l = Punto(1,Punto(2,Punto(3,Punto(6))))
    print(es_31_01_2023(l).key)


