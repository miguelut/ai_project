from rubics import *
from collections import deque
import time

#
# Iterative Deepening
#

visited = set()

def solveID(cube, depthlimit):
  for d in range(1,depthlimit+1):
    visited.clear()
    seq = dfSearch(cube, [], d)
    if(seq != False):
      return seq
  return False



def dfSearch(cube, seq, depth):
  if(cube in visited):
    return False
  elif(checkSolved(cube)):
    return seq
  elif(depth == 0):
    return False
  else:
    visited.add(cube)
    for x in range(18):
      newcube = applySeq([x], cube)
      ret = dfSearch(newcube, seq + [x], depth - 1)
      if(ret != False):
        return ret
    return False

#
# Testing
#

t1 = time.time()

for i in range(1):
    seq = genRandSeq(4)
    cube = applySeq(seq, solvedCube)
    print(seq)

    ret = solveID(cube, 4)
    if( ret == False ):
        print('failed!')
        exit()
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
    
