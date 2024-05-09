def simple_generator(n):
    alfabeto = ['a', 'b']
    trovate = []
    for i in range(n):
        trovate.append()
        yield i
        i += 1

def genera(n, simb,stringhe):
    if len(simb)<n:
        genera(n,simb+'a',stringhe)
        genera(n,simb+'b',stringhe)
    elif len(simb)==n:
        stringhe.append(simb)
    return

def es3(n):
    alfabeto = ['a', 'b']
    stringhe = []
    genera(n,'',stringhe)
    for string in stringhe:
        print(string+string[::-1])
            
es3(2)