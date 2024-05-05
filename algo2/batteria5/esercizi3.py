
def es(V,i,j):
    if i == j: return V[i] == i
    m = (i+j)//2
    if V[m] == m: return True
    if V[m] > m:
        return es(V,i,m)
    else:
        return es(V,m,j)

if __name__ == '__main__':
    V = [5,6,7,8]
    print(es(V,0,len(V)-1))
    V = [0,2,3]
    print(es(V,0,len(V)-1))