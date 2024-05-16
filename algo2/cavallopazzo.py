def ricorsiva(n,scacchiera,sol,x=0,y=0,i=0):
    if i == n*n-1:
        print(sol)
        return True
    px = x+2
    py = y+1
    if px<n and py<n and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x+2
    py = y-1
    if px<n and py>=0 and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x-2
    py = y+1
    if px>=0 and py<n and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x-2
    py = y-1
    if px>=0 and py>=0 and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x+1
    py = y+2
    if px<n and py<n and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x+1
    py = y-2
    if px<n and py>=0 and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x-1
    py = y+2
    if px>=0 and py<n and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    px = x-1
    py = y-2
    if px>=0 and py>=0 and scacchiera[py][px]==0:
        scacchiera[py][px]=1
        sol.append((px,py))
        if ricorsiva(n,scacchiera,sol,px,py,i+1):
            return True
        sol.pop()
        scacchiera[py][px]=0
    return False

def cerca_percorso(n):
    scacchiera = [[0 for _ in range(n)] for _ in range(n)]
    scacchiera[0][0]=1
    sol = []
    return ricorsiva(n,scacchiera,sol)

def printTab(tab):
    sout = ''
    for rig in tab:
        sout+=str(rig)+'\n'
    print(sout)

if __name__ == '__main__':
    print(cerca_percorso(5))