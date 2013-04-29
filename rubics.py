#!/usr/bin/python
import random


#
# This file contains the definition of the model for a 3X3X3 cube
# along with all of the functions needed to create it, manipulate it and visualize it.
# Import this file to impliment a solving algorithm.
#
#


# 	The cube is modeled as a array of 6 2d arrays,
#          each of which represents a face of the cube
#
#       I'll visualize it like this
#
#               |  |  |  |
#      	        |  back  |
#               |  |  |  |
#
# |  |  |  |    |  |  |  |    |  |  |  |    |  |  |  |
# |  Left  |    |  Top   |    |  right |    | bottom |
# |  |  |  |    |  |  |  |    |  |  |  |    |  |  |  |
#
# 	        |  |  |  |
#	        |  front |
#	        |  |  |  |
#
#       This is meant to look like the cube if you had litterally folded it out
#       like a paper cube. Thus the bottom face is reflected accross the vertical axis.
#       All of the turns directions will be indicated in reference to this picture.
#       When thinking of the following rotations you must abandon how you think about
#       the cube in 3d form. Remember all turns are made in reference to this picture!
#


# The tiles of the cube shall be indexed like this:
# Cube[side][vertical axis][horizontal axis] = color

# The axises refer to the orientation of the drawing above.
# 0 means upward/leftward
# 1 means middle of the face
# 2 mean downward/rightward


# These are for convienience in referencing the faces
Left = 0
Top = 1
Front = 2      # Don't change these!
Back = 3
Right = 4
Bottom = 5



#
# Cube Initialization
#

solvedCube =(((1,1,1),
             (1,1,1),
             (1,1,1)),
        ((2,2,2),
         (2,2,2),
         (2,2,2)),
        ((3,3,3),
         (3,3,3),
         (3,3,3)),
        ((4,4,4),
         (4,4,4),
         (4,4,4)),
        ((5,5,5),
         (5,5,5),
         (5,5,5)),
        ((6,6,6),
         (6,6,6),
         (6,6,6)))
              


        
#
# Cube Operations
#

# -There are 18 operations, two for each face/middle layer
#  in either direction (clock-wise, counter-clock-wise)
#
# -All of the operations are done in place. The functions will not return anything
#
# -I do not implement double turns explicitly
#
# -Each operation will be represented with either a letter denoting the face that is turned
#  or a pair of letters indicating the two faces between which is the middle layer turned.
#
# -Lowercase means turning clock-wise/right/up
#  Uppercase means turning counter-clock-wise/left/down (relative to the picture above!!!)


#Left = 0
#Top = 1
#Front = 2      
#Back = 3
#Right = 4
#Bottom = 5



def f(C):
        # Front Face Rotation - clock-wise
        fro = tuple(zip(*((C[Front])[::-1])))

        # Edges of Other Faces
        top = (C[Top][0], C[Top][1], C[Left][2])
        lef = (C[Left][0], C[Left][1], C[Bottom][2])
        bot = (C[Bottom][0], C[Bottom][1], C[Right][2])
        rit = (C[Right][0], C[Right][1], C[Top][2])

        return (lef, top, fro, C[Back], rit, bot)

def F(C):
        return f(f(f(C)))


def ba(C):
        # Back Face Rotation - clock-wise
        bac =  tuple(zip(*((C[Back])[::-1])))

        # Edges of Other Faces        
        top = (C[Right][0],  C[Top][1], C[Top][2])
        rit = (C[Bottom][0],  C[Right][1], C[Right][2])
        bot = (C[Left][0],  C[Bottom][1], C[Bottom][2])
        lef = (C[Top][0], C[Left][1], C[Left][2])

        return (lef, top, C[Front], bac, rit, bot)

def BA(C):
        return ba(ba(ba(C)))


