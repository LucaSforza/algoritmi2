
def generate_trees(n):
    # Caso base: un albero vuoto
    if n == 0:
        return [None]

    # Memorizzazione per la programmazione dinamica
    dp = [[] for _ in range(n + 1)]
    dp[0] = [None]

    # Costruisci gli alberi per ogni dimensione da 1 a n
    for nodes in range(1, n + 1):
        for root in range(nodes):
            for left in dp[root]:
                for right in dp[nodes - root - 1]:
                    node = Node(left, right)
                    dp[nodes].append(node)

    return dp[n]


def es2(n):
    if n == 0:
        return [None]
    
    dp = [0 for _ in range(n + 1)]
    dp[0],dp[1] = 1,1

    for nodes in range(2, n + 1):
        for left in range(nodes):
                dp[nodes] += dp[left]*dp[nodes-left-1]
    print(dp)

    return dp[n]

if __name__=="__main__":

    print(es2(5))