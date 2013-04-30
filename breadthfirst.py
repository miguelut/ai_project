from collections import deque
from rubics import *
import time

def bfSearch(cube):
    visitedCubes = set()
    seqQue = deque([[]])
    while( True ):     
        seq = seqQue.popleft()
        if( len(seq) > 7):
            return False
        else:
            newcube = applySeq(seq, cube)    
            if(checkSolved(newcube)):
                return seq
            else:
                if( newcube not in visitedCubes ):
                    visitedCubes.add(newcube)
                    print(visitedCubes)
                    seqQue.extend([seq + [x] for x in range(18)])



t1 = time.time()

for x in range(1):
    seq = genRandSeq(1)
    cube = applySeq(seq, solvedCube)
    print(seq)

    soln = bfSearch(cube)
    if(soln == False):
       print("failed")
       break
    print(soln)
    printCube(applySeq(soln, cube))

t2 = time.time()
print(' took %0.3f s' % (t2-t1))
