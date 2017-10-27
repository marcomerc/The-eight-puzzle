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
    def Goal_Test(node):
        if np.array_equal(node, self.goal):
            return True
        else:
            return False

    def Actions(self,node):
        matrixs = []
        row,col = node.shape
        for i in row:
            for i in col:
                if node.item(i,j) == 0:
                    loc = [i,j]
                    break
        if  loc[1] < col - 1:                    #checking if you can move to the right
            chidl1 = copy.deepcopy(node)
            temp = child1.item(loc[0],loc[1])
            temp2 = child1.item(loc[0],loc[1]+1)
            child1[loc[0],loc[1]] = temp2
            child1[loc[0],loc[1]+1] = temp
            martixs.append(child1)
        if  loc[1] > 0:                      #checking if you could move to the left
            chidl2 = copy.deepcopy(node)
            temp = child2.item(loc[0],loc[1])
            child2[loc[0],loc[1]] = child2.item(loc[0],loc[1]-1)
            child2[loc[0],loc[1]-1] = temp
            martixs.append(child1)
        if  loc[0] < row - 1:                #checking if you could move to the right
            chidl3 = copy.deepcopy(node)
            temp = child3.item(loc[0],loc[1])
            child3[loc[0],loc[1]] = child3.item(loc[0]+1,loc[1])
            child3[loc[0],loc[1]+1] = temp
            martixs.append(child3)
        if  loc[0] > 0:                 #checking if you could move to the right
            chidl1 = copy.deepcopy(node)
            temp = child1.item(loc[0],loc[1])
            child1[loc[0],loc[1]] = child1.item(loc[0],loc[1]-1)
            child1[loc[0],loc[1]-1] = temp
            martixs.append(child1)

        return martixs


def Unifor_Cost_Search(problem):
    node = child(problem.node,"problem", 0)
    frontier =  Q.PriorityQueue()
    frontier.put(node)
    explore = []
    while True:
        if frontier.empty():
            return 'failure'
        node = frontier.get()
        if problem.Goal_Test(node.Node):
            return node.Node
        for eachAction in problem.Actions(node.Node):
            childa = child(eachAction,"problem",node.Cost+1)

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
        # if algorithmType == 1:


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
