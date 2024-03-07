# algoritmo con H(1) perche dopo 100 torna sempre 1
def es1_1(n)->int:
      t = 0 
      n = abs(n)  # H(1)
      if n>100:   # H(1)
        return 1
      else:
        for i in range(n):
            t+=3
        return t
      
# algoritmo con H(n) perche dopo 100 incrementa t di 3 n volte 
def es1_2(n)->int:
      t = 0 
      n = abs(n)  # H(1)
      if n<100:   # H(n)
        return 1
      else:
        for i in range(n):
            t+=3
        return t


# caso ottimo quando il numero e dispari H(1)
# caso pessimo quando il numero e pari H(n)
def es2(n)->int:
        if n<0: n-=n
        while n>0:
            if n%2==1:return 1
            n-=2
        return 0


# complessita H(sqrt(n))
def es3(n):
    n=abs(n)
    x = r =0
    while x*x < n:
        x+=1
        r+=3*x
    return r

# complessita H(log(n))
def es3(n)->int:
    n = abs(n)
    x = r = 0
    while n>1:
        r+=2
        n = n//3
    return r


# complessita H(log(log(n)))
# all prima iterazione fa 2 alla seconda iterazione diventa 2^2
# alla terza itaerazione diventa 2^2*2^2 e cosi  via 
# p = 2^2^i circa uguale n

def es4(n):
    n = abs(n)
    p=2
    while n>p:
        p = p*p
    return p

# complessita di H(1) per le prime due iustruzioni
# complessita di H(n) per il for 
# complessita di H(3^n) per il while 
# alla fine la complessita e H(1) + H(n) + H(3^n) = H(3^n)

def es5(n)->int:
    n = abs(n)
    t = x = 1
    for i in range(n): t=3*t  # H(n)
    while t > x:              # H(3^n)
        x+=2
        t-=2
    return t







