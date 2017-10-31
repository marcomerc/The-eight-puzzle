import sys
import numpy as np
import copy
import Queue as Q
class child():
    def __init__(self, n,state, cost):
          self.priority = cost
          self.Cost = cost
          self.Node = n
          self.Cost = cost
          self.STATE = state
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

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
        loc =[0,0]

        i = 0
        print(node,"where is zero")
        while i <= row:
            j= 0
            while j <= col:
                print(node[i,j])
                if node[i,j] == 0:
                    loc[0] = i
                    loc[1] = j
                    break
                j=j+1
            i=i+1
        # print("row, col", loc)
        i = i-1
        j = j-1
        print(i,j)
        # print("node needs actions", node)
        if  i > loc[1] :                    #checking if you can move to the right
            child1 = copy.deepcopy(node)
            temp = child1.item(loc[0],loc[1])
            child1[loc[0],loc[1]] = child1.item(loc[0],loc[1]+1)
            child1[loc[0],loc[1]+1] = temp
            # print("right",child1)
            matrixs.append(child1)
        if   0 < loc[1]:                      #checking if you could move to the left
            child2 = copy.deepcopy(node)
            temp = child2.item(loc[0],loc[1])
            child2[loc[0],loc[1]] = child2.item(loc[0],loc[1]-1)
            child2[loc[0],loc[1]-1] = temp
            matrixs.append(child2)
            # print("left",child2)

        if  i > loc[0] :                #checking if you could move to the bottom
            child3 = copy.deepcopy(node)
            temp = child3.item(loc[0],loc[1])
            child3[loc[0],loc[1]] = child3.item(loc[0]+1,loc[1])
            child3[loc[0]+1,loc[1]] = temp
            matrixs.append(child3)
            # print("bottom",child3)

        if  0 < loc[0]:                 #checking if yopu could move to the top
            child4 = copy.deepcopy(node)
            temp = child4.item(loc[0],loc[1])
            child4[loc[0],loc[1]] = child4.item(loc[0]-1,loc[1])
            child4[loc[0]-1,loc[1]] = temp
            matrixs.append(child4)
            # print("top",child4)

        return matrixs
def notFrontierOrExplore( node, frontier, explore):
    qu = Q.PriorityQueue()
    qu.queue = copy.deepcopy(frontier.queue)

    while not qu.empty():
        temp1 = qu.get()
        # print("checking if its in  frontier\n",temp1.Node)
        if np.array_equal(node.Node, temp1.Node):
            # print("in frontier" )
            return False

    cexpplore = copy.deepcopy(explore)
    for i in explore:
        if np.array_equal(node.Node, i.Node):
            # print("in explore")
            return False
    return True
def inFrontierWithHigherCost(node,frontier):
    qu = Q.PriorityQueue()
    qu.queue = copy.deepcopy(frontier.queue)
    while not qu.empty():
        temp1 = qu.get()
        if node.Cost < temp1.Cost and np.array_equal(temp1.node,node.Node):
            return True
    return False

def Unifor_Cost_Search(problem):
    node = child(problem.node,"problem", 1)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    frontierHash  = {}
    explore = []
    i = 0
    while  True:
        # print("the len of explore", len(explore), "the size of the q",len(frontier))
        # print("is the frontier empty ? ", frontier.empty())
        if frontier.empty():
            return 'failure'
        node1 = frontier.get()

        # print("loop", node1.Node)
        if problem.Goal_Test(node1.Node) == True:
            return node1.Node
        explore.append(node1)
        t = []
        print("number of child expand",i, )
        for eachAction in problem.Actions(node1.Node):

                childnode = copy.deepcopy(eachAction)
                childa = copy.deepcopy(child(childnode,"problem",node1.Cost+1))
                # print("len",  len(t))

                if notFrontierOrExplore(childa,frontier,explore):


                    t.append(childa)
                    # print("not in expore or frontier", childa.Node)
                elif inFrontierWithHigherCost(childa,frontier):
                    print(" with lower Cost")
        j = 0




        while(j < len(t)):
            # print(t[j].Cost)
            # frontierHash[t[j]] ==  t[j]
            frontier.put(t[j])
            j = j+1
        i=i+1


if __name__ == "__main__":
    goal = np.matrix([[1,2,3], [4,5,6], [7,8,0]])
    print("Welcome to Bertie Woosters 8-puzzle solver. ")
    ValInput = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle\n" )
    if ValInput ==  1:
        m = np.matrix([[7,6,8], [3,0,4], [2,5,1]])
        print(len(m))

        p = problem(m,None,0,goal)

        print("Enter your choice of algorithm")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic.")
        algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))
        if algorithmType == 1:
            wow = Unifor_Cost_Search(p)
            print("solution",wow)


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
