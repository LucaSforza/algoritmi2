def crea(n,s):
    if len(s)==n:
        print(s)
        print(s[::-1])
        return
    else:
        crea(n,s+'0')
        crea(n,s+'1')
    return

def numZeri(n,k):
    partenza = '0'*k
    crea(n,partenza)
    return 

def crea2(n,k,s='',cnt=0):
    if len(s)==n:
        print(s)
        return
    else:
        if (cnt==k):
            crea2(n,k,s+'0',cnt)
            crea2(n,k,s+'1',cnt)
        else:
            crea2(n,k,s+'0',cnt+1)
            if n-len(s)-1>=k:
                crea2(n,k,s+'1',0)
    return

#crea2(4,2)


def contazerouno(s):
    T = [0]*len(s)
    cntz = 0
    for i in range(len(s)):
        if s[i]=='0':
            T[i]=T[i-1]
            cntz+=1
        elif s[i]=='1':
            if cntz!=0:
                T[i]=cntz+T[i-1]
    return T[-1]

#print(contazerouno('010010'))