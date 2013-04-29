from rubics import *
from collections import deque
import time

#
# Iterative Deepening
#

def solveID(cube, depthlimit):
    for d in range(1,depthlimit+1):
        seq = dfSearch(cube, [], d, set())
        if(seq != False):
            return seq
    return False



def dfSearch(cube, seq, depth, visitedCubes):
    if( depth == 0 and checkSolved(cube) ):
        return seq
    elif(  depth > 0):
        visitedCubes.add(cube)
        for x in range(18):
            newcube = applySeq([x], cube)
            if( newcube not in visitedCubes ):
                ret = dfSearch(newcube, seq + [x], depth - 1, set())
                if(ret != False):
                    return ret
        return False
    else:
        return False



#
# Testing
#

t1 = time.time()

for i in range(5):
    seq = genRandSeq(6)
    cube = applySeq(seq, solvedCube)
    print(seq)

    ret = solveID(cube, 6)
    if( ret == False ):
        print('failed!')
        break
    else:
#        print('change seq ' + str(seq))
        print('soln seq ' + str(ret) )
        print('before')
        printCube(cube)
        print('after')
        testcube = applySeq(ret, cube)        
        printCube(testcube)


t2 = time.time()
print(' took %0.3f s' % (t2-t1))
    
