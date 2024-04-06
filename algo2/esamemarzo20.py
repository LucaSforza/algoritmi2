
def luca(n: int,k: int) -> int:
    pos = [0]*n
    fin = [k-1]*n
    count = 1
    while pos != fin:
        count+=1
        add_one(n-1,k,pos)
    return count

def add_one(ptr: int,k:int,pos:list[int]):
    pos[ptr]+=1
    if pos[ptr] == k and ptr!=0:
        pos[ptr] = add_one(ptr-1,k,pos)
    return pos[ptr]

def es2(n: int,k: int,seq:list[int]=None):
    counter = 0
    if seq is None:
        for num in range(k):  # H(k)
            counter+=es2(n,k,[num]) 
    elif len(seq) == n: #H(1)
        return 1
    elif len(seq) < k: 
        for nuovonumero in range(k):  #H(k)
            if nuovonumero>=seq[-1]:
                if len(seq) < k:
                    counter += es2(n,k,seq+[nuovonumero])
    return counter

print(es2(3,4))
print(luca(3,4))