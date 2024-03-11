# complessita di programmmi ricorsivi 
    3 metodi per calcolarna la complessita 
    - 

##  fattoriale
```python
def fattoriale(n):
    f = 1 
    for i in range (n+1):  ## H(n) viene eseguito esattamente n volte mentre questo H(1)
        f=f*i
    return f


def fattorialeRicorcivo(n):    #H(n) anche questo viene eseguito n volte ma ha H(n) anche per 
    if n<=1 : return 1         #lo spazio 
    return fattorialeRicorcivo(n-1)*n

```

## ricerca sequenziale 
    la vestione sequenziale ha:
        tempo H(n)
        spazio H(1)

    la versione ricorsiva con lo slicing:
        tempo H(n^2)
        spazio sommatoria da i = 1 a n di i --> n(n+1)/2 quindi lo spazio è n^2

    la versione ricorsiva passando indice :
        tempo H(n)
        spazio H(1)

```python
def ricseqR(A,x):
    if A==[] : return False
    if A[0]==x :return True
        return ricseqR(A[1:],x)

def ricseqIndice(A,x,i=0):
    if i>=len(A) : return False
    if A[i]==x :return True
        return ricseqR(A,x,i+1)
```

# Ricerca binaria (vettore ordinato)
    versione ricorsiva:
        T(n) = (H(1) se n=0,T(n/2)+H(1) altrimenti) il tutto vien H(log(n))

```python

def ricercaBinariaR(A,x,i=0,j=-1):
    if j == -1 j = len(A)-1
    if i>j return False   #H(1)
    m = (i+j)//2   #H(1)
    if A[m]==x:return True
    if A[m]>x:return ricercaBinariaR(A,x,i,m-1)
    else:return ricercaBinariaR(A,x,m+1,j)

ricercaBinariaR(A,x,0,len(A)-1)

```

# Fibonacci

```python
def fibonacciIterativo(n):
    if n<=1 : return n
    a,b= 0,1
    for i in range(2,n+1):
        a,b= b,a+b
    return b


def fibonacciRicorsivo(n):
    if n<=1 : return n
    return fibonacciRicorsivo(n-1)+fibonacciRicorsivo(n-2)
a = time
fibonacciRicorsivo(100)
b = time()
print(b-a)


def fibonacciRicorsivo(n):
    if n=1 :
        fprima = 0
        fcorrent = 1
    else:
        fprima,fcorrent = fibonacciRicorsivo(n-1)

    return fcorrent,fprima+fcorrent

fibonacciRicorsivo(100)[1]

```