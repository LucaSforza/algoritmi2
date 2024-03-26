# O(n)
def padre_in_comune(fathers_u: list[int], fathers_v: list[int],n: int) -> int:
    count = [0 for _ in range(n)] # O(n)
    
    if len(fathers_u) == len(fathers_v):
        pass
    elif len(fathers_u) > len(fathers_v):
        while len(fathers_u) > len(fathers_v):
            fathers_v.append(None)
    else:
        while len(fathers_u) < len(fathers_v):
            fathers_u.append(None)

    for u,v in zip(fathers_u,fathers_v): # O(n) se input corretti
        if u is not None:
            count[u] += 1
        if v is not None:
            count[v] += 1
        if count[u] == 2:
            return u
        if count[v] == 2:
            return v
    assert False, "Input sbagliati oppure errore fatale"

#TODO: contettualmente funziona in pratica no
def distanza(P: list[int],u: int, v: int) -> int:
    fathers_u = [u]
    fathers_v = [v]
    u_origin = u
    v_origin = v
    while True: # O(n)
        fathers_u.append(P[u])
        u = P[u]
        if P[u] == u:
            break
    
    while True: # O(n)
        fathers_v.append(P[v])
        v = P[v]
        if P[v] == v:
            break
    # O(n)
    padre_comune = padre_in_comune(fathers_u, fathers_v, len(P))
    count_u = 0
    while True:
        u_origin = P[u_origin]
        if u_origin == padre_comune:
            count_u += 1
            break
        if u_origin == P[u_origin]:
            count_u = 0
            break
        count_u += 1

    count_v = 0
    
    while True:
        v_origin = P[v_origin]
        if v_origin == padre_comune:
            count_v += 1
            break
        if v_origin == P[v_origin]:
            count_v = 0
            break
        count_v += 1

    return count_u + count_v

if __name__ == '__main__':
    list_in = [1, 1, 0, 1, 3, 2, 2, 8, 0]
    
    print(distanza(list_in, 8, 3))
    print(distanza(list_in,2,5))