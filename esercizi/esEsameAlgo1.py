"""
Dato un array A di n interi compresi fra 0 e 50, sapendo che nell'array sono certamente presenti
dei duplicati, si vuole determinare la distanza massima tra le posizioni di due elementi duplicati di A
Ad esempio A = [3,3,4,6,6,3,5,5,5,6,6,9,9,1]
"""

# O(n)
def es2(A: list[int]) -> int:
    D = [[0,0] for _ in range(50)] # O(1)
    for i,n in enumerate(A):
        if D[n][0] == 0:
            D[n][0] = i
        else:
            D[n][1] = i - D[n][0]
    return max(D,key=lambda x:x[1])[1]

class Nodo:
    def __init__(self,key, left = None ,right = None) -> None:
        self.key = key
        self.left = left
        self.right = right

def init_albero() -> Nodo:
    return Nodo(0,Nodo(2,Nodo(1),Nodo(7,Nodo(9))),Nodo(5,Nodo(6),Nodo(-40,Nodo(-35))))

def es3(r: Nodo) -> int:
    if r is None:
        return 0
    count = 0
    if r.key % 2 == 0 and  r.left is not None and r.right is not None:
        count += 1
    return es3(r.left) + es3(r.right) + count

if __name__ == '__main__':
    A = [3,3,4,6,6,3,5,5,5,6,6,9,9,1]
    print(es2(A))
    print(es3(init_albero()))