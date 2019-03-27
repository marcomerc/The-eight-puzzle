# Project Title

The is an 8 tile puzzle solver. It allows the user to enter an 8 tile and it will solve it.

## Getting Started

To clone
Git clone https://github.com/marcomerc/The-eight-puzzle.git

### Prerequisites

The libraries used are the following make sure to install the libraries.
You have to run it with Python 2.7
```
import numpy as np
import copy
import timeit
import Queue as Q
```



### Runing and  tests


```
python puz.py
```
A menu will pop up

```
Welcome to Marco Mercado's 8-puzzle solver.
Type "1" to use a default puzzle, or "2" to enter your own puzzle
```
Enter 1 to run the test.

```
Enter your choice of algorithm
1. Uniform Cost Search
2. A* with the Misplaced Tile heuristic.
3. A* with the Manhattan distance heuristic.
```
Enter the type of Heuristic you want to use. 
Mnahattan Distribution is the most efficient searching algorithm, while Uniform Cost Search is the least effective algorithm.



## Authors

* **Marco Mercado** - *Initial work* - [PurpleBooth](https://github.com/marcomerc)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This is A* implementation
* Dr. Keogh from UC Riverside
