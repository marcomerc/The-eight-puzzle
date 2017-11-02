import sys
import numpy as np
import copy
import timeit
import Queue as Q
class child():                     # the class that i made for each node.
    # the way the class is initialized and takes in the following items
    def __init__(self, n,state, cost,d):
      self.priority = cost          #the priority to keep track of the queue
      self.Cost = cost                # the cost is set to cost
      self.Node = n                 #the node itself
      self.STATE = state            # the state.
      self.depth = d                #keeps track of the depth of the node
    def __hash__(self):
         return hash(self.Node)      # this is for the has table. and what to hash
    def __cmp__(self, other):       #what the queue is organized,
        return cmp(self.Cost, other.priority) # by the priiority which is the cost
dic = {}                               #this dictionary is use to find the locations of each
dic[1] = [0,0]                          #element in the goal state
dic[2] = [0,1]
dic[3] = [0,2]
dic[4] = [1,0]
dic[5] = [1,1]
dic[6] = [1,2]
dic[7] = [2,0]
dic[8] = [2,1]
dic[0] = [2,2]
class problem():        # a class for the problem.
# the initialization of the problem class
    def __init__(self,initial_node, state, cost,g):
      self.node = copy.deepcopy(initial_node)
      self.C = 1
      self.initial_state = None
      self.goal = g
      #a function checks if the node passed in is the same as the goal.
      # if a solution was found
    def Goal_Test(self,node):
        if np.array_equal(node, self.goal):
            return True
        else:
            return False
    #passing in node checks if the possible ways of nodes that could be expand too
    # and returns them.
    def Actions(self,node):
        matrixs = []
        row,col = node.shape
        row = row-1
        col = col-1
        loc =[0,0]

        i = 0
        #this finds where thez zero is located in the node.
        while i <= row:
            j= 0
            while j <= col:
                # print(node[i,j])
                if node[i,j] == 0:
                    loc[0] = i
                    loc[1] = j
                    break
                j=j+1
            i=i+1
        i = i-1
        j = j-1
        # checks base on the location of zoro what it could expand too
        if  i > loc[1] :                    #checking if you can move to the right
            child1 = copy.deepcopy(node)   #making a copy of the node and change the values
            temp = child1.item(loc[0],loc[1])
            child1[loc[0],loc[1]] = child1.item(loc[0],loc[1]+1)
            child1[loc[0],loc[1]+1] = temp
            # print("right",child1)
            matrixs.append(child1)
        if   0 < loc[1]:                      #checking if you could move to the left
            child2 = copy.deepcopy(node)       #making a copy of the node and change the values
            temp = child2.item(loc[0],loc[1])
            child2[loc[0],loc[1]] = child2.item(loc[0],loc[1]-1)
            child2[loc[0],loc[1]-1] = temp
            matrixs.append(child2)
            # print("left",child2)

        if  i > loc[0] :                #checking if you could move to the bottom
            child3 = copy.deepcopy(node) #making a copy of the node and change the values
            temp = child3.item(loc[0],loc[1])
            child3[loc[0],loc[1]] = child3.item(loc[0]+1,loc[1])
            child3[loc[0]+1,loc[1]] = temp
            matrixs.append(child3)
            # print("bottom",child3)

        if  0 < loc[0]:                 #checking if yopu could move to the top
            child4 = copy.deepcopy(node) #making a copy of the node and change the values
            temp = child4.item(loc[0],loc[1])
            child4[loc[0],loc[1]] = child4.item(loc[0]-1,loc[1])
            child4[loc[0]-1,loc[1]] = temp
            matrixs.append(child4)
            # print("top",child4)

        return matrixs
    #checking if the node exist in the frontier or the explore.
def notFrontierOrExplore( node, frontier, explore):
    #iterating throught frontier and checking if its equal to node
    for key in frontier:
        if np.array_equal(frontier[key].Node,node.Node):
            return False
    #iterating throught explore and see if its equal to the node.
    i = 0
    while i < len(explore):
        if np.array_equal(node.Node,explore[i].Node):
            return False
        i+=1
    return True
def inFrontierWithHigherCost(node,frontier):
    #checking if  its in the frontier with a higher cost.
    for key in frontier:
        if np.array_equal(frontier[key].Node,node.Node):
            if frontier[key].Cost > node.Cost:
                return True

    return False
#checking  how many tiles are misplace.
def misplaceTilesHeristic(node):
    compare =np.matrix([[1,2,3], [4,5,6], [7,8,0]])
    i = 0
    count = 0
    row,col = node.shape
    # print(node,"where is zero")
    while i <= row-1:
        j= 0
        while j <= col-1:
            if node[i,j] != compare[i,j]:
                count =count+1
            j=j+1
        i=i+1
    return count
#checking the ManhattanDistance and calculate it
def ManhattanDistance(node):
    count = 0
    i = 0
    row,col = node.shape
    # print(node,"where is zero")
    while i <= row-1:
        j= 0
        while j <= col-1:
            loc = dic[ node[i,j] ]      # use a dictionary to get locations of goal state tiles.
            count =count+ abs(loc[0] - i) + abs(loc[1] - j)
            j=j+1
        i=i+1
    return count


