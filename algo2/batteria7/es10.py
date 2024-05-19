def es(n: int):
    nodo = 0
    I = [0]*(n**2+1)
    C = [0]*n
    M = [[0]*n for _ in range(n)]
    def es1(M: list[list[int]],n: int, I:list[int], C: list[int],i=0,j=0,sr=0,sd=0,sda=0):
        nonlocal nodo 
        nodo += 1
        limite = (n*(n**2+1))//2
        if i == n:
            giusto = True
            for row in M:
                if sum(row) != limite:
                    giusto = False
            for j in range(n):
                summ = 0
                for i in range(n):
                    summ+=M[i][j]
                if summ != limite:
                    giusto = False
            summ = 0
            for i in range(n):
                summ+= M[i][i]
            if summ != limite:
                giusto = False
            j = 0
            summ = 0
            for i in reversed(range(n)):
                summ += M[j][i]
                j+=1
            if summ != limite:
                giusto = False
            if not giusto:
                print("ERROR: non funziona qua")
            for row in M:
                print(row)
            print()
            return
        prima = M[i][j]
        for k in range(1,n**2+1):
            if I[k] == 0 and ( k+sr <= limite and k+C[j] <= limite):
                if i ==j==n-1 and sd+k != limite:
                    continue
                if i == n-1 and j == 0 and sda+k != limite:
                    continue
                if i==j and sd + k > limite:
                    continue
                if i+j == n-1 and sda + k > limite:
                    continue
                M[i][j] = k
                I[k] = 1
                C[j]+=k
                if i==j:
                    sd += k
                if i+j == n - 1:
                    sda += k
                if j < n-1:
                    es1(M,n,I,C,i,j+1,sr+k,sd,sda)
                else:
                    es1(M,n,I,C,i+1,0,0,sd,sda)
                I[k] = 0
                C[j] -= k
                if i==j:
                    sd -= k
                if i+j == n - 1:
                    sda -= k
                M[i][j] = prima
    
    es1(M,n,I,C)
    print(nodo)

        
        

if __name__ == '__main__':
    es(4)