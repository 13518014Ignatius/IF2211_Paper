from itertools import repeat
from multiprocessing import Manager, Pool
from rubik import *
import time

finishState =       [[[1,1,1],[1,1,1],[1,1,1]], 
                     [[2,2,2],[2,2,2],[2,2,2]],
                     [[3,3,3],[3,3,3],[3,3,3]],
                     [[4,4,4],[4,4,4],[4,4,4]],
                     [[5,5,5],[5,5,5],[5,5,5]],
                     [[6,6,6],[6,6,6],[6,6,6]]]

if __name__ == '__main__':
    rubik = deepcopy(finishState)
    print("Enter scramble notation text file path here:")
    fileName = input()
    txtFile = open(fileName, 'r')
    fileContent = txtFile.read()
    scrambleList = fileContent.split(' ')
    txtFile.close()
    scrambleCube(rubik, scrambleList)
    solvingMethod = ''
    print("What method would you like to use to solve the puzzle? Type the number only")
    print("1. BFS")
    print("2. Branch & Bound")
    inputNum = int(input())
    if (inputNum == 1):
        solvingMethod += 'BFS'
    elif (inputNum == 2):
        solvingMethod += 'BB'
    liveNode = []
    currentNode = [0, rubik, '', calculateCost(rubik, finishState)]
    nextNodeIdx = 0
    totalNodeIdx = 0
    if (currentNode[3] != 0):
        nextRubik = deepcopy(rubik)
        F(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'F', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        R(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'R', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        U(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'U', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        B(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'B', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        L(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'L', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        D(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'D', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        Fi(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'Fi', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        Ri(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'Ri', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        Ui(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'Ui', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        Bi(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'Bi', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        Li(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'Li', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        Di(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'Di', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        F2(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'FF', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        R2(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'RR', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        U2(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'UU', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        B2(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'BB', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        L2(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'LL', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)
        nextRubik = deepcopy(rubik)
        D2(nextRubik)
        nextNodeIdx += 1
        nextNode = [nextNodeIdx, nextRubik, 'DD', calculateCost(nextRubik, finishState)]
        liveNode.append(nextNode)

        if (solvingMethod == 'BB'): 
            mergeSortLiveNode(liveNode, 0, len(liveNode) - 1)

        manager = Manager()
        queue = manager.Queue()
        pool = Pool(processes=16)
        if (solvingMethod == 'BFS'):
            start = time.perf_counter()
            resultNode = pool.starmap(processLiveNodeBFS, zip(liveNode, repeat(finishState), repeat(queue)))
            finish = time.perf_counter()
        elif (solvingMethod == 'BB'):
            start = time.perf_counter()
            resultNode = pool.starmap(processLiveNodeBB, zip(liveNode, repeat(finishState), repeat(queue)))
            finish = time.perf_counter()
        resultNode = [node for node in resultNode if node != None]
        currentNode = resultNode[0]

        print("The notations to solve the puzzle are:")
        printPath(currentNode[2])
        print(f"Execution time to solve the puzzle is {round(finish - start, 2)} second(s)")
    