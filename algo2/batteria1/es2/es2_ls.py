
def count_zero(l:list[int]) -> int:
    result = 0
    for i in l:
        if i == 0:
            result+=1
    return result

# O(n^3)
def es2ls(S: list[int], k:int ) -> int:
    #TODO il caso tutti 0 deve tornare n-1
    n = len(S)
    max_z_cnt = 0
    z_cnt = 0
    numbers = []
    for y in reversed(range(n + 1)):
        for x in range(n + 1):
            if x+(n-y) > n:
                break
            z_cnt += count_zero(S[:x])
            z_cnt += count_zero(S[y:]) 
            numbers.extend(S[:x])
            numbers.extend(S[y:])
            if sum(numbers) <= k:
                if max_z_cnt < z_cnt:
                    max_z_cnt = z_cnt
            z_cnt = 0
            numbers.clear()
    return max_z_cnt

def es2ls_new(S: list[int], k:int) -> int:
    #TODO il caso tutti 0 deve tornare n-1
    y = len(S)
    max_z_cnt = 0
    summ = 0
    for x in range(len(S)):
        if S[x] == 0:
            max_z_cnt += 1
        summ += S[x]
        if summ > k:
            summ -= S[x]
            x -= 1
            break
    
    z_cnt = max_z_cnt
    for y in reversed(range(len(S))):

        if x == y:
            x -= 1
            if x == -1:
                if max_z_cnt > z_cnt:
                    return max_z_cnt
                return z_cnt
            if S[x] == 0:
                if z_cnt > max_z_cnt:
                    max_z_cnt = z_cnt
                z_cnt -= 1
            summ -= S[x]

        summ += S[y]
        if S[y] == 0:
            z_cnt += 1

        while summ > k:
            x -= 1
            if x == -1:
                if max_z_cnt > z_cnt:
                    return max_z_cnt
                return z_cnt
            if S[x] == 0:
                if z_cnt > max_z_cnt:
                    max_z_cnt = z_cnt
                z_cnt -= 1
            summ -= S[x]
    assert False, "Qualcosa è vermante andato storto"
        

if __name__ == '__main__':
    lista = [1,0,2,8,0,5,1,6,0,0,3]
    k = 8
    print("SOLUZIONI CON INPUT: S = [1,0,2,8,0,5,1,6,0,0,3], k = 8")
    print("Soluzione O(n^3) Luca:    ",es2ls(lista,k))
    print("Soluzione O(n) Luca: ",es2ls_new(lista,k))
    print()

    lista = [0,0,0,0,0,0]

    print("SOLUZIONI CON INPUT: S = [0,0,0,0,0,0], k = 8")
    print("Soluzione O(n^3) Luca:    ",es2ls(lista,k))
    print("Soluzione O(n) di Luca: ",es2ls_new(lista,k))

    print()
