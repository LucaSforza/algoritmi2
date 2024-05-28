from math import inf

def cercaCore(caricoCore):
    idxc = 0
    min_pesoc = inf
    for ic,core in enumerate(caricoCore):
        if core<min_pesoc:
            min_pesoc = core
            idxc = ic

    return idxc

def assegnaProcessi(k,processi:list[int]):
    caricoCore = [0]*k
    processi.sort(reverse=True)
    assegnamento = [-1]*len(processi)
    for proc in processi:
        caricoCore[cercaCore(caricoCore)]+=proc
    return max(caricoCore)

if __name__=="__main__":
    # k = 5
    # processi = [3,90,80,5,5,100,3,3]
    k = 3
    processi = [1,1,1,1,1,1,1,1]
    print(assegnaProcessi(k,processi))