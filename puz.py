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
            count =count+ abs(loc[0] - i) + abs(loc[1] - j) # calculates the distance in manhattan
            j=j+1
        i=i+1
    return count


def Unifor_Cost_Search(problem): # uniform cost function
    node = child(problem.node,None, 0,0)        #creating the root
    frontier =  Q.PriorityQueue()       # the queue
    frontier.put(node)                  #putting the queue in the frontier
    frontierHash  = {}                  #i also kept a dictionary to access them faster.
    explore = []
    i = 0
    numFront = 1
    maxFront = 1
    print("expanding state")
    print(node.Node)
    while  True:                        #while true
        if frontier.empty():            #check if frontier is the empty
            return 'failure'
        node1 = frontier.get()
        numFront-=1
        if maxFront < numFront:         #keeping track of  max in the frontier
            maxFront = numFront

        # print("loop", node1.Node)
        if problem.Goal_Test(node1.Node) == True: #check if we achieve the goal state
            return node1,i,maxFront
        explore.append(node1)               #add it too the explore
        print("The best state to expand with a g(n) = ", node1.Cost, " and h(n) =", 0 ) ## the steps that we expanded
        print(node1.Node)
        for eachAction in problem.Actions(node1.Node): #expand the state
                childnode = copy.deepcopy(eachAction)
                childa = copy.deepcopy(child(childnode,copy.deepcopy(node1),node1.Cost+1,node1.depth+1))
                if notFrontierOrExplore(childa,frontierHash,explore):    # check it its not in frontier or explore
                    frontierHash[childa] =  childa
                    frontier.put(childa)
                    numFront+=1
                elif inFrontierWithHigherCost(childa,frontierHash): #check if its in frontier with a higher cost
                    frontierHash[childa] = childa
                    frontier.put(childa)


        i=i+1


def  misplaceTiles(problem): # function for the misplaceTiles
    node = child(problem.node,None, 1,0)
    frontier =  Q.PriorityQueue()       #set uup the frontier
    frontier.put(node)
    frontierHash  = {}                  # a dictionary too for frontier
    explore = []
    i = 0
    numFront = 1
    maxFront = 1
    print("expanding state")
    print(node.Node)
    while  True:
        i=i+1
        if frontier.empty():            #check if the frontier is empty
            return 'failure'
        node1 = frontier.get()
        numFront-=1
        if maxFront < numFront:      #keep track of the number of max in frontier
            maxFront = numFront

        if problem.Goal_Test(node1.Node) == True: #if goal return goal, expanded notes and max in fron tier
            return node1,i,maxFront
        explore.append(node1)
        print("The best state to expand with a g(n) = ", node1.Cost, " and h(n) =", misplaceTilesHeristic(node1.Node) ) ## the steps that we expanded
        print(node1.Node)

        for eachAction in problem.Actions(node1.Node): #expand the node
                childnode = copy.deepcopy(eachAction)
                #created the new nodes here with the new cost of misplace tiles
                childa = copy.deepcopy(child(childnode,copy.deepcopy(node1),node1.depth+misplaceTilesHeristic(eachAction),node1.depth+1))
                if notFrontierOrExplore(childa,frontierHash,explore): #check if its in frontier or explore
                    frontierHash[childa] =  childa
                    frontier.put(childa)
                    numFront+=1
                elif inFrontierWithHigherCost(childa,frontierHash): #check if its frontier with higher cost
                    frontierHash[childa] = childa
                    frontier.put(childa)


        i+=1

def  Manhattan(problem): # the Manhattan distance function
    node = child(problem.node,None, 1,0)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    frontierHash  = {}
    explore = []
    i = 0
    print("expanding state")
    print(node.Node)
    numFront = 1
    maxFront = 1
    while  True:

        if frontier.empty(): #check if the frontier is empty.
            return 'failure'
        node1 = frontier.get()
        if maxFront < numFront:  #keep track of the number of max in frontier
            maxFront = numFront
        if problem.Goal_Test(node1.Node) == True: #check if we found the goal state
            return node1,i,maxFront
        explore.append(node1)
        print("The best state to expand with a g(n) = ", node1.Cost, " and h(n) =", ManhattanDistance(node1.Node)) ## the steps that we expanded
        print(node1.Node)
        for eachAction in problem.Actions(node1.Node): #expand each note
                childnode = copy.deepcopy(eachAction)
                #created a new note for the expande version of the note
                childa = copy.deepcopy(child(childnode,node1,node1.depth+ ManhattanDistance(eachAction),node1.depth+1))
                if notFrontierOrExplore(childa,frontierHash,explore): #check if its in frontier or explore
                    frontierHash[childa] =  childa
                    frontier.put(childa)
                    numFront+=1
                elif inFrontierWithHigherCost(childa,frontierHash): # checking if its in frontier with higher cost
                    frontierHash[childa] = childa
                    frontier.put(childa)
        i+=1


def printaa(w): # prints the final menu
    if type(w) is str:
        print(w)
    else:
        wow = w[0]
        s = []
        print("Goal!!!") #it prints the menu
        print("to solve the problem the search algorithm expanded a total of",w[1], "nodes.")
        print("the maximum number of nodes in the queue at any one time was ", w[2])
        print("the depth of the goal node was ",w[0].depth )





if __name__ == "__main__":

    goal = np.matrix([[1,2,3], [4,5,6], [7,8,0]])
    print("Welcome to Marco Mercado's 8-puzzle solver. ")  ## it prints the top of the menu
    ValInput = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle\n" )
    if ValInput ==  1:
        m = np.matrix([[0,3,5], [8,4,7], [1,6,2]])
        p = problem(m,None,0,goal)


        print("Enter your choice of algorithm")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic.") #input on which algorithm to get.
        algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))
        if algorithmType == 1:
            wow = Unifor_Cost_Search(p) # calls the uniform algorithm
            printaa(wow)
        if algorithmType == 2:
            wow = misplaceTiles(p) #calls the misplaceTiles

            printaa(wow)
        if algorithmType == 3: #calls the Manhattan
            wow = Manhattan(p)
            printaa(wow)



    elif ValInput == 2:
        print("Enter your  puzzle, use a zero to represent the blank") #input on which puzzle to use
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
        print("2. A* with the Misplaced Tile heuristic.") # choose the algorithm
        algorithmType = int(raw_input("3. A* with the Manhattan distance heuristic.\n"))
        if algorithmType == 1:
            wow = Unifor_Cost_Search(p) # calls the uniform algorithm
            printaa(wow)
        if algorithmType == 2:
            wow = misplaceTiles(p)  #calls the misplaceTiles
            printaa(wow)
        if algorithmType == 3: #calls the Manhattan
            wow = Manhattan(p)
            printaa(wow)
