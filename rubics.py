#!/usr/bin/python
import random


#
# This file contains the definition of the model for a 3X3X3 cube
# Along with all of the functions needed to create it, manipulate it and visualize it.
# Import this file to impliment a solving algorithm.
#
#


# 	The cube is visualized as a 3d array as follows:
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
#


# The cube shall be indexed like this:
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

def newSolvedCube():
        C = list([list([list([1,1,1]),
                   list([1,1,1]),
                   list([1,1,1])]),
                  list([list([2,2,2]),
                   list([2,2,2]),
                   list([2,2,2])]),
                  list([list([3,3,3]),
                   list([3,3,3]),
                   list([3,3,3])]),
                  list([list([4,4,4]),
                   list([4,4,4]),
                   list([4,4,4])]),
                  list([list([5,5,5]),
                   list([5,5,5]),
                   list([5,5,5])]),
                  list([list([6,6,6]),
                   list([6,6,6]),
                   list([6,6,6])])])

        return C
              
#def newScrambledCube():


        
#
# Cube Operations
#

# -There are 18 operations, two for each face/middle layer
#  in either direction (clock-wise, counter-clock-wise)
#
# -I do not implement double turns explicitly
#
# -Each operation will be represented with either a letter denoting the face that is turned
#  or the two faces between which is the middle layer turned
#
# -Lowercase means turning clock-wise/right/up
#  Uppercase means turning counter-clock-wise/left/down (relative to the picture above!!!)




def f(C):
        # Front Face Rotation - clock-wise
        C[Front] = list(zip(*((C[Front])[::-1])))

        # Edges of Other Faces
        oldtop = C[Top][2]

        C[Top][2] = C[Left][2]
        C[Left][2] = C[Bottom][2]
        C[Bottom][2] = C[Right][2]
        C[Right][2] = oldtop

def F(C):
        # Front Face Rotation - counter-clock-wise
        C[Front] = list(zip(*C[Front]))[::-1]

        # Edges of Other Faces
        oldtop = C[Top][2]

        C[Top][2] = C[Right][2]
        C[Right][2] = C[Bottom][2]
        C[Bottom][2] = C[Left][2]
        C[Left][2] = oldtop

def ba(C):
        # Back Face Rotation - clock-wise
        C[Back] = list(zip(*((C[Back])[::-1])))

        # Edges of Other Faces
        oldtop = list(C[Top][0])
        
        C[Top][0] = C[Right][0]
        C[Right][0] = C[Bottom][0]
        C[Bottom][0] = C[Left][0]
        C[Left][0] = oldtop
        

def BA(C):
        # Back Face Rotation - counter-clock-wise
        C[Back] = list(zip(*C[Back]))[::-1]

        # Edges of Other Faces
        oldtop = C[Top][0]
        
        C[Top][0] = C[Left][0]
        C[Left][0] = C[Bottom][0]
        C[Bottom][0] = C[Right][0]
        C[Right][0] = oldtop


def l(C):
        # Left Face Rotation - clock-wise
        C[Left] = list(zip(*((C[Left])[::-1])))

        oldfront = []
        oldfront.append(C[Front][0][0])
        oldfront.append(C[Front][1][0])
        oldfront.append(C[Front][2][0])

        C[Front][0][0] = C[Top][0][0]
        C[Front][1][0] = C[Top][1][0]
        C[Front][2][0] = C[Top][2][0]
        C[Top][0][0] = C[Back][0][0]
        C[Top][1][0] = C[Back][1][0]
        C[Top][2][0] = C[Back][2][0]
        C[Back][2][0] = C[Bottom][0][2] # Careful here, the bottom is reflected accross vertical!
        C[Back][1][0] = C[Bottom][1][2]
        C[Back][0][0] = C[Bottom][2][2]
        C[Bottom][0][2] = oldfront[2]
        C[Bottom][1][2] = oldfront[1]
        C[Bottom][2][2] = oldfront[0]

def L(C):
        # Left Face Rotation - counter-clock-wise
        C[Left] = list(zip(*C[Left]))[::-1]

        oldfront = []
        oldfront.append(C[Front][0][0])
        oldfront.append(C[Front][1][0])
        oldfront.append(C[Front][2][0])

        C[Front][0][0] = C[Bottom][2][2]
        C[Front][1][0] = C[Bottom][1][2]
        C[Front][2][0] = C[Bottom][0][2]
        C[Bottom][2][2] = C[Back][0][0] # Careful here, the bottom is reflected accross vertical!
        C[Bottom][1][2] = C[Back][1][0]
        C[Bottom][0][2] = C[Back][2][0]
        C[Back][0][0] = C[Top][0][0]
        C[Back][1][0] = C[Top][1][0]
        C[Back][2][0] = C[Top][2][0]
        C[Top][0][0] = oldfront[0]
        C[Top][1][0] = oldfront[1]
        C[Top][2][0] = oldfront[2]

