import numpy as np

#Initializing a matrix representing a solved 3x3x3 cube
#There are 6 faces (one of each color) and each face is composed of 3 columns
cube = [np.array([['o', 'o', 'o'] for column in range(3)]), 
    np.array([['w', 'w', 'w'] for column in range(3)]),
    np.array([['g', 'g', 'g'] for column in range(3)]),
    np.array([['y', 'y', 'y'] for column in range(3)]),
    np.array([['r', 'r', 'r'] for column in range(3)]),
    np.array([['b', 'b', 'b'] for column in range(3)])]

def rotate(direction, face):
    if face == 0:
        affected_side_faces_idx = [1, 2, 3, 5]

    elif face == 1:
        affected_side_faces_idx = [0, 5, 4, 2]

    elif face == 2:
        affected_side_faces_idx = [0, 1, 4, 3]

    elif face == 3:
        affected_side_faces_idx = [0, 2, 4, 5]

    elif face == 4:
        affected_side_faces_idx = [1, 5, 2, 3]

    elif face == 5:
        affected_side_faces_idx = [1, 0, 3, 4]
 
    if direction == 'right':
        right_turn(affected_side_faces_idx)

    if direction == 'left':
        #rotate forward face
        left_turn(affected_side_faces_idx)

def right_turn(affected_side_faces_idx):
    np.rot90(cube)

    new_affected_side_faces_top = []

    for side in range(len(affected_side_faces_idx)):
        new_affected_side_faces_top.append(list(cube[affected_side_faces_idx[(side - 1) % 4]][0]))

    for side in range(len(new_affected_side_faces_top)):
        cube[affected_side_faces_idx[side]][0] = new_affected_side_faces_top[side]

def left_turn(affected_side_faces_idx):
    for i in range(3):
        right_turn(affected_side_faces_idx)

    
def translator(move):
    if move[0].lower() == 'f':
        face = 1
    
    if move[0].lower() == 'l':
        face = 2

    if move[0].lower() == 'r':
        face = 5

    if move[0].lower() == 'b':
        face = 3

    if move.lower() == 'u':
        face = 0

    if move.lower() == 'd':
        face = 4

    try:
        if move[1] == "'":
            direction = 'left'

            try:
                if move[2] == '2':
                    for i in range(2):
                        rotate(direction, face)

            except:
                rotate(direction, face)

        else:
            try:
                for i in range(move[1]):
                    rotate('right', face)

            except:
                rotate('right', face)

    except:
        rotate('right', face)

translator("L'2")
print(cube)