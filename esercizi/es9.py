G = [
    [9,2], # 1 -> 10,3
    [0,2,5,7], # 2 -> 1,3,6,8
    [], # 3
    [4,6], # 4 -> 5,7
    [10], # 5 -> 11
    [], # 6
    [9], # 7 -> 10
    [8], # 8 -> 9
    [], # 9
    [10], # 10 -> 11
    [3], # 11 -> 4
]

def count_pozzo(u: int, L: list[list[int]], V: list[int]):
    V[u] = True
    count = 0
    for x in L[u]:
        if not V[x]:
            if len(L[x]) == 0:
                count += 1
            count += count_pozzo(x,L,V)
    return count

if __name__ == '__main__':
    V = [False for _ in range(len(G))]
    print(count_pozzo(1,G,V))