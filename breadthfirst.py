from collections import deque
from copy import deepcopy
from rubics import *
import time



def bfSearch(cube):
    seqQue = deque([[]])
    while( True ):     
        seq = seqQue.popleft()
        if( len(seq) > 6):
            return False
        else:
            applySeq(seq, cube)
            if(checkSolved(cube)):
                return seq
            else:
                applySeq(getUndoSeq(seq), cube)
                seqQue.extend([seq + [x] for x in range(18)])



t1 = time.time()

for x in range(1):
    cube = newSolvedCube()
    cube2 = deepcopy(cube)
    seq = genRandSeq(6)
    applySeq(seq, cube)
    applySeq(seq, cube2)
    print(seq)

    soln = bfSearch(cube)
    if(soln == False):
       print("failed")
       break
    print(soln)
    printCube(cube2)
    applySeq(soln, cube2)
    printCube(cube2)

t2 = time.time()
print(' took %0.3f s' % (t2-t1))
