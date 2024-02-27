
def count_zero(l:list[int]) -> int:
    result = 0
    for i in l:
        if i == 0:
            result+=1
    return result

# O(n^3)
def es2(S: list[int], k:int ) -> int:
    n = len(S)
    max_z_cnt = 0
    z_cnt = 0
    numbers = []
    for y in range(n):
        for x in range(n):
            if x+y >= n:
                break
            z_cnt += count_zero(S[:x])
            z_cnt += count_zero(S[-y:]) 
            numbers.extend(S[:x])
            numbers.extend(S[-y:])
            if sum(numbers) <= k:
                if max_z_cnt < z_cnt:
                    max_z_cnt = z_cnt
            z_cnt = 0
            numbers = []
    return max_z_cnt

if __name__ == '__main__':
    lista = [1,0,2,8,0,5,1,6,0,0,3]
    k = 8
    print(es2(lista,k))