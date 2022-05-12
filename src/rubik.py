from copy import deepcopy
from math import floor
from multiprocessing import Pool, Event

# All side layouts are viewed as if the cube is facing up (the white-colored side at the top, the yellow/orange side at the bottom), arranged from top to bottom row, with front side at the front
# Except for the bottom side. The bottom side is viewed as if the entire cube (that is in face-up condition) is rotated 180 degrees clockwise around the x axis, arranged from top to bottom row

topSide = [[1,1,1],[1,1,1],[1,1,1]]
frontSide = [[2,2,2],[2,2,2],[2,2,2]]
leftSide = [[3,3,3],[3,3,3],[3,3,3]]
backSide = [[4,4,4],[4,4,4],[4,4,4]]
rightSide = [[5,5,5],[5,5,5],[5,5,5]]
bottomSide = [[6,6,6],[6,6,6],[6,6,6]]
rubik = []
rubik.append(topSide)
rubik.append(frontSide)
rubik.append(leftSide)
rubik.append(backSide)
rubik.append(rightSide)
rubik.append(bottomSide)

def F(rubik):
    # Rotate front side
    temp = deepcopy(rubik[1][0])
    rubik[1][0][0], rubik[1][0][1], rubik[1][0][2] = rubik[1][2][0], rubik[1][1][0], rubik[1][0][0]
    rubik[1][2][0], rubik[1][1][0], rubik[1][0][0] = rubik[1][2][2], rubik[1][2][1], rubik[1][2][0]
    rubik[1][2][2], rubik[1][2][1], rubik[1][2][0] = rubik[1][0][2], rubik[1][1][2], rubik[1][2][2]
    rubik[1][0][2], rubik[1][1][2], rubik[1][2][2] = temp[0], temp[1], temp[2]
    # Rotate each row of a side that connects to the front side
    temp = deepcopy(rubik[0][2])
    rubik[0][2][0], rubik[0][2][1], rubik[0][2][2] = rubik[2][2][2], rubik[2][1][2], rubik[2][0][2]
    rubik[2][2][2], rubik[2][1][2], rubik[2][0][2] = rubik[5][0][2], rubik[5][0][1], rubik[5][0][0]
    rubik[5][0][2], rubik[5][0][1], rubik[5][0][0] = rubik[4][0][0], rubik[4][1][0], rubik[4][2][0]
    rubik[4][0][0], rubik[4][1][0], rubik[4][2][0] = temp[0], temp[1], temp[2]

def Fi(rubik):
    # Rotate front side
    temp = deepcopy(rubik[1][0])
    rubik[1][0][2], rubik[1][0][1], rubik[1][0][0] = rubik[1][2][2], rubik[1][1][2], rubik[1][0][2]
    rubik[1][2][2], rubik[1][1][2], rubik[1][0][2] = rubik[1][2][0], rubik[1][2][1], rubik[1][2][2]
    rubik[1][2][0], rubik[1][2][1], rubik[1][2][2] = rubik[1][0][0], rubik[1][1][0], rubik[1][2][0]
    rubik[1][0][0], rubik[1][1][0], rubik[1][2][0] = temp[2], temp[1], temp[0]
    # Rotate each row of a side that connects to the front side
    temp = deepcopy(rubik[0][2])
    rubik[0][2][2], rubik[0][2][1], rubik[0][2][0] = rubik[4][2][0], rubik[4][1][0], rubik[4][0][0]
    rubik[4][2][0], rubik[4][1][0], rubik[4][0][0] = rubik[5][0][0], rubik[5][0][1], rubik[5][0][2]
    rubik[5][0][0], rubik[5][0][1], rubik[5][0][2] = rubik[2][0][2], rubik[2][1][2], rubik[2][2][2]
    rubik[2][0][2], rubik[2][1][2], rubik[2][2][2] = temp[2], temp[1], temp[0]

