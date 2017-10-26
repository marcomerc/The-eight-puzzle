import sys
import numpy







if __name__ == "__main__":
    problem
    print("Welcome to Bertie Woosters 8-puzzle solver. ")
    ValInput = int(input("Type “1” to use a default puzzle, or “2” to enter your own puzzle." ))
    if ValInput ==  1:
        problem = numpy.matrix('1,2,3;4,5,6;7.8,0')
    elif ValInput == 2:
        print("Enter your puzzle, use a zero to represent the blank")
        rowOne = input("Enter the first row, use space or tabs between numbers" )
        rowTwo = input("Enter the second row, use space or tabs between numbers")
        rowTree = input("Enter the third row, use space or tabs between numbers")
        problme = (rowOne,rowTwo, rowTree)