def l(C):
        # Left Face Rotation - clock-wise

        lef =  tuple(zip(*((C[Left])[::-1])))


        fro = ((C[Top][0][0], C[Front][0][1], C[Front][0][2]),
               (C[Top][1][0], C[Front][1][1], C[Front][1][2]),
               (C[Top][2][0], C[Front][2][1], C[Front][2][2]))
        top = ((C[Back][0][0], C[Top][0][1], C[Top][0][2]),
               (C[Back][1][0], C[Top][1][1], C[Top][1][2]),
               (C[Back][2][0], C[Top][2][1], C[Top][2][2]))
        bac = ((C[Bottom][2][2], C[Back][0][1], C[Back][0][2]),
               (C[Bottom][1][2], C[Back][1][1], C[Back][1][2]),
               (C[Bottom][0][2], C[Back][2][1], C[Back][2][2]))
        bot = ((C[Bottom][0][0], C[Bottom][0][1], C[Front][2][0]),
               (C[Bottom][1][0], C[Bottom][1][1], C[Front][1][0]),
               (C[Bottom][2][0], C[Bottom][2][1], C[Front][0][0]))
        

        return (lef, top, fro, bac, C[Right], bot)

def L(C):
        return l(l(l(C)))


def r(C):
        rit =  tuple(zip(*((C[Right])[::-1])))


        fro = ((C[Front][0][0], C[Front][0][1], C[Bottom][2][0]),
               (C[Front][1][0], C[Front][1][1], C[Bottom][1][0]),
               (C[Front][2][0], C[Front][2][1], C[Bottom][0][0]))
        top = ((C[Top][0][0], C[Top][0][1], C[Front][0][2]),
               (C[Top][1][0], C[Top][1][1], C[Front][1][2]),
               (C[Top][2][0], C[Top][2][1], C[Front][2][2]))
        bac = ((C[Back][0][0], C[Back][0][1], C[Top][0][2]),
               (C[Back][1][0], C[Back][1][1], C[Top][1][2]),
               (C[Back][2][0], C[Back][2][1], C[Top][2][2]))
        bot = ((C[Back][2][2], C[Bottom][0][1], C[Bottom][0][2]),
               (C[Back][1][2], C[Bottom][1][1], C[Bottom][1][2]),
               (C[Back][0][2], C[Bottom][2][1], C[Bottom][2][2]))
        

        return (C[Left], top, fro, bac, rit, bot)


def R(C):
        return r(r(r(C)))

def t(C):
         # Top Face Rotation - clock-wise
        top =  tuple(zip(*((C[Top])[::-1])) )

        
        bac = (C[Back][0], C[Back][1],
               (C[Left][2][2], C[Left][1][2], C[Left][0][2]))
        lef = ((C[Left][0][0], C[Left][0][1], C[Front][0][0]),
               (C[Left][1][0], C[Left][1][1], C[Front][0][1]),
               (C[Left][2][0], C[Left][2][1], C[Front][0][2]))
        fro = ((C[Right][2][0], C[Right][1][0], C[Right][0][0]),
               C[Front][1], C[Front][2])
        rit = ((C[Back][2][0], C[Right][0][1], C[Right][0][2]),
               (C[Back][2][1], C[Right][1][1], C[Right][1][2]),
               (C[Back][2][2], C[Right][2][1], C[Right][2][2]))

        return (lef, top, fro, bac, rit, C[Bottom])

def T(C):
        return t(t(t(C)))

def bo(C):
         # Bottom Face Rotation - clock-wise
        bot =  tuple(zip(*((C[Bottom])[::-1])))  # This must be flipped!
 
        bac = ((C[Left][2][0], C[Left][1][0], C[Left][0][0]),
                C[Back][1], C[Back][2])
        lef = ((C[Front][2][0], C[Left][0][1], C[Left][0][2]),
               (C[Front][2][1], C[Left][1][1], C[Left][1][2]),
               (C[Front][2][2], C[Left][2][1], C[Left][2][2]))
        fro = (C[Front][0], C[Front][1],
               (C[Right][2][2], C[Right][1][2],  C[Right][0][2]))
        rit = ((C[Right][0][0], C[Right][0][1], C[Back][0][0]),
               (C[Right][1][0], C[Right][1][1], C[Back][0][1]),
               (C[Right][2][0], C[Right][2][1], C[Back][0][2]))

        return (lef, C[Top], fro, bac, rit, bot)