def L(rubik):
    # Rotate left side
    temp = deepcopy(rubik[2][0])
    rubik[2][0][0], rubik[2][0][1], rubik[2][0][2] = rubik[2][2][0], rubik[2][1][0], rubik[2][0][0]
    rubik[2][2][0], rubik[2][1][0], rubik[2][0][0] = rubik[2][2][2], rubik[2][2][1], rubik[2][2][0]
    rubik[2][2][2], rubik[2][2][1], rubik[2][2][0] = rubik[2][0][2], rubik[2][1][2], rubik[2][2][2]
    rubik[2][0][2], rubik[2][1][2], rubik[2][2][2] = temp[0], temp[1], temp[2]
    # Rotate each row of a side that connects to the left side
    temp = [deepcopy(rubik[0][0][0]), deepcopy(rubik[0][1][0]), deepcopy(rubik[0][2][0])]
    rubik[0][0][0], rubik[0][1][0], rubik[0][2][0] = rubik[3][2][2], rubik[3][1][2], rubik[3][0][2]
    rubik[3][2][2], rubik[3][1][2], rubik[3][0][2] = rubik[5][0][0], rubik[5][1][0], rubik[5][2][0]
    rubik[5][0][0], rubik[5][1][0], rubik[5][2][0] = rubik[1][0][0], rubik[1][1][0], rubik[1][2][0]
    rubik[1][0][0], rubik[1][1][0], rubik[1][2][0] = temp[0], temp[1], temp[2]

def Li(rubik):
    # Rotate left side
    temp = deepcopy(rubik[2][0])
    rubik[2][0][2], rubik[2][0][1], rubik[2][0][0] = rubik[2][2][2], rubik[2][1][2], rubik[2][0][2]
    rubik[2][2][2], rubik[2][1][2], rubik[2][0][2] = rubik[2][2][0], rubik[2][2][1], rubik[2][2][2]
    rubik[2][2][0], rubik[2][2][1], rubik[2][2][2] = rubik[2][0][0], rubik[2][1][0], rubik[2][2][0]
    rubik[2][0][0], rubik[2][1][0], rubik[2][2][0] = temp[2], temp[1], temp[0]
    # Rotate each row of a side that connects to the left side
    temp = [deepcopy(rubik[0][0][0]), deepcopy(rubik[0][1][0]), deepcopy(rubik[0][2][0])]
    rubik[0][2][0], rubik[0][1][0], rubik[0][0][0] = rubik[1][2][0], rubik[1][1][0], rubik[1][0][0]
    rubik[1][2][0], rubik[1][1][0], rubik[1][0][0] = rubik[5][2][0], rubik[5][1][0], rubik[5][0][0]
    rubik[5][2][0], rubik[5][1][0], rubik[5][0][0] = rubik[3][0][2], rubik[3][1][2], rubik[3][2][2]
    rubik[3][0][2], rubik[3][1][2], rubik[3][2][2] = temp[2], temp[1], temp[0]

def B(rubik):
    # Rotate back side
    temp = deepcopy(rubik[3][0])
    rubik[3][0][0], rubik[3][0][1], rubik[3][0][2] = rubik[3][2][0], rubik[3][1][0], rubik[3][0][0]
    rubik[3][2][0], rubik[3][1][0], rubik[3][0][0] = rubik[3][2][2], rubik[3][2][1], rubik[3][2][0]
    rubik[3][2][2], rubik[3][2][1], rubik[3][2][0] = rubik[3][0][2], rubik[3][1][2], rubik[3][2][2]
    rubik[3][0][2], rubik[3][1][2], rubik[3][2][2] = temp[0], temp[1], temp[2]
    # Rotate each row of a side that connects to the back side
    temp = [deepcopy(rubik[0][0][2]), deepcopy(rubik[0][0][1]), deepcopy(rubik[0][0][0])]
    rubik[0][0][2], rubik[0][0][1], rubik[0][0][0] = rubik[4][2][2], rubik[4][1][2], rubik[4][0][2]
    rubik[4][2][2], rubik[4][1][2], rubik[4][0][2] = rubik[5][2][0], rubik[5][2][1], rubik[5][2][2]
    rubik[5][2][0], rubik[5][2][1], rubik[5][2][2] = rubik[2][0][0], rubik[2][1][0], rubik[2][2][0]
    rubik[2][0][0], rubik[2][1][0], rubik[2][2][0] = temp[0], temp[1], temp[2]