def r(C):
        # Right Face Rotation - clock-wise
        C[Right] = list(zip(*((C[Right])[::-1])))

        oldfront = []
        oldfront.append(C[Front][0][2])
        oldfront.append(C[Front][1][2])
        oldfront.append(C[Front][2][2])

        C[Front][0][2] = C[Bottom][2][0]
        C[Front][1][2] = C[Bottom][1][0]
        C[Front][2][2] = C[Bottom][0][0]
        C[Bottom][2][0] = C[Back][0][2] # Careful here, the bottom is reflected accross vertical!
        C[Bottom][1][0] = C[Back][1][2]
        C[Bottom][0][0] = C[Back][2][2]
        C[Back][0][2] = C[Top][0][2]
        C[Back][1][2] = C[Top][1][2]
        C[Back][2][2] = C[Top][2][2]
        C[Top][0][2] = oldfront[0]
        C[Top][1][2] = oldfront[1]
        C[Top][2][2] = oldfront[2]

def R(C):
         # Right Face Rotation - counter-clock-wise
        C[Right] = list(zip(*C[Right]))[::-1]

        oldfront = []
        oldfront.append(C[Front][0][2])
        oldfront.append(C[Front][1][2])
        oldfront.append(C[Front][2][2])
        
        C[Front][0][2] = C[Top][0][2]
        C[Front][1][2] = C[Top][1][2]
        C[Front][2][2] = C[Top][2][2]
        C[Top][0][2] = C[Back][0][2]
        C[Top][1][2] = C[Back][1][2]
        C[Top][2][2] = C[Back][2][2]
        C[Back][0][2] = C[Bottom][0][0] # Careful here, the bottom is reflected accross vertical!
        C[Back][1][2] = C[Bottom][1][0]
        C[Back][2][2] = C[Bottom][2][0]
        C[Bottom][0][0] = oldfront[2]
        C[Bottom][1][0] = oldfront[1]
        C[Bottom][2][0] = oldfront[0]

def t(C):
         # Top Face Rotation - clock-wise
        C[Top] = list(zip(*((C[Top])[::-1])))

        oldback = list(C[Back][2])
        
        C[Back][2][0] = C[Left][2][2]
        C[Back][2][1] = C[Left][1][2]
        C[Back][2][2] = C[Left][0][2]
        C[Left][0][2] = C[Front][0][0]
        C[Left][1][2] = C[Front][0][1]
        C[Left][2][2] = C[Front][0][2]
        C[Front][0][0] = C[Right][2][0]
        C[Front][0][1] = C[Right][1][0]
        C[Front][0][2] = C[Right][0][0]
        C[Right][0][0] = oldback[0]
        C[Right][1][0] = oldback[1]
        C[Right][2][0] = oldback[2]

def T(C):
         # Top Face Rotation - counter-clock-wise
        C[Top] = list(zip(*C[Top]))[::-1]

        oldback = list(C[Back][2])
        
        C[Back][2][0] = C[Right][0][0]
        C[Back][2][1] = C[Right][1][0]
        C[Back][2][2] = C[Right][2][0]
        C[Right][0][0] = C[Front][0][2]
        C[Right][1][0] = C[Front][0][1]
        C[Right][2][0] = C[Front][0][0]
        C[Front][0][2] = C[Left][2][2]
        C[Front][0][1] = C[Left][1][2]
        C[Front][0][0] = C[Left][0][2]
        C[Left][0][2] = oldback[2]
        C[Left][1][2] = oldback[1]
        C[Left][2][2] = oldback[0]

def bo(C):
         # Bottom Face Rotation - clock-wise
        C[Bottom] = list(zip(*C[Bottom]))[::-1]  # This must be flipped!
 
        oldback = list(C[Back][0])
        
        C[Back][0][0] = C[Left][2][0]
        C[Back][0][1] = C[Left][1][0]
        C[Back][0][2] = C[Left][0][0]
        C[Left][0][0] = C[Front][2][0]
        C[Left][1][0] = C[Front][2][1]
        C[Left][2][0] = C[Front][2][2]
        C[Front][2][0] = C[Right][2][2]
        C[Front][2][1] = C[Right][1][2]
        C[Front][2][2] = C[Right][0][2]
        C[Right][0][2] = oldback[0]
        C[Right][1][2] = oldback[1]
        C[Right][2][2] = oldback[2]

def BO(C):
         # Top Face Rotation - counter-clock-wise
        C[Bottom] = list(zip(*((C[Bottom])[::-1]))) # Flipp it !! because botom is reflected

        oldback = list(C[Back][0])
        
        C[Back][0][0] = C[Right][0][2]
        C[Back][0][1] = C[Right][1][2]
        C[Back][0][2] = C[Right][2][2]
        C[Right][0][2] = C[Front][2][2]
        C[Right][1][2] = C[Front][2][1]
        C[Right][2][2] = C[Front][2][0]
        C[Front][2][2] = C[Left][2][0]
        C[Front][2][1] = C[Left][1][0]
        C[Front][2][0] = C[Left][0][0]
        C[Left][0][0] = oldback[2]
        C[Left][1][0] = oldback[1]
        C[Left][2][0] = oldback[0]

        
