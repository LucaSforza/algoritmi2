from typing import Optional

def cassonetti(case: list[int], k: int) -> list[int]:
    pos_k = None
    result = []
    for c in case:
        if not rientra(c,pos_k,k):
            pos_k = c + k
            result.append(pos_k)
    return result

def rientra(c: int,pos_k: Optional[int],k :int) -> bool:
    if pos_k is None:
        return False
    return c >= pos_k - k and c <= pos_k + k

if __name__ == '__main__':
    C = [2, 5, 7, 11, 14, 16, 18]
    k = 3
    print(cassonetti(C,k))