def Bi(rubik):
    # Rotate back side
    temp = deepcopy(rubik[3][0])
    rubik[3][0][2], rubik[3][0][1], rubik[3][0][0] = rubik[3][2][2], rubik[3][1][2], rubik[3][0][2]
    rubik[3][2][2], rubik[3][1][2], rubik[3][0][2] = rubik[3][2][0], rubik[3][2][1], rubik[3][2][2]
    rubik[3][2][0], rubik[3][2][1], rubik[3][2][2] = rubik[3][0][0], rubik[3][1][0], rubik[3][2][0]
    rubik[3][0][0], rubik[3][1][0], rubik[3][2][0] = temp[2], temp[1], temp[0]
    # Rotate each row of a side that connects to the back side
    temp = [deepcopy(rubik[0][0][2]), deepcopy(rubik[0][0][1]), deepcopy(rubik[0][0][0])]
    rubik[0][0][0], rubik[0][0][1], rubik[0][0][2] = rubik[2][2][0], rubik[2][1][0], rubik[2][0][0]
    rubik[2][2][0], rubik[2][1][0], rubik[2][0][0] = rubik[5][2][2], rubik[5][2][1], rubik[5][2][0]
    rubik[5][2][2], rubik[5][2][1], rubik[5][2][0] = rubik[4][0][2], rubik[4][1][2], rubik[4][2][2]
    rubik[4][0][2], rubik[4][1][2], rubik[4][2][2] = temp[2], temp[1], temp[0]

def R(rubik):
    # Rotate right side
    temp = deepcopy(rubik[4][0])
    rubik[4][0][0], rubik[4][0][1], rubik[4][0][2] = rubik[4][2][0], rubik[4][1][0], rubik[4][0][0]
    rubik[4][2][0], rubik[4][1][0], rubik[4][0][0] = rubik[4][2][2], rubik[4][2][1], rubik[4][2][0]
    rubik[4][2][2], rubik[4][2][1], rubik[4][2][0] = rubik[4][0][2], rubik[4][1][2], rubik[4][2][2]
    rubik[4][0][2], rubik[4][1][2], rubik[4][2][2] = temp[0], temp[1], temp[2]
    # Rotate each row of a side that connects to the right side
    temp = [deepcopy(rubik[0][2][2]), deepcopy(rubik[0][1][2]), deepcopy(rubik[0][0][2])]
    rubik[0][2][2], rubik[0][1][2], rubik[0][0][2] = rubik[1][2][2], rubik[1][1][2], rubik[1][0][2]
    rubik[1][2][2], rubik[1][1][2], rubik[1][0][2] = rubik[5][2][2], rubik[5][1][2], rubik[5][0][2]
    rubik[5][2][2], rubik[5][1][2], rubik[5][0][2] = rubik[3][0][0], rubik[3][1][0], rubik[3][2][0]
    rubik[3][0][0], rubik[3][1][0], rubik[3][2][0] = temp[0], temp[1], temp[2]

def Ri(rubik):
    # Rotate right side
    temp = deepcopy(rubik[4][0])
    rubik[4][0][2], rubik[4][0][1], rubik[4][0][0] = rubik[4][2][2], rubik[4][1][2], rubik[4][0][2]
    rubik[4][2][2], rubik[4][1][2], rubik[4][0][2] = rubik[4][2][0], rubik[4][2][1], rubik[4][2][2]
    rubik[4][2][0], rubik[4][2][1], rubik[4][2][2] = rubik[4][0][0], rubik[4][1][0], rubik[4][2][0]
    rubik[4][0][0], rubik[4][1][0], rubik[4][2][0] = temp[2], temp[1], temp[0]
    # Rotate each row of a side that connects to the right side
    temp = [deepcopy(rubik[0][2][2]), deepcopy(rubik[0][1][2]), deepcopy(rubik[0][0][2])]
    rubik[0][0][2], rubik[0][1][2], rubik[0][2][2] = rubik[3][2][0], rubik[3][1][0], rubik[3][0][0]
    rubik[3][2][0], rubik[3][1][0], rubik[3][0][0] = rubik[5][0][2], rubik[5][1][2], rubik[5][2][2]
    rubik[5][0][2], rubik[5][1][2], rubik[5][2][2] = rubik[1][0][2], rubik[1][1][2], rubik[1][2][2]
    rubik[1][0][2], rubik[1][1][2], rubik[1][2][2] = temp[2], temp[1], temp[0]

