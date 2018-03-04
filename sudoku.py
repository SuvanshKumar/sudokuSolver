
SIZE = 9

### Functions ###

def display_puzzle(puzzle):
	leng = len(puzzle)
	for i in range(leng):
		for j in range(leng):
			print(puzzle[i][j], end=' ')
		print(end='\n')
	return

# def is_valid_row(puzzle, row=0):
# 	for j in range(SIZE):
# 		thisOcc=0
# 		for k in range(1, SIZE+1):
# 			if puzzle[row][j]==k:
# 				thisOcc+=1
# 		if(thisOcc>1):
# 			return False
# 	return True

def is_valid_row(puzzle, row=0):
	for num in range(1,SIZE+1):
		thisOcc=0
		for i in range(SIZE):
			if puzzle[row][i]==num:
				thisOcc+=1;
		if thisOcc>1:
			return False
	return True

# def is_valid_col(puzzle, col=0):
# 	for j in range(SIZE):
# 		thisOcc=0
# 		for k in range(1, SIZE+1):
# 			if puzzle[j][col]==k:
# 				thisOcc+=1
# 		if(thisOcc>1):
# 			return False
# 	return True

def is_valid_col(puzzle, col=0):
	for num in range(1,SIZE+1):
		thisOcc=0
		for i in range(SIZE):
			if puzzle[i][col]==num:
				thisOcc+=1;
		if thisOcc>1:
			return False
	return True

# def is_valid_box(puzzle, i):
# 	#This function is valid only for SIZE=3
# 	for j in range( (i//3)*3 , (i//3)*3+3):
# 		for k in range( (i%3)*3 , (i%3)*3+3):
# 			for l in range(1, SIZE+1):
# 				thisOcc=0;
# 				if(puzzle[j][k]==l):
# 					thisOcc+=1
# 			if(thisOcc>1):
# 				return False
# 	return True;

def is_valid_box(puzzle, box=0):
	#This function is valid only for SIZE=3
	for num in range(1, SIZE+1):
		thisOcc=0
		for i in range((box//3)*3, (box//3)*3+3):
			for j in range((box%3)*3, (box%3)*3+3):
				if puzzle[i][j]==num:
					thisOcc+=1
		if thisOcc>1:
			return False
	return True

def is_valid_puzzle(puzzle):
	#checking rows
	for i in range(SIZE):
		if(not is_valid_row(puzzle, i)):
			return False
	#checking columns
	for i in range(SIZE):
		if(not is_valid_col(puzzle, i)):
			return False
	#checking boxes
	for i in range(SIZE):
		if(not is_valid_box(puzzle, i)):
			return False
	return True
	
def complete_one_remaining(puzzle):
	'''
	this function checks if only one block is empty in a row, col or a box, then fills it
	also, whenever any number is filled, it should repeat (loop) itself till that iteration where no new number is filled
	This function may be called many times by the solve_puzzle method
	'''


	return puzzle

def solve_puzzle(puzzle):
	puzzle = complete_one_remaining(puzzle)
	#continue this function and think for what to do later

	return puzzle

puzzle = []

# puzzle = input_puzzle(puzzle)
# cannot be made function? (because python uses pass by value)
for i in range(1,SIZE+1):
	print("\nEnter row %d\n" % i)
	b = input()
	b.strip()
	while(len(b)!=SIZE):
		print("Wrong... there must be 9 characters. Please try again\n")
		b = input()
		b.strip()
	a = []
	for j in range(SIZE):
		if(b[j]>='1' and b[j]<='9'):
			a.append(int(b[j]))
		else:
			a.append(0)
	puzzle.append(a);

leng = len(puzzle)

print("The puzzle is")
display_puzzle(puzzle)
print('\n') # \n\n for two new lines

if(not is_valid_puzzle(puzzle)):
	printf("Wrong puzzle")
	exit()

# only during development phase
assert is_valid_puzzle(puzzle) == True

puzzle_Backup = puzzle

puzzle = solve_puzzle(puzzle)
#the above call should solve the puzzle and return the puzzle object