#Centers
# tb - Layer between top and bottom
def tb(C):

        # Rotate the layer between the top and bottom layer clock-kwise
        oldback = list(C[Back][1])
        
        C[Back][1][0] = C[Left][2][1]
        C[Back][1][1] = C[Left][1][1]
        C[Back][1][2] = C[Left][0][1]
        C[Left][0][1] = C[Front][1][0]
        C[Left][1][1] = C[Front][1][1]
        C[Left][2][1] = C[Front][1][2]
        C[Front][1][0] = C[Right][2][1]
        C[Front][1][1] = C[Right][1][1]
        C[Front][1][2] = C[Right][0][1]
        C[Right][0][1] = oldback[0]
        C[Right][1][1] = oldback[1]
        C[Right][2][1] = oldback[2]

def TB(C):

        # Rotate the layer between the top and bottom layer counter-clock-kwise
        oldback = list(C[Back][1])
        
        C[Back][1][0] = C[Right][0][1]
        C[Back][1][1] = C[Right][1][1]
        C[Back][1][2] = C[Right][2][1]
        C[Right][0][1] = C[Front][1][2]
        C[Right][1][1] = C[Front][1][1]
        C[Right][2][1] = C[Front][1][0]
        C[Front][1][0] = C[Left][0][1]
        C[Front][1][1] = C[Left][1][1]
        C[Front][1][2] = C[Left][2][1]
        C[Left][0][1] = oldback[2]
        C[Left][1][1] = oldback[1]
        C[Left][2][1] = oldback[0]

def fb(C):
    oldtop = list(C[Top][1])

    C[Top][1] = C[Left][1]
    C[Left][1] = C[Bottom][1]
    C[Bottom][1] = C[Right][1]
    C[Right][1] = oldtop

def FB(C):
    oldtop = list(C[Top][1])

    C[Top][1] = C[Right][1]
    C[Right][1] = C[Bottom][1]
    C[Bottom][1] = C[Left][1]
    C[Left][1] = oldtop
    
def lr(C):
    oldfront = list([C[Front][0][1], C[Front][1][1], C[Front][2][1]])

    C[Front][0][1] = C[Top][0][1]
    C[Front][1][1] = C[Top][1][1]
    C[Front][2][1] = C[Top][2][1]
    C[Top][0][1] = C[Back][0][1]
    C[Top][1][1] = C[Back][1][1]
    C[Top][2][1] = C[Back][2][1]
    C[Back][0][1] = C[Bottom][2][1]
    C[Back][1][1] = C[Bottom][1][1]
    C[Back][2][1] = C[Bottom][0][1]
    C[Bottom][0][1] = oldfront[2]
    C[Bottom][1][1] = oldfront[1]
    C[Bottom][2][1] = oldfront[0]

def LR(C):
    oldfront = list([C[Front][0][1], C[Front][1][1], C[Front][2][1]])

    C[Front][0][1] = C[Bottom][2][1]
    C[Front][1][1] = C[Bottom][1][1]
    C[Front][2][1] = C[Bottom][0][1]
    C[Bottom][0][1] = C[Back][2][1]
    C[Bottom][1][1] = C[Back][1][1]
    C[Bottom][2][1] = C[Back][0][1]
    C[Back][0][1] = C[Top][0][1]
    C[Back][1][1] = C[Top][1][1]
    C[Back][2][1] = C[Top][2][1]
    C[Top][0][1] = oldfront[0]
    C[Top][1][1] = oldfront[1]
    C[Top][2][1] = oldfront[2]


listOfAllOps = [f,F,ba,BA,t,T ,bo,BO,l,L ,r ,R ,lr ,LR,tb,TB,fb,FB]

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

def genScrambleSeq(length):
    scramSeq = []
    for x in range(length):
        scramSeq.append(random.randrange(0,18))
    return scramSeq


def applySeq(seq, cube):
    #for n in seq:
    listOfAllOps[0](cube)
    listOfAllOps[1](cube)
    listOfAllOps[2](cube)
    listOfAllOps[3](cube)
    #listOfAllOps[4](cube)
    #listOfAllOps[5](cube)
    #listOfAllOps[6](cube)
    #listOfAllOps[7](cube)
    #listOfAllOps[8](cube)
    listOfAllOps[9](cube)
    #listOfAllOps[10](cube)
    #listOfAllOps[11](cube)
    #listOfAllOps[12](cube)
    #listOfAllOps[13](cube)
    #listOfAllOps[14](cube)
    #listOfAllOps[15](cube)
    #listOfAllOps[16](cube)
    #listOfAllOps[17](cube)

#def getUndoSeq():


#def newScrambledCube():

def test(C):
    f(C)
    F(C)
    ba(C)
    lr(C)
    print("After lr(C)")
    #t(C)
    #r(C)
    #r(C)
    #ba(C)
    #BO(C)
    #T(C)

#
# Testing
#
Cube = newSolvedCube()

printCube(Cube)

seq = genScrambleSeq(20)
print(seq)
#applySeq(seq, Cube)
test(Cube)
print('After Rotation')
printCube(Cube)