def U(rubik):
    # Rotate top side
    temp = deepcopy(rubik[0][0])
    rubik[0][0][0], rubik[0][0][1], rubik[0][0][2] = rubik[0][2][0], rubik[0][1][0], rubik[0][0][0]
    rubik[0][2][0], rubik[0][1][0], rubik[0][0][0] = rubik[0][2][2], rubik[0][2][1], rubik[0][2][0]
    rubik[0][2][2], rubik[0][2][1], rubik[0][2][0] = rubik[0][0][2], rubik[0][1][2], rubik[0][2][2]
    rubik[0][0][2], rubik[0][1][2], rubik[0][2][2] = temp[0], temp[1], temp[2]
    # Rotate each row of a side that connects to the top side
    temp = deepcopy(rubik[1][0])
    rubik[1][0][2], rubik[1][0][1], rubik[1][0][0] = rubik[4][0][2], rubik[4][0][1], rubik[4][0][0]
    rubik[4][0][2], rubik[4][0][1], rubik[4][0][0] = rubik[3][0][2], rubik[3][0][1], rubik[3][0][0]
    rubik[3][0][2], rubik[3][0][1], rubik[3][0][0] = rubik[2][0][2], rubik[2][0][1], rubik[2][0][0]
    rubik[2][0][2], rubik[2][0][1], rubik[2][0][0] = temp[2], temp[1], temp[0]

def Ui(rubik):
    # Rotate top side
    temp = deepcopy(rubik[0][0])
    rubik[0][0][2], rubik[0][0][1], rubik[0][0][0] = rubik[0][2][2], rubik[0][1][2], rubik[0][0][2]
    rubik[0][2][2], rubik[0][1][2], rubik[0][0][2] = rubik[0][2][0], rubik[0][2][1], rubik[0][2][2]
    rubik[0][2][0], rubik[0][2][1], rubik[0][2][2] = rubik[0][0][0], rubik[0][1][0], rubik[0][2][0]
    rubik[0][0][0], rubik[0][1][0], rubik[0][2][0] = temp[2], temp[1], temp[0]
    # Rotate each row of a side that connects to the top side
    temp = deepcopy(rubik[1][0])
    rubik[1][0][0], rubik[1][0][1], rubik[1][0][2] = rubik[2][0][0], rubik[2][0][1], rubik[2][0][2]
    rubik[2][0][0], rubik[2][0][1], rubik[2][0][2] = rubik[3][0][0], rubik[3][0][1], rubik[3][0][2]
    rubik[3][0][0], rubik[3][0][1], rubik[3][0][2] = rubik[4][0][0], rubik[4][0][1], rubik[4][0][2]
    rubik[4][0][0], rubik[4][0][1], rubik[4][0][2] = temp[0], temp[1], temp[2]

def D(rubik):
    # Rotate bottom side
    temp = deepcopy(rubik[5][0])
    rubik[5][0][0], rubik[5][0][1], rubik[5][0][2] = rubik[5][2][0], rubik[5][1][0], rubik[5][0][0]
    rubik[5][2][0], rubik[5][1][0], rubik[5][0][0] = rubik[5][2][2], rubik[5][2][1], rubik[5][2][0]
    rubik[5][2][2], rubik[5][2][1], rubik[5][2][0] = rubik[5][0][2], rubik[5][1][2], rubik[5][2][2]
    rubik[5][0][2], rubik[5][1][2], rubik[5][2][2] = temp[0], temp[1], temp[2]
    # Rotate each row of a side that connects to the bottom side
    temp = deepcopy(rubik[1][2])
    rubik[1][2][0], rubik[1][2][1], rubik[1][2][2] = rubik[2][2][0], rubik[2][2][1], rubik[2][2][2]
    rubik[2][2][0], rubik[2][2][1], rubik[2][2][2] = rubik[3][2][0], rubik[3][2][1], rubik[3][2][2]
    rubik[3][2][0], rubik[3][2][1], rubik[3][2][2] = rubik[4][2][0], rubik[4][2][1], rubik[4][2][2]
    rubik[4][2][0], rubik[4][2][1], rubik[4][2][2] = temp[0], temp[1], temp[2]