def BO(C):
        return bo(bo(bo(C)))


       
#Centers
# tb - Layer between top and bottom
def tb(C):

        # Rotate the layer between the top and bottom layer clock-kwise
        oldback = list(C[Back][1])
        
        bac = (C[Back][0],
               (C[Left][2][1], C[Left][1][1], C[Left][0][1]),
               C[Back][2])
        lef = ((C[Left][0][0], C[Front][1][0], C[Left][0][2]),
               (C[Left][1][0], C[Front][1][1], C[Left][1][2]),
               (C[Left][2][0], C[Front][1][2], C[Left][2][2]))
        fro = (C[Front][0],
               (C[Right][2][1], C[Right][1][1], C[Right][0][1]),
               C[Front][2])
        rit = ((C[Right][0][0], C[Back][1][0], C[Right][0][2]),
               (C[Right][1][0], C[Back][1][1], C[Right][1][2]),
               (C[Right][2][0], C[Back][1][2], C[Right][2][2]))

        return (lef, C[Top], fro, bac, rit, C[Bottom])


def TB(C):
        return tb(tb(tb(C)))



def fb(C):

    top = (C[Top][0], C[Left][1], C[Top][2])
    lef = (C[Left][0], C[Bottom][1], C[Left][2])
    bot = (C[Bottom][0], C[Right][1], C[Bottom][2])
    rit = (C[Right][0], C[Top][1], C[Right][2])

    return (lef, top, C[Front], C[Back], rit, bot)


def FB(C):
        return fb(fb(fb(C)))



def lr(C):
        
    fro = ((C[Front][0][0], C[Top][0][1], C[Front][0][2]),
           (C[Front][1][0], C[Top][1][1], C[Front][1][2]),
           (C[Front][2][0], C[Top][2][1], C[Front][2][2]))
    top = ((C[Top][0][0], C[Back][0][1], C[Top][0][2]),
           (C[Top][1][0], C[Back][1][1], C[Top][1][2]),
           (C[Top][2][0], C[Back][2][1], C[Top][2][2]))
    bac = ((C[Back][0][0], C[Bottom][2][1], C[Back][0][2]),
           (C[Back][1][0], C[Bottom][1][1], C[Back][1][2]),
           (C[Back][2][0], C[Bottom][0][1], C[Back][2][2]))
    bot = ((C[Bottom][0][0], C[Front][2][1], C[Bottom][0][2]),
           (C[Bottom][1][0], C[Front][1][1], C[Bottom][1][2]),
           (C[Bottom][2][0], C[Front][0][1], C[Bottom][2][2]))

    return (C[Left], top, fro, bac, C[Right], bot)

def LR(C):
           return lr(lr(lr(C)))


listOfAllOps = [f,F,ba,BA,t,T,bo,BO,l,L,r,R,lr,LR,tb,TB,fb,FB]

#
# Cube Visualization
#



