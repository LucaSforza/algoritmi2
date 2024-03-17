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
    fathers_u = []
    fathers_v = []
    u_origin = u - 1
    v_origin = v - 1
    while True: # O(n)
        fathers_u.append(P[u - 1])
        u = P[u - 1]
        if P[u - 1] == u:
            break
    
    while True: # O(n)
        fathers_v.append(P[v - 1])
        v = P[v - 1]
        if P[v - 1] == v:
            break
    # O(n)
    padre_comune = padre_in_comune(fathers_u, fathers_v, len(P))
    count_u = 0
    while True:
        u_origin = P[u_origin]
        if u_origin == padre_comune:
            break
        count_u += 1

    count_v = 0
    
    while True:
        v_origin = P[v_origin]
        if v_origin == padre_comune:
            break
        count_v += 1

    return count_u + count_v + 1

if __name__ == '__main__':
    list_in = [2, 2, 1, 2, 4, 3, 3, 9, 1]
    
    print(distanza(list_in, 9, 4))
    print(distanza(list_in,3,6))