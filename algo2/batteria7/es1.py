

def stampaStringhe1(n,s='',maxa=0,lasta=0):
    if n ==0:
        print(s)
        return
    if maxa%2==0:
        stampaStringhe1(n-1,s+'b',lasta,0)
    if n>1:
        stampaStringhe1(n-2,s+'aa',maxa,0)
    
    return 

def stampaStringhe2(n,s='',acnt=0,bcnt=0):
    if n ==0:
        print(s)
    else:
        if n>1 or acnt%2==0:
            stampaStringhe2(n-1,s+'a',acnt+1,bcnt)
        if n>1 or bcnt%2==0:
            stampaStringhe2(n-1,s+'b',acnt,bcnt+1)
    return 


def stampaStringhe3(n,s=''):
    if n%2==1:
        stampaStringhe3(n-1,'a')
        stampaStringhe3(n-1,'b')
    else:
        if n==0:
            print(s)
        else:
            stampaStringhe3(n-2,'a'+s+'a')
            stampaStringhe3(n-2,'b'+s+'b')
    return

def stampaStringhe4(n,s='',lastadd=None):
    if n==0:
        print(s)
    else:
        if s=='':
            stampaStringhe4(n-1,'1',1)
            stampaStringhe4(n-1,'2',2)
            stampaStringhe4(n-1,'3',3)
            stampaStringhe4(n-1,'4',4)
        else:
            dx2 = lastadd+2
            dx3 = lastadd+3
            if dx2<5:
                stampaStringhe4(n-1,s+str(dx2),dx2)
            if dx3<5:
                stampaStringhe4(n-1,s+str(dx3),dx3)
            sx2 = lastadd-2
            if sx2>0:
                stampaStringhe4(n-1,s+str(sx2),sx2)
            sx3 = lastadd-3
            if sx3>0:
                stampaStringhe4(n-1,s+str(sx3),sx3)
    return

def stampaStringhe5(n,s=''):
    if n ==len(s):
        print(s)
    else:
        for t in range(1,n+1):
            if s == '' or (int(s[-1])%2 != t%2 and str(t) not in s):
                stampaStringhe5(n,s+str(t))
    return

def stampaStr6(n,m,k,kcnt,s=''):
    if len(s)==n:
        print(s)
    else:
        for num in range(1,m+1):
            if kcnt[num]<k:
                kcnt[num]+=1
                stampaStr6(n,m,k,kcnt,s+str(num))
                kcnt[num]-=1

    return

def stampaStringhe6(n,m,k):
    kcnt = [0]*n
    stampaStr6(n,m,k,kcnt)
    return

if __name__=="__main__":
    stampaStringhe6(3,2,2)