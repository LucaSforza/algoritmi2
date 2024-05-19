def es(S: str):
    n = len(S)
    i = j = start = 0

    T = [[-1] * n for _ in range(n)]

    while True:
        if i == j:
            T[i][j] = 0
        elif i + 1 == j and S[i] != S[j]:
            T[i][j] = 1
        elif i + 1 == j and S[i] == S[j]:
            T[i][j] = 0
        elif S[i] != S[j]:
            T[i][j] = min(T[i+1][j],T[i][j-1]) + 1
        elif S[i] == S[j]:
            T[i][j] = T[i + 1][j - 1]
        if j == n - 1:
            i = 0
            j = start + 1
            start += 1
            if start == n:
                break
            continue
        i += 1
        j += 1
    return T[0][n-1]


S = "cic"
print(es(S))