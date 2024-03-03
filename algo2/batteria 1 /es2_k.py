from enum import Enum, auto

logUsefullSubSeqInfoList=False

class BigO(Enum):
    N = auto()
    N_LOGN = auto()
    N2 = auto()
    N3 = auto()
    
class SubSeqInfo:
    def __init__(self, zeroCount: int, elemCount: int, elemSum: int):
        self.zeroCount=zeroCount
        self.elemCount=elemCount
        self.elemSum=elemSum

    def __str__(self) -> str:
        return "(zeroCount="+str(self.zeroCount)+", elemCount="+str(self.elemCount)+", elemSum="+str(self.elemSum)+")"
    
    def __repr__(self) -> str:
        return str(self)



def getUsefullSubSeqInfoList(seq:list[int], k:int)-> list[SubSeqInfo]:
    # usefull sub sequences are ordered in zeroCount increasing order starting from 0 with +1 steps

    # starts with only the empty set that is always valid
    outList = [SubSeqInfo(0, 0, 0)] 
    idx = -1
    sum = 0
    zeroCount=0

    # add element only if new sequence is valid, supposing empty the set in the opposite direction.
    maxUsableCount = len(seq)-1 # x+y<n with x=idx+1 and y=0 and n=len(seq)
                                # -> (idx+1)+1<len(seq) where one +1 is for evaluating the next element and the other +1 is for passage from index to count
                                # idx+1<len(seq)-1 
    while idx+1 < maxUsableCount and sum + seq[idx+1]<= k: # next is valid
        idx+=1
        newVal = seq[idx]
        sum+=newVal
        if newVal == 0:
            zeroCount+=1
            outList.append(SubSeqInfo(zeroCount, idx+1, sum)) # a usefull sequence must terminate with a zero (idx+1 is the used element count)

    if logUsefullSubSeqInfoList:
        print(outList)

    return outList

def isValidSol(l:SubSeqInfo, r:SubSeqInfo, k:int, n:int)-> bool:
    return l.elemCount+r.elemCount<n and l.elemSum+r.elemSum<=k

def getSol_O_N_Helper(infoList1:list[SubSeqInfo], infoList2:list[SubSeqInfo], k:int, n:int)->int:
    idx1=0 # empty set
    idx2=0 # full set (list2 is reversed)
    curMaxZeroCount= infoList1[idx1].zeroCount + infoList2[idx2].zeroCount
    # one empty set and one full set is a valid solution pair (see getUsefullSubSeqInfoList(...))

    while True:
        # try first to add elements to first list
        if idx1+1 < len(infoList1) and isValidSol(infoList1[idx1+1], infoList2[idx2], k, n):
            idx1+=1 # at most n
        else:
            # when no more element can be added to first list, try to remove elements from second list
            if idx2+1 < len(infoList2):
                idx2+=1 # at most n
            else:
                break # unimprovable, nothing valid to add to first list and nothing to remove from second list
        curMaxZeroCount = max(curMaxZeroCount, infoList1[idx1].zeroCount+infoList2[idx2].zeroCount)
    return curMaxZeroCount

def getSol_O_N(infoListL:list[SubSeqInfo], infoListR:list[SubSeqInfo], k:int, n:int)->int:
    infoListRRev = list(infoListR)
    infoListRRev.reverse()

    infoListLRev = list(infoListL)
    infoListLRev.reverse()
     
    return min(getSol_O_N_Helper(infoListL, infoListRRev, k, n),
               getSol_O_N_Helper(infoListR, infoListLRev, k, n))


def getCentralIndex(minIncluded:int, maxExcluded:int)->int:
    incr=(maxExcluded-minIncluded)//2
    return minIncluded + incr

def getSol_O_NlogN(infoListL:list[SubSeqInfo], infoListR:list[SubSeqInfo], k:int, n:int)->int:
    curMaxZeroCount=0
    for l in infoListL:
        minInclIdx=0
        maxExclIdx=len(infoListR)
        lZeroCount= l.zeroCount
        while (maxExclIdx - minInclIdx) > 1:# TODO! implement binary search of max valid pair(l,r) using infoListR zeroCount natural order
            currIdx=getCentralIndex(minInclIdx, maxExclIdx)
            r=infoListR[currIdx]
            if isValidSol(l, r, k, n):
                curMaxZeroCount = max(curMaxZeroCount, lZeroCount+r.zeroCount)
                minInclIdx=currIdx
            else:
                maxExclIdx=currIdx
        curMaxZeroCount = max(curMaxZeroCount, lZeroCount+ infoListR[minInclIdx].zeroCount)# finally evaluate R zeroCount(minInclIdx) (can be avoided?)
    return curMaxZeroCount

def getSol_O_N2(infoListL:list[SubSeqInfo], infoListR:list[SubSeqInfo], k:int, n:int)->int:
    curMaxZeroCount=0
    for l in infoListL:
        for r in infoListR:
            if isValidSol(l, r, k, n):
                curMaxZeroCount = max(curMaxZeroCount, l.zeroCount+r.zeroCount)
    return curMaxZeroCount

def es2k(seq:list[int], k:int, bigO:BigO)->int:
    n=len(seq)

    # initialize infoListL and infoListR including only potentially usefull sub sequences
    # usefull sub sequences are ordered in zeroCount increasing order starting from 0 with +1 steps
    infoListL  = getUsefullSubSeqInfoList(seq,k)# left subsequence info sequence
    seqRev = list(seq)
    seqRev.reverse()
    infoListR = getUsefullSubSeqInfoList(seqRev,k)# right subsequence sequence (using reversed input sequence)

    # return the maximum zero count of valid (left,rigth) subsequence pairs
    match bigO:
        case BigO.N:
            return getSol_O_N(infoListL,infoListR,k,n)
        case BigO.N_LOGN:
            return getSol_O_NlogN(infoListL,infoListR,k,n)
        case BigO.N2:
            return getSol_O_N2(infoListL,infoListR,k,n)
        case _:
            raise ValueError("Unimplemented bigO order: " + bigO.name)

def log_es2k(seq:list[int], k:int)->int:
    print("SOLUZIONI CON INPUT: S = " + str(seq)+", k = " + str(k)+", n = " + str(len(seq)))
    print("  Soluzione k O(n)        : MaxZeroCount = ", es2k(seq, k, BigO.N))
    print("  Soluzione k O(n^2)      : MaxZeroCount = ", es2k(seq, k, BigO.N2))
    print("  Soluzione k O(n*log(n)) : MaxZeroCount = ", es2k(seq, k, BigO.N_LOGN))


if __name__ == '__main__':
    k = 8
    log_es2k([1,0,2,8,0,5,1,6,0,0,3], k)
    log_es2k([0,0,0,0,0,0,0,0,0,0,0], k)
    log_es2k([1,1,1,1,1,1,1,1,1,1,1], k)
    log_es2k([1,0,1,0,1,0,1,0,1,0,1], k)    
    log_es2k([2,0,2,0,2,0,2,0,2,0,2], k)
    log_es2k([0,2,0,2,0,2,0,2,0,2,0], k)
    log_es2k([0,2,0,2,0,0,0,2,0,2,0], k)
    log_es2k([4,0,4,0,4,0,4,0,4,0,4], k)
    log_es2k([0,4,0,4,0,4,0,4,0,4,0], k)
    log_es2k([0,4,0,0,0,0,0,0,0,4,0], k)
    log_es2k([0,8,0,0,0,0,0,0,0,8,0], k)
    log_es2k([0,9,0,0,0,0,0,0,0,9,0], k)
    log_es2k([0,0,0,0,0,9,0,0,0,0,0], k)