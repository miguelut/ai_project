import rubics
from copy import deepcopy

#
# Iterative Deepening
#

def solveID(cube, depthlimit):
    for d in range(1,depthlimit+1):
        #C = deepcopy(cube)
        #seq = dfSearch(C, [], d)
        seq = dfSearch(cube, [], d)
        if(seq != False):
            return seq
    return False


def dfSearch(cube, seq, depth):
    if(rubics.checkSolved(cube) == True):
        return seq
    elif(depth > 0):
        ret = False
        for x in range(18):
            #newcube = deepcopy(C)
            #rubics.applySeq([x], newcube)
            #ret = dfSearch(newcube, seq + [x], depth - 1)
            rubics.applySeq([x], cube)
            ret = dfSearch(cube, seq + [x], depth - 1)
            if(ret != False):
                return ret
            rubics.applySeq(rubics.getUndoSeq([x]), cube)
        return False
    else:
        return False



#
# Testing
#

for i in range(1):
    cube = rubics.newSolvedCube()

    seq = rubics.genRandSeq(5)
    rubics.applySeq(seq, cube)
    #rubics.printCube(cube)
    
    #ret = dfSearch(cube, [], 5)
    ret = solveID(cube, 5)
    if( ret == False ):
        print('failed!')
    else:
        print('change seq ' + str(seq))
        print('soln seq ' + str(ret) )
        testcube = rubics.newSolvedCube()
        rubics.applySeq(seq, testcube)
        print('before')
        rubics.printCube(testcube)
        print('after')
        rubics.applySeq(ret, testcube)        
        rubics.printCube(testcube)


    
