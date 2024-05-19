
def es(n: int,i=0,sol=[]):
    if i == n:
        print(sol)
        return
    for j in [0,1,2]:
        if i==0 or (j == 1 or sol[i-1] == 1):
            sol.append(j)
            es(n,i+1,sol)
            sol.pop()
            
if __name__ == '__main__':
    es(3)
            