def Di(rubik):
    # Rotate bottom side
    temp = deepcopy(rubik[5][0])
    rubik[5][0][2], rubik[5][0][1], rubik[5][0][0] = rubik[5][2][2], rubik[5][1][2], rubik[5][0][2]
    rubik[5][2][2], rubik[5][1][2], rubik[5][0][2] = rubik[5][2][0], rubik[5][2][1], rubik[5][2][2]
    rubik[5][2][0], rubik[5][2][1], rubik[5][2][2] = rubik[5][0][0], rubik[5][1][0], rubik[5][2][0]
    rubik[5][0][0], rubik[5][1][0], rubik[5][2][0] = temp[2], temp[1], temp[0]
    # Rotate each row of a side that connects to the bottom side
    temp = deepcopy(rubik[1][2])
    rubik[1][2][2], rubik[1][2][1], rubik[1][2][0] = rubik[4][2][2], rubik[4][2][1], rubik[4][2][0]
    rubik[4][2][2], rubik[4][2][1], rubik[4][2][0] = rubik[3][2][2], rubik[3][2][1], rubik[3][2][0]
    rubik[3][2][2], rubik[3][2][1], rubik[3][2][0] = rubik[2][2][2], rubik[2][2][1], rubik[2][2][0]
    rubik[2][2][2], rubik[2][2][1], rubik[2][2][0] = temp[2], temp[1], temp[0]

def F2(rubik):
    F(rubik)
    F(rubik)

def R2(rubik):
    R(rubik)
    R(rubik)

def U2(rubik):
    U(rubik)
    U(rubik)

def B2(rubik):
    B(rubik)
    B(rubik)

def L2(rubik):
    L(rubik)
    L(rubik)

def D2(rubik):
    D(rubik)
    D(rubik)

def printCube(rubik):
    for side in rubik:
        print("A new side")
        for col in side:
            print(col)

def calculateCost(rubik, state):
    totalCost = 0
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if (state[i][j][k] == 0):
                    continue
                else:
                    if (state[i][j][k] != rubik[i][j][k]):
                        totalCost += 1
    return totalCost

def getLastMove(moveHistory):
    listMove = []
    if (len(moveHistory) != 0):
        listMove.append(moveHistory[len(moveHistory) - 1])
        if (listMove[0] == 'i'):
            listMove.insert(0, moveHistory[len(moveHistory) - 2])
    lastMove = ''.join(listMove)
    return lastMove


