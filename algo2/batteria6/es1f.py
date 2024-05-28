

def es1(n):
    f1 = [0]*n
    f0 = [0]*n
    f1[0]=1
    f0[0]=1
    for i in range(1,n):
        f1[i]=f0[i-1]
        f0[i]=f0[i-1]+f1[i-1]
    return f1[n-1]+f0[n-1]


#print(es1(4))

def es2(n):
    f01 = [0]*n
    f0 = [0]*n
    f11 = [0]*n
    f01[0]=1
    f0[0]=1
    f11[0]=0
    for i in range(1,n):
        f01[i]=f0[i-1]
        f11[i]=f01[i-1]       
        f0[i]=f0[i-1]+f01[i-1]+f11[i-1]
    return f01[n-1]+f0[n-1]+f11[n-1]


print(es2(4))