def Unifor_Cost_Search(problem):
    node = child(problem.node,None, 0,0)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    frontierHash  = {}
    explore = []
    i = 0
    numFront = 1
    maxFront = 1
    while  True:
        if frontier.empty():
            return 'failure'
        node1 = frontier.get()
        numFront-=1
        if maxFront < numFront:
            maxFront = numFront

        # print("loop", node1.Node)
        if problem.Goal_Test(node1.Node) == True:
            return node1,i,maxFront
        explore.append(node1)
        # print("number of child expand",i, )
        for eachAction in problem.Actions(node1.Node):
                childnode = copy.deepcopy(eachAction)
                childa = copy.deepcopy(child(childnode,copy.deepcopy(node1),node1.Cost+1,node1.depth+1))
                if notFrontierOrExplore(childa,frontierHash,explore):
                    frontierHash[childa] =  childa
                    frontier.put(childa)
                    numFront+=1
                elif inFrontierWithHigherCost(childa,frontierHash):
                    frontierHash[childa] = childa
                    frontier.put(childa)

        i=i+1


def  misplaceTiles(problem):
    node = child(problem.node,None, 1,0)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    frontierHash  = {}
    explore = []
    i = 0
    numFront = 1
    maxFront = 1
    while  True:
        i=i+1
        if frontier.empty():
            return 'failure'
        node1 = frontier.get()
        numFront-=1
        if maxFront < numFront:
            maxFront = numFront

        if problem.Goal_Test(node1.Node) == True:
            return node1,i,maxFront
        explore.append(node1)
        for eachAction in problem.Actions(node1.Node):
                childnode = copy.deepcopy(eachAction)
                childa = copy.deepcopy(child(childnode,copy.deepcopy(node1),node1.depth+misplaceTilesHeristic(eachAction),node1.depth+1))
                if notFrontierOrExplore(childa,frontierHash,explore):
                    frontierHash[childa] =  childa
                    frontier.put(childa)
                    numFront+=1
                elif inFrontierWithHigherCost(childa,frontierHash):
                    frontierHash[childa] = childa
                    frontier.put(childa)
        i+=1

def  Manhattan(problem):
    node = child(problem.node,None, 1,0)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    frontierHash  = {}
    explore = []
    i = 0
    numFront = 1
    maxFront = 1
    while  True:

        if frontier.empty():
            return 'failure'

        node1 = frontier.get()
        if maxFront < numFront:
            maxFront = numFront
        if problem.Goal_Test(node1.Node) == True:
            return node1,i,maxFront
        explore.append(node1)
        for eachAction in problem.Actions(node1.Node):
                childnode = copy.deepcopy(eachAction)
                childa = copy.deepcopy(child(childnode,node1,node1.depth+ ManhattanDistance(eachAction),node1.depth+1))
                if notFrontierOrExplore(childa,frontierHash,explore):
                    frontierHash[childa] =  childa
                    frontier.put(childa)
                    numFront+=1
                elif inFrontierWithHigherCost(childa,frontierHash):
                    frontierHash[childa] = childa
                    frontier.put(childa)
        i+=1
def printaa(w):
    wow = w[0]
    s = []
    g = wow.STATE

    while not np.array_equal(wow.Node,m):
        s.append(copy.deepcopy(wow))
        wow = wow.STATE
    i = len(s) - 1
    print("Expanding  state")
    print(m)

    while i > 0 :

        print("The best state to expand with a g(n) = ", s[i].Cost, " and h(n) =", 0 )
        print(s[i].Node)
        i-=1
    print("Goal!!!")
    print("to solve the problem the search algorithm expanded a total of",w[1], "nodes.")
    print("the maximum number of nodes in the queue at any one time was ", w[2])
    print(w[0].depth)





if __name__ == "__main__":
    goal = np.matrix([[1,2,3], [4,5,6], [7,8,0]])
    print("Welcome to Bertie Woosters 8-puzzle solver. ")
    ValInput = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle" )
    if ValInput ==  1:
        m = np.matrix([[1,2,3], [7,4,0], [8,6,5]])
        print(len(m))
        p = problem(m,None,0,goal)


        # print("Enter your choice of algorithm")
        # print("1. Uniform Cost Search")
        # print("2. A* with the Misplaced Tile heuristic.")
        # algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))
        # if algorithmType == 1:
        start = timeit.timeit()
        wow = Unifor_Cost_Search(p)
        end = timeit.timeit()
        print("time",abs(end - start) )
        printaa(wow)
        # if algorithmType == 2:
        start = timeit.timeit()
        wow = misplaceTiles(p)
        end = timeit.timeit()
        print("time",abs(end - start) )
        printaa(wow)
        # if algorithmType == 3:
        s = timeit.timeit()
        wow = Manhattan(p)
        e = timeit.timeit()
        print("time",e - s)
        printaa(wow)



    elif ValInput == 2:
        print("Enter your  puzzle, use a zero to represent the blank")
        rowOne = raw_input("Enter the first row, use space or tabs between numbers\n" )
        rowTwo = raw_input("Enter the second row, use space or tabs between numbers\n")
        rowTree = raw_input("Enter the third row, use space or tabs between numbers\n")
        rowOne = map(int, rowOne.split())
        rowTwo = map(int, rowTwo.split())
        rowTree = map(int, rowTree.split())
        print(rowOne)
        m = np.matrix([rowOne,rowTwo,rowTree])
        p = problem(m,None,0, goal)
        print("Enter your choice of algorithm")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic.")
        algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))

        if algorithmType == 1:
            wow = Unifor_Cost_Search(p)
            printaa(wow)
        if algorithmType == 2:
            wow = misplaceTiles(p)
            printaa(wow)
        if algorithmType == 3:
            wow = Manhattan(p)
            printaa(wow)
