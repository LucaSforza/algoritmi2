from math import inf

def coin_change(C: int, A: list[int]) -> int:
    T = [inf]*(C+1)
    T[0] = 0
    for i in range(1,C+1):
        min_c = inf
        for j in A:
            if j == i:
                min_c = 1
                break
            if j < i and T[i-j] != inf:
                min_c = min(T[i-j] + 1,min_c)
        T[i] = min_c
    if T[C] == inf:
        return -1
    return T[C]

if __name__ == '__main__':
    c1 = 8
    c2 = 62
    A  = [5, 7, 10, 25] 
    print(coin_change(c1,A))
    print(coin_change(c2,A))