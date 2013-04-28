import rubics
from copy import deepcopy

#
# Iterative Deepening
#

def solveID(cube, depthlimit):
    for d in range(1,depthlimit+1):
        C = deepcopy(cube)
        seq = dfSearch(C, [], d)
        if(seq != False):
            return seq
    return False

def dfSearch(C, seq, depth):
    if(rubics.checkSolved(C) == True):
        return seq
    elif(depth > 0):
        ret = False
        for x in range(18):
            newcube = deepcopy(C)
            rubics.applySeq([x], newcube)
            ret = dfSearch(newcube, seq + [x], depth - 1)
            if(ret != False):
                return ret
        return False
    else:
        return False


for i in range(10):
    cube = rubics.newSolvedCube()

    seq = rubics.genRandSeq(3)
    rubics.applySeq(seq, cube)
    #rubics.printCube(cube)
    
    #ret = dfSearch(cube, [], 5)
    ret = solveID(cube, 3)
    if( ret == False ):
        print('failed!')
        #break
    else:
        print('change seq ' + str(seq))
        print('soln seq ' + str(ret) )
        #print('before')
        #rubics.printCube(cube)
        #print('after')
        #rubics.applySeq(ret, cube)        
        #rubics.printCube(cube)


    
