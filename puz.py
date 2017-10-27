import sys
import numpy as np
import copy
import Queue as Q
class child():
    def __init__(self, n,state, cost):
          self.Cost = cost
          self.Node = n
          self.Cost = cost
          self.STATE = state
    def __cmp__(self, other):
        return cmp(self.Cost, other.priority)

class problem():
    def __init__(self,initial_node, state, cost,g):
      self.node = copy.deepcopy(initial_node)
      self.C = 1
      self.initial_state = None
      self.goal = g
    def Goal_Test(self,n):
        if np.array_equal(n, self.goal):
            return True
        else:
            return False

    def Actions(self,node):
        matrixs = []
        row,col = node.shape
        row = row-1
        col = col-1
        loc =[]
        print(row, col)
        i = 0
        while i < row:
            j = 0
            while j < col:
                if node.item(i,j) == 0:
                    row = i
                    col = j
                    break
                j=j+1
            i=i+1
        print("row, col", row,col)
        print("node needs actions", node)
        if  j < col :                    #checking if you can move to the right
            child1 = copy.deepcopy(node)
            temp = child1.item(i,j)
            temp2 = child1.item(i,j+1)
            child1[i,j] = temp2
            child1[i,j+1] = temp
            print("right")
            matixs.append(child1)
        if  j > 0:                      #checking if you could move to the left
            child2 = copy.deepcopy(node)
            temp = child2.item(i,j)
            child2[i,j] = child2.item(i,j-1)
            child2[i,j-1] = temp
            matrixs.append(child2)
            print("left",child2)

        if  i < row :                #checking if you could move to the bottom
            chidl3 = copy.deepcopy(node)
            temp = child3.item(i,j)
            child3[i,j] = child3.item(i+1,j)
            child3[i+1,j] = temp
            matrixs.append(child3)
            print("bottom",child3)

        if  i > 0:                 #checking if yopu could move to the top
            child4 = copy.deepcopy(node)
            temp = child4.item(i,j)
            child4[i,j] = child4.item(i-1,j)
            child4[i-1,j] = temp
            matrixs.append(child4)
            print("top",child4)

        return matrixs
def notFrontierOrExplore( node, frontier, explore):

    while not frontier.empty():
        temp1 = frontier.get()
        if np.array_equal(node, temp1):
            return False
    cexpplore = copy.deepcopy(explore)
    for i in explore:
        if np.array_equal(node, i):
            return False
    return True
def inFrontierWithHigherCost(node):
    while not frontier.empty():
        temp1 = frontier.get()
        if np.array_equal(node, temp1):
            return False
    cexpplore = copy.deepcopy(explore)




def Unifor_Cost_Search(problem):
    node = child(problem.node,"problem", 0)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    explore = []
    i = 0
    while i < 2:
        if frontier.empty():
            return 'failure'
        print(frontier,"iterating at ", i)
        node1 = frontier.get()
        print("loop", node1.Node)

        if problem.Goal_Test(node1.Node) == True:
            return node1.Node
        e = problem.Actions(node1.Node)
        print(e,"allow actions")
        j=0
        while j < len(e):
            eachAction = e[j]
            print("actions each", eachAction)
            childa = child(eachAction,"problem",node1.Cost+1)
            if notFrontierOrExplore(childa,frontier,explore):
                frontier.put(childa)
                print("not in expore or frontier", childa.Node)

            j=1+j
        i=i+1


if __name__ == "__main__":
    goal = np.matrix([[1,2,3], [4,5,6], [7,8,0]])
    print("Welcome to Bertie Woosters 8-puzzle solver. ")
    ValInput = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle\n" )
    if ValInput ==  1:
        m = np.matrix([[2,1,3], [4,5,6], [7,8,0]])
        print(len(m))

        p = problem(m,None,0,goal)

        print("Enter your choice of algorithm")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic.")
        algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))
        if algorithmType == 1:
            Unifor_Cost_Search(p)


    elif ValInput == 2:
        print("Enter your puzzle, use a zero to represent the blank")
        rowOne = raw_input("Enter the first row, use space or tabs between numbers\n" )
        rowTwo = raw_input("Enter the second row, use space or tabs between numbers\n")
        rowTree = raw_input("Enter the third row, use space or tabs between numbers\n")
        rowOne = map(int, rowOne.split())
        rowTwo = map(int, rowTwo.split())
        rowTree = map(int, rowTree.split())
        m = (rowOne,rowTwo,rowTree)
        problem = parent(m,0)
        print("Enter your choice of algorithm")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic.")
        algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))
        if algorithmType == 1:
            Unifor_Cost_Search(problm)
