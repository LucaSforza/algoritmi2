

def es1(s):
    n = len(s)
    T = [1]*n 
    for i in range(n):
        for j in range(i):
            if s[i]%s[j]==0 and T[i]<T[j]+1:
                T[i]= T[j]+1
    print(T)
    return max(T)

def es2(s,out = ''):
    pos = len(out)
    if pos == len(s):
        print(out)
        return
    for new in ['0','1','2']:
        if s[pos]!=new:
            if out == '' or new!=out[-1]:
                es2(s,out+new)
    return




if __name__=='__main__':
    # s2 = [1,3,6,13,17,18]
    # s1  = [3,5,10,20]
    # s3 = [2,4,8,16,19,304]
    # print(es1(s3))
    st1 = '2001'
    es2(st1)