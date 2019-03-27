# Project Title

The is an 8 tile puzzle solver. It allows the user to enter an 8 tile and it will solve it.

## Getting Started

To clone
Git clone https://github.com/marcomerc/The-eight-puzzle.git

### Prerequisites

Java 

If you want to use this on your data you have to edit line 341 to change the file number
the data is formated in columns with the first column being the class. the other columns the features.
### Runing and  tests


```
javac project.java
java project
```
A menu will pop up

```
Enter the type of feature selection algorithm to use
For Backward feature selection algorithm enter 1
For Forward  feature selection algorithm enter 2
For Marco's  featere selection algorithm enter 3
```
Enter an option to run the feautre algorithm that you want to use.

output should look like this, but may different base on the algorithm that you use.


```

Feature set { 46 37 21 25 12 13 6 30 36 23 4 17 39 18 47 50 16 33 10 29 44 22 35 14 45 38 32 19 8 31 43 28 15 3 48 1 7 24 11 40 5 20 41 2 49 34 26 27 42 } was best, accuracy is  0.69%
the features that give the best accuracy are 45 36  the accuracy is 0.97
```




## Authors

* **Marco Mercado** - *All work done by marco* - [MarcoMerc](https://github.com/marcomerc)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This is a feautre selection implementation
* Dr. Keogh from UC Riverside
