import rubics
import time
from copy import deepcopy

#
# Iterative Deepening
#

def solveID(cube, depthlimit):
    for d in range(1,depthlimit+1):
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

t1 = time.time()

for i in range(1):
    cube = rubics.newSolvedCube()

    seq = rubics.genRandSeq(5)
    rubics.applySeq(seq, cube)

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


t2 = time.time()
print(' took %0.3f s' % (t2-t1))
    
