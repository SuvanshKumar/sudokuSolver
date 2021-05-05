# Sudoku Solver

Implementation of Depth-First Tree Search algorithm for solving a sudoku puzzle 

To run the code, just clone the repository, and run python in the base of the repository:

```bash
$ git clone https://github.com/SuvanshKumar/sudokuSolver.git
$ cd sudokuSolver
$ python
```

Then import the sudoku solver, input your puzzle, and it would solve the puzzle (or import the library into your 
own code)

```python
import sudoku

my_puzzle = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
	[8, 4, 2, 9, 7, 3, 5, 6, 1],
	[9, 6, 1, 2, 8, 5, 3, 7, 4],
	[2, 8, 6, 3, 4, 9, 1, 5, 7],
	[4, 1, 3, 8, 5, 7, 9, 2, 6],
	[5, 7, 9, 1, 2, 6, 4, 3, 8],
	[1, 5, 7, 4, 9, 2, 6, 8, 3],
	[6, 9, 4, 7, 3, 8, 2, 1, 5],
	[3, 2, 8, 5, 6, 1, 7, 4, 9]]

sdk = sudoku.Sudoku(my_puzzle)

sdk.solve() # This API will be changed/deprecated later, so don't rely on this for production code
```

