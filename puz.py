import sys
import numpy as np
import copy


class child():
    def __init__(self, n, cost):
          self.Node = n
          self.Cost = cost
          self.STATE = None



class problem():
    def __init__(self,initial_node, state, cost):
      self.node = initial_node
      self.C = 0
      self.initial_state = None

    def Goal_Test(self, node):
        print("test")

#
# def Unifor_Cost_Search(problem):
#     child = copy.deepcopy(problem)


if __name__ == "__main__":

    print("Welcome to Bertie Woosters 8-puzzle solver. ")
    ValInput = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle\n" )
    if ValInput ==  1:
        m = np.matrix([[2,1,3], [4,5,6], [7,8,0]])
        p = problem(m,None,0)

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
