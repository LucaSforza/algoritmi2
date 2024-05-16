'''
abbiamo un vettore una lista di interi positivi e un intero k 
vogliom sapere se nella lista é presente un insieme di elementi la cui somma è k
'''
def es(A,k):
    nodo = 0
    def somma(A,k,sol,i=0,tot = 0):
        nonlocal nodo
        nodo+=1
        if k == tot:
            return True 
        if i==len(A)-1:
            return False 
        sol.append(A[i])
        if somma(A,k,sol,i+1,tot+A[i])==True:return True
        sol.pop()
        if somma(A,k,sol,i+1,tot)==True: return True
        return False
    
    sol = []
    x = somma(A,k,sol)
    print(nodo)
    if x==True:
        return sol
    return




if __name__=="__main__":
    A = [61,20,1,33,20,2,4,1,1,33]
    print(es(A,70))