def processLiveNodeBB(currentNode, evolvingState, queue):
    liveNode = []
    liveNode.append(currentNode)
    nextNodeIdx = 12
    while(True):
        if (not queue.empty()):
            return None
        currentNode = liveNode.pop(0)
        if (currentNode[3] == 0):
            break
        lastMove = getLastMove(currentNode[2])
        if (lastMove != 'Fi' and lastMove != 'F'):
            nextRubik = deepcopy(currentNode[1])
            F(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'F', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ri' and lastMove != 'R'):
            nextRubik = deepcopy(currentNode[1])
            R(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'R', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ui' and lastMove != 'U'):
            nextRubik = deepcopy(currentNode[1])
            U(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'U', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Bi' and lastMove != 'B'):
            nextRubik = deepcopy(currentNode[1])
            B(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'B', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Li' and lastMove != 'L'):
            nextRubik = deepcopy(currentNode[1])
            L(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'L', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Di' and lastMove != 'D'):
            nextRubik = deepcopy(currentNode[1])
            D(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'D', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'F' and lastMove != 'Fi'):
            nextRubik = deepcopy(currentNode[1])
            Fi(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Fi', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'R' and lastMove != 'Ri'):
            nextRubik = deepcopy(currentNode[1])
            Ri(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Ri', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'U' and lastMove != 'Ui'):
            nextRubik = deepcopy(currentNode[1])
            Ui(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Ui', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'B' and lastMove != 'Bi'):
            nextRubik = deepcopy(currentNode[1])
            Bi(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Bi', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'L' and lastMove != 'Li'):
            nextRubik = deepcopy(currentNode[1])
            Li(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Li', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'D' and lastMove != 'Di'):
            nextRubik = deepcopy(currentNode[1])
            Di(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Di', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Fi' and lastMove != 'F'):
            nextRubik = deepcopy(currentNode[1])
            F2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'FF', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ri' and lastMove != 'R'):
            nextRubik = deepcopy(currentNode[1])
            R2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'RR', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ui' and lastMove != 'U'):
            nextRubik = deepcopy(currentNode[1])
            U2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'UU', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Bi' and lastMove != 'B'):
            nextRubik = deepcopy(currentNode[1])
            B2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'BB', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Li' and lastMove != 'L'):
            nextRubik = deepcopy(currentNode[1])
            L2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'LL', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Di' and lastMove != 'D'):
            nextRubik = deepcopy(currentNode[1])
            D2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'DD', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        mergeSortLiveNode(liveNode, 0, len(liveNode) - 1)
    queue.put(1)
    return currentNode

def processLiveNodeBFS(currentNode, evolvingState, queue):
    liveNode = []
    liveNode.append(currentNode)
    nextNodeIdx = 12
    while(True):
        if (not queue.empty()):
            return None
        currentNode = liveNode.pop(0)
        if (currentNode[3] == 0):
            break
        lastMove = getLastMove(currentNode[2])
        if (lastMove != 'Fi' and lastMove != 'F'):
            nextRubik = deepcopy(currentNode[1])
            F(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'F', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ri' and lastMove != 'R'):
            nextRubik = deepcopy(currentNode[1])
            R(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'R', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ui' and lastMove != 'U'):
            nextRubik = deepcopy(currentNode[1])
            U(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'U', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Bi' and lastMove != 'B'):
            nextRubik = deepcopy(currentNode[1])
            B(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'B', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Li' and lastMove != 'L'):
            nextRubik = deepcopy(currentNode[1])
            L(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'L', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Di' and lastMove != 'D'):
            nextRubik = deepcopy(currentNode[1])
            D(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'D', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'F' and lastMove != 'Fi'):
            nextRubik = deepcopy(currentNode[1])
            Fi(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Fi', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'R' and lastMove != 'Ri'):
            nextRubik = deepcopy(currentNode[1])
            Ri(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Ri', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'U' and lastMove != 'Ui'):
            nextRubik = deepcopy(currentNode[1])
            Ui(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Ui', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'B' and lastMove != 'Bi'):
            nextRubik = deepcopy(currentNode[1])
            Bi(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Bi', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'L' and lastMove != 'Li'):
            nextRubik = deepcopy(currentNode[1])
            Li(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Li', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'D' and lastMove != 'Di'):
            nextRubik = deepcopy(currentNode[1])
            Di(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'Di', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Fi' and lastMove != 'F'):
            nextRubik = deepcopy(currentNode[1])
            F2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'FF', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ri' and lastMove != 'R'):
            nextRubik = deepcopy(currentNode[1])
            R2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'RR', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Ui' and lastMove != 'U'):
            nextRubik = deepcopy(currentNode[1])
            U2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'UU', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Bi' and lastMove != 'B'):
            nextRubik = deepcopy(currentNode[1])
            B2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'BB', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Li' and lastMove != 'L'):
            nextRubik = deepcopy(currentNode[1])
            L2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'LL', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
        if (lastMove != 'Di' and lastMove != 'D'):
            nextRubik = deepcopy(currentNode[1])
            D2(nextRubik)
            nextNodeIdx += 1
            nextNode = [nextNodeIdx, nextRubik, currentNode[2] + 'DD', calculateCost(nextRubik, evolvingState)]
            liveNode.append(nextNode)
    queue.put(1)
    return currentNode

def mergeSortLiveNode(liveNode, start, end):
    if (start < end):
        mid = floor((start + end)/2)
        mergeSortLiveNode(liveNode, start, mid)
        mergeSortLiveNode(liveNode, mid + 1, end)
        mergeLiveNode(liveNode, start, mid, end)
    

def mergeLiveNode(liveNode, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    leftArr = []
    for a in range(n1):
        leftArr.append(liveNode[start + a])
    rightArr = []
    for b in range(n2):
        rightArr.append(liveNode[mid + 1 + b])
    
    i = 0
    j = 0
    k = start

    while (i < n1 and j < n2):
        cleanMoveHistory1 = calculatePath(leftArr[i][2])
        cleanMoveHistory2 = calculatePath(rightArr[j][2])
        if (leftArr[i][3] < rightArr[j][3]):
            liveNode[k] = leftArr[i]
            i += 1
        elif (cleanMoveHistory1 + leftArr[i][3] <= cleanMoveHistory2 + rightArr[j][3]):
            liveNode[k] = leftArr[i]
            i += 1
        else:
            liveNode[k] = rightArr[j]
            j += 1
        k += 1
    
    while(i < n1):
        liveNode[k] = leftArr[i]
        i += 1
        k += 1
    
    while(j < n2):
        liveNode[k] = rightArr[j]
        j += 1
        k += 1

def printPath(pathList):
    curIndex = 0
    while curIndex < len(pathList):
        curPath = ''
        curPath += pathList[curIndex]
        if (curIndex + 1 == len(pathList)):
            print(curPath)
            break
        if (pathList[curIndex + 1] == 'i'):
            nextPath = ''
            curIndex += 1
            curPath += pathList[curIndex]
            if (curIndex + 1 == len(pathList)):
                print(curPath)
                break
            nextPath += pathList[curIndex + 1]
            if (curIndex + 2 == len(pathList)):
                print(curPath, end=' ')
                print(nextPath)
                break
            nextPath += pathList[curIndex + 2]
            if (nextPath == curPath):
                curIndex += 2
                if (curIndex + 1 == len(pathList)):
                    print(curPath[0] + '2')
                else:
                    print(curPath[0] + '2', end=' ')
            else:
                print(curPath, end=' ')
        else:
            if (curIndex + 2 == len(pathList)):
                if (pathList[curIndex + 1] == curPath):
                    print(curPath + '2')
                    break
                else:
                    print(curPath, end=' ')
                    print(pathList[curIndex + 1])
                    break
            if (pathList[curIndex + 2] != 'i'):
                if (pathList[curIndex + 1] == curPath):
                    curIndex += 1
                    print(curPath + '2', end=' ')

                else:
                    print(curPath, end=' ')
            else:
                print(curPath, end=' ')
        curIndex += 1

def calculatePath(pathList):
    i = 0
    total = 0
    while (i < len(pathList)):
        currentPath = pathList[i]
        total += 1
        if (i + 1 == len(pathList)):
            break
        if (pathList[i + 1] == 'i'):
            nextPath = ''
            i += 1
            currentPath += pathList[i]
            if (i + 1 == len(pathList)):
                break
            if (i + 2 == len(pathList)):
                total += 1
                break
            nextPath += pathList[i + 1]
            nextPath += pathList[i + 2]
            if (currentPath == nextPath):
                i += 2
        else:
            if (i + 2 == len(pathList)):
                if (pathList[i + 1] != currentPath):
                    total += 1
                break
            else:
                if (pathList[i + 1] == currentPath and pathList[i + 2] != 'i'):
                    i += 1
        i += 1
    return total

def scrambleCube(rubik, scrambleList):
    for notation in scrambleList:
        match notation:
            case 'F':
                F(rubik)
            case 'R':
                R(rubik)
            case 'U':
                U(rubik)
            case 'B':
                B(rubik)
            case 'L':
                L(rubik)
            case 'D':
                D(rubik)
            case 'Fi':
                Fi(rubik)
            case 'Ri':
                Ri(rubik)
            case 'Ui':
                Ui(rubik)
            case 'Bi':
                Bi(rubik)
            case 'Li':
                Li(rubik)
            case 'Di':
                Di(rubik)
            case 'F2':
                F2(rubik)
            case 'R2':
                R2(rubik)
            case 'U2':
                U2(rubik)
            case 'B2':
                B2(rubik)
            case 'L2':
                L2(rubik)
            case 'D2':
                D2(rubik)


    
            

