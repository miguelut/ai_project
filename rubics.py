


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
        C = [ [['b12','b','b'],
               ['b11','b','b'],
               ['b10','b','b']],
              [['w','w','w'],
               ['w','w','w'],
               ['w','w','w']],
              [['r','r','r'],
               ['r','r','r'],
               ['r9','r8','r7']],
              [['o1','o2','o3'],
               ['o','o','o'],
               ['o','o','o']],
              [['g','g','g4'],
               ['g','g','g5'],
               ['g','g','g6']],
              [['y1','y2','y3'],
               ['y8','y','y4'],
               ['y7','y6','y5']]]

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

def b(C):
        # Back Face Rotation - clock-wise
        C[Back] = list(zip(*((C[Back])[::-1])))

        # Edges of Other Faces
        oldtop = list(C[Top][0])
        
        C[Top][0] = C[Right][0]
        C[Right][0] = C[Bottom][0]
        C[Bottom][0] = C[Left][0]
        C[Left][0] = oldtop
        

def B(C):
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

def b(C):
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

def B(C):
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
# lr - Layer betweem left and right (Cap upward, lower downward)
# fb - Layer between front and back (Cap leftward, lower rightward)





#
# Cube Visualization
#



def printCube(C):
        print('            |' + C[Back][0][0] + '|' + C[Back][0][1] + '|' + C[Back][0][2] + '|')
        print('            |' + C[Back][1][0] + '|' + C[Back][1][1] + '|' + C[Back][1][2] + '|')
        print('            |' + C[Back][2][0] + '|' + C[Back][2][1] + '|' + C[Back][2][2] + '|\n')
        
        print(' |' + C[Left][0][0]   + '|' + C[Left][0][1]   + '|' + C[Left][0][2]   + '|   ' +
              ' |' + C[Top][0][0]    + '|'  + C[Top][0][1]   + '|'  + C[Top][0][2]   + '|   ' +
              ' |' + C[Right][0][0]  + '|' + C[Right][0][1]  + '|' + C[Right][0][2]  + '|   ' +
              ' |' + C[Bottom][0][0] + '|' + C[Bottom][0][1] + '|' + C[Bottom][0][2] + '|   ' )
        
        print(' |' + C[Left][1][0]   + '|' + C[Left][1][1]   + '|' + C[Left][1][2]   + '|   ' +
              ' |' + C[Top][1][0]    + '|' + C[Top][1][1]    + '|' + C[Top][1][2]    + '|   ' +
              ' |' + C[Right][1][0]  + '|' + C[Right][1][1]  + '|' + C[Right][1][2]  + '|   ' +
              ' |' + C[Bottom][1][0] + '|' + C[Bottom][1][1] + '|' + C[Bottom][1][2] + '|   ' )

        print(' |' + C[Left][2][0]   + '|' + C[Left][2][1]   + '|' + C[Left][2][2]   + '|   ' +
              ' |' + C[Top][2][0]    + '|' + C[Top][2][1]    + '|' + C[Top][2][2]    + '|   ' +
              ' |' + C[Right][2][0]  + '|' + C[Right][2][1]  + '|' + C[Right][2][2]  + '|   ' +
              ' |' + C[Bottom][2][0] + '|' + C[Bottom][2][1] + '|' + C[Bottom][2][2] + '| \n' )

        print('            |' + C[Front][0][0] + '|' + C[Front][0][1] + '|' + C[Front][0][2] + '|')
        print('            |' + C[Front][1][0] + '|' + C[Front][1][1] + '|' + C[Front][1][2] + '|')
        print('            |' + C[Front][2][0] + '|' + C[Front][2][1] + '|' + C[Front][2][2] + '|\n\n')



#
# Testing
#
Cube = newSolvedCube()


printCube(Cube)
print('After Rotation')
B(Cube)


printCube(Cube)
