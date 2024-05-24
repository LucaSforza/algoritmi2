def es(n,f,s):
    t = [[0]*(s+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(i,s+1):
            if i==j:t[i][j]=1
            else:
                for x in range(1,f+1):
                    if j-x>=0:
                        t[i][j]+=t[i-1][j-1]


def cercaCosto(costiPerPezzo,n):
    massimo = 0
    len_pezzo = None
    for i,prezzo in enumerate(1,costiPerPezzo):
        prezzo_pezzo = prezzo//i
        if prezzo_pezzo>massimo:
            massimo = prezzo_pezzo
            len_pezzo = i
    pezzi_venduti = n//len_pezzo
    guadagno = pezzi_venduti*prezzo_pezzo
    mancanti = n-pezzi_venduti
    if mancanti>1:
        return guadagno+cercaCosto(costiPerPezzo[:mancanti],mancanti)
    elif mancanti == 1:
        return costiPerPezzo[0]
    else:
        return 0

def cercaDivisibili(s,n):
    inizio = 0
    fine = 1
    cnt = 1
    in_seq = False
    while inizio < fine:
        if fine==inizio and fine < len(s)-1 :
                fine+=1
        else: return cnt
    
        string_in_esame = s[inizio:fine]
        somma = sum(string_in_esame)
        if somma % n == 0:
            in_seq = True 
            cnt += 1
            fine+=1
        elif in_seq:
            fine-=1
            in_seq = False
        elif not in_seq:
            inizio+=1
            if fine<=inizio:
                fine = inizio+ 1



    return cnt


if __name__=='__main__':
    n = 8
    costi = [0,1,5,8,9,10,17,17,20]
    #print(cercaCosto(costi,n))
    s = [3,3,5,8,8]
    s2 = [3,4,5,6]
    n = 3
    print(cercaDivisibili(s,n))