def printCube(C):
        print('            |' + str(C[Back][0][0]) + '|' + str(C[Back][0][1]) + '|' + str(C[Back][0][2]) + '|')
        print('            |' + str(C[Back][1][0]) + '|' + str(C[Back][1][1]) + '|' + str(C[Back][1][2]) + '|')
        print('            |' + str(C[Back][2][0]) + '|' + str(C[Back][2][1]) + '|' + str(C[Back][2][2]) + '|\n')
        
        print(' |' + str(C[Left][0][0])   + '|' + str(C[Left][0][1])  + '|' + str(C[Left][0][2])   + '|   ' +
              ' |' + str(C[Top][0][0])    + '|' + str(C[Top][0][1])   + '|'  + str(C[Top][0][2])   + '|   ' +
              ' |' + str(C[Right][0][0])  + '|' + str(C[Right][0][1])  + '|' + str(C[Right][0][2])  + '|   ' +
              ' |' + str(C[Bottom][0][0]) + '|' + str(C[Bottom][0][1]) + '|' + str(C[Bottom][0][2]) + '|   ' )
        
        print(' |' + str(C[Left][1][0])   + '|' + str(C[Left][1][1])   + '|' + str(C[Left][1][2])   + '|   ' +
              ' |' + str(C[Top][1][0])    + '|' + str(C[Top][1][1])    + '|' + str(C[Top][1][2])    + '|   ' +
              ' |' + str(C[Right][1][0])  + '|' + str(C[Right][1][1])  + '|' + str(C[Right][1][2])  + '|   ' +
              ' |' + str(C[Bottom][1][0]) + '|' + str(C[Bottom][1][1]) + '|' + str(C[Bottom][1][2]) + '|   ' )

        print(' |' + str(C[Left][2][0])   + '|' + str(C[Left][2][1])   + '|' + str(C[Left][2][2])   + '|   ' +
              ' |' + str(C[Top][2][0])    + '|' + str(C[Top][2][1])    + '|' + str(C[Top][2][2])    + '|   ' +
              ' |' + str(C[Right][2][0])  + '|' + str(C[Right][2][1])  + '|' + str(C[Right][2][2])  + '|   ' +
              ' |' + str(C[Bottom][2][0]) + '|' + str(C[Bottom][2][1]) + '|' + str(C[Bottom][2][2]) + '| \n' )

        print('            |' + str(C[Front][0][0]) + '|' + str(C[Front][0][1]) + '|' + str(C[Front][0][2]) + '|')
        print('            |' + str(C[Front][1][0]) + '|' + str(C[Front][1][1]) + '|' + str(C[Front][1][2]) + '|')
        print('            |' + str(C[Front][2][0]) + '|' + str(C[Front][2][1]) + '|' + str(C[Front][2][2]) + '|\n\n')



#
# Scrambling and Operation Sequences
#


def genRandSeq(length):
        return [random.randrange(0,18) for x in range(length)]

def applySeq(seq, cube):
        if( not seq ):
                return cube
        else:
                *head, tail = seq
                return listOfAllOps[tail](applySeq(head, cube))


def getUndoSeq(seq):
    def inverse(x):
        if (x % 2 == 0):
            return x + 1
        else:
            return x - 1
    return [inverse(x) for x in seq[::-1]]

    
def newScrambledCube(s):
        return applySeq(genRandSeq(s), solvedCube)


def checkSolved(C):
        if( len(set(C[Front][0]) | set(C[Front][1]) | set(C[Front][2])) == 1 and
            len(set(C[Back][0])  | set(C[Back][1])  | set(C[Back][2])) == 1 and
            len(set(C[Top][0])   | set(C[Top][1])   | set(C[Top][2])) == 1 and
            len(set(C[Bottom][0])| set(C[Bottom][1])| set(C[Bottom][2])) == 1 and
            len(set(C[Left][0])  | set(C[Left][1])  | set(C[Left][2])) == 1 and
            len(set(C[Right][0]) | set(C[Right][1]) | set(C[Right][2])) == 1
            ):
                return True
        else: return



#
# Testing
#
#Cube = newSolvedCube()

##import time
##
##totalTime = 0
##sucess = True
##for i in range(1000):
##    seq = genRandSeq(100)
##    #print(seq)
##    cube = applySeq(seq, solvedCube)
##    #printCube(cube)
##    
##    undocube = applySeq(getUndoSeq(seq), cube)
##    #printCube(undocube)
##    t1 = time.time()
##    solved = checkSolved(undocube) 
##    t2 = time.time()
##    totalTime += (t2-t1)
##    if( solved != True ):
##        print('failed attempt!!!')
##        printCube(undocube)
##        sucess = False
##        break
##
##if( sucess):
##    print('Avg checkSolved time ' + str(totalTime/10000))
