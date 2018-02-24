

### Functions ###

def display_puzzle(puzzle):
	leng = len(puzzle)
	for i in range(leng):
		for j in range(leng):
			print(puzzle[i][j], end=' ')
	print()
	return

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
		if(not ValidBox(puzzle, i)):
			return False
	return True
	
def is_valid_row(puzzle, i):
	for j in range(SIZE):
		thisOcc=0
		for k in range(1, SIZE+1):
			if puzzle[i][j]==k:
				thisOcc+=1
		if(thisOcc>1):
			return False
	return True

def is_valid_col(puzzle, i):
	for j in range(SIZE):
		thisOcc=0
		for k in range(1, SIZE+1):
			if puzzle[j][i]==k:
				thisOcc+=1
		if(thisOcc>1):
			return False
	return True

def is_valid_box(puzzle, i):
	#This function is valid only for SIZE=3
	for j in range( (i//3)*3 , (i//3)*3+3):
		for k in range( (i%3)*3 , (i%3)*3+3):
			for l in range(1, SIZE+1):
				thisOcc=0;
				if(puzzle[j][k]==l):
					thisOcc+=1
			if(thisOcc>1):
				return False
	return True;

SIZE = 9;
puzzle = []

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



