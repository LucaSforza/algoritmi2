def countZero(ins:list[int],sogl:int,xIndex:int=0,yIndex:int=0,max_z_count=0)->bool:
    for i in range(len(ins)):
        #SX
        if sum(list[:xIndex])+sum(list[-yIndex:])<=len(ins) and xIndex+yIndex<sogl:
            if countZero(ins,sogl,xIndex+1,yIndex) and countZero(ins,sogl,xIndex,yIndex+1):
                
        else :
            return False

        #DX