def es(S: list[int]) -> int:
    T = [0]*len(S)
    
    for i in range(len(S)):
        if i==0:
            T[i] = S[i]
        elif i==1:
            T[i] = max(S[0],S[1])
        else:
            T[i] = max(T[i-1],T[i-2]+S[i])
    return T[len(S)-1]

if __name__ == '__main__':
    print(es([1,5,4,6,10,3,2,9]))