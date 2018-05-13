# import pdb

class Sudoku:
	'''
SIZE	: number of blocks in one row, number of rows, cols and boxes (should be a perfect square, but not sure)

puzzle 	: SIZE X SIZE matrix of numbers (1 to SIZE for non-empty blocks, 0 for empty blocks)

map 	: defines for a given block (81 blocks in 9 by 9 sudoku), which all numbers are possible
			each map[i][j] is a set. eg. map[2][5]={2,3,9} means that in the block in 3rd row and 6th column (puzzle[2][5]), the numbers 2,3 and 9 can come
			if the block [i][j] in puzzle is filled (solved), then in map it is marked as {0}, eg. if puzzle[3][1]=5, then block[3][1]={0}

rcb_map : defines for a given row, col or box, a given number can appear at what all places
			rcb_map['row'] is a list of SIZE dictionaries, each of which is of the form {1:{0,2,3}, 2:{4}, 3:{2,3,8}...}
			it shows that for a given row, 1 can appear at indices 0,2,3 and 2 is at 4 (solved), etc.
'''
	def __init__(self,puzzle=[],SIZE=9):
		self.puzzle=puzzle
		self.SIZE=SIZE
		self.map=[]
		self.rcb_map={'row':[], 'column':[], 'box':[]}
		self.update_map()
		self.update_rcb_map()

	def display_puzzle(self):
		leng = len(self.puzzle)
		for i in range(leng):
			leng2 = len(self.puzzle[i])
			for j in range(leng2):
				print(self.puzzle[i][j], end=' ')
			print(end='\n')
		return

	def is_valid_row(self,row=0):
		for num in range(1,self.SIZE+1):
			thisOcc=0
			for i in range(self.SIZE):
				if self.puzzle[row][i]==num:
					thisOcc+=1;
				elif self.puzzle[row][i]<1 or self.puzzle[row][i]>self.SIZE:
					return False
			if thisOcc>1:
				return False
		return True

	def is_valid_col(self,col=0):
		for num in range(1,self.SIZE+1):
			thisOcc=0
			for i in range(self.SIZE):
				if self.puzzle[i][col]==num:
					thisOcc+=1;
				elif self.puzzle[i][col]<1 or self.puzzle[i][col]>self.SIZE:
					return False
			if thisOcc>1:
				return False
		return True

	def is_valid_box(self,box=0):
		#This function is valid only for SIZE=9
		for num in range(1, self.SIZE+1):
			thisOcc=0
			for i in range((box//3)*3, (box//3)*3+3):
				for j in range((box%3)*3, (box%3)*3+3):
					if self.puzzle[i][j]==num:
						thisOcc+=1
					elif self.puzzle[i][j]<1 or self.puzzle[i][j]>self.SIZE:
						return False
			if thisOcc>1:
				return False
		return True

	def is_valid_puzzle(self):
		#checking rows
		for i in range(self.SIZE):
			if(not self.is_valid_row(i)):
				return False
		#checking columns
		for i in range(self.SIZE):
			if(not self.is_valid_col(i)):
				return False
		#checking boxes
		for i in range(self.SIZE):
			if(not self.is_valid_box(i)):
				return False
		return True

	def get_row(self, n):
		return self.puzzle[n]

	def get_col(self, n):
		colList=[]
		for row in self.puzzle:
			colList.append(row[n])
		return colList

	def get_box(self, box=None, row=None, col=None):
		bx=[]
		if box==None:
			box=(row//3)*3+col//3
		for i in range((box//3)*3, (box//3)*3+3):
			for j in range((box%3)*3, (box%3)*3+3):
				bx.append(self.puzzle[i][j])
		return bx

	def update_map(self, row=None, col=None, num=None):
		if (row==None or col==None or num==None):
			self.map=[]
			for i in range(self.SIZE):
				row_list=[]
				for j in range(self.SIZE):
					this_map={1,2,3,4,5,6,7,8,9}
					if self.puzzle[i][j]!=0:
						this_map={0}
					else:
						for k in range(self.SIZE):
							if self.puzzle[k][j] in this_map:
								this_map.remove(self.puzzle[k][j])
						for k in range(self.SIZE):
							if self.puzzle[i][k] in this_map:
								this_map.remove(self.puzzle[i][k])
						box = (i//3)*3+j//3
						for k1 in range((box//3)*3, (box//3)*3+3):
							for k2 in range((box%3)*3, (box%3)*3+3):
								if self.puzzle[k1][k2] in this_map:
									this_map.remove(self.puzzle[k1][k2])
					row_list.append(this_map)
				self.map.append(row_list)
		else:
			self.map[row][col]={0}
			for i in range(self.SIZE):
				if num in self.map[i][col]:
					self.map[i][col].remove(num)
			for j in range(self.SIZE):
				if num in self.map[row][j]:
					self.map[row][j].remove(num)
			box = (row//3)*3+col//3
			for k1 in range((box//3)*3, (box//3)*3+3):
				for k2 in range((box%3)*3, (box%3)*3+3):
					if num in self.map[k1][k2]:
						self.map[k1][k2].remove(num)

	def update_rcb_map(self, row=None, column=None, number=None):
		# continue this function, then the solve one
		if (row==None or column==None or number==None):
			for rowNumber in range(self.SIZE):
				possibilities={}
				for num in range(1,self.SIZE+1,1):
					possibilities[num]=set()
					for position in range(self.SIZE):
						possibilities[num].add(position)
						''' now the possibilities dictionary is:
							{ 1:{0,1,2,3,4,5,6,7,8},
								2:{0,1,2,3,4,5,6,7,8},
								3:{0,1,2,3,4,5,6,7,8},
								4:{0,1,2,3,4,5,6,7,8},
								5:{0,1,2,3,4,5,6,7,8},
								6:{0,1,2,3,4,5,6,7,8},
								7:{0,1,2,3,4,5,6,7,8},
								8:{0,1,2,3,4,5,6,7,8},
								9:{0,1,2,3,4,5,6,7,8}}
						'''
				for j in range(self.SIZE):
					if self.puzzle[rowNumber][j]!=0:
						possibilities[self.puzzle[rowNumber][j]]={j}
						for num in range(1,self.SIZE+1,1):
							if num!=self.puzzle[rowNumber][j] and j in possibilities[num]:
								possibilities[num].remove(j)
					col_this = self.get_col(j)
					box_this = self.get_box(row=rowNumber, col=j)
					for num in range(1,self.SIZE+1,1):
						if num in col_this or num in box_this:
							if j in possibilities[num] and len(possibilities[num])!=1:
								possibilities[num].remove(j)
				self.rcb_map['row'].append(possibilities)
			for colNumber in range(self.SIZE):
				possibilities={}
				for num in range(1,self.SIZE+1,1):
					possibilities[num]=set()
					for position in range(self.SIZE):
						possibilities[num].add(position)
						''' now the possibilities dictionary is:
							{ 1:{0,1,2,3,4,5,6,7,8},
								2:{0,1,2,3,4,5,6,7,8},
								3:{0,1,2,3,4,5,6,7,8},
								4:{0,1,2,3,4,5,6,7,8},
								5:{0,1,2,3,4,5,6,7,8},
								6:{0,1,2,3,4,5,6,7,8},
								7:{0,1,2,3,4,5,6,7,8},
								8:{0,1,2,3,4,5,6,7,8},
								9:{0,1,2,3,4,5,6,7,8}}
						'''
				for i in range(self.SIZE):
					if self.puzzle[i][colNumber]!=0:
						possibilities[self.puzzle[i][colNumber]]={i}
						for num in range(1,self.SIZE+1,1):
							if num!=self.puzzle[i][colNumber] and i in possibilities[num]:
								possibilities[num].remove(i)
					row_this = self.get_row(i)
					box_this = self.get_box(row=i, col=colNumber)
					for num in range(1,self.SIZE+1,1):
						if num in row_this or num in box_this:
							if i in possibilities[num] and len(possibilities[num])!=1:
								possibilities[num].remove(i)
				self.rcb_map['column'].append(possibilities)
			for boxNumber in range(self.SIZE):
				possibilities={}
				for num in range(1,self.SIZE+1,1):
					possibilities[num]=set()
					for position in range(self.SIZE):
						possibilities[num].add(position)
						''' now the possibilities dictionary is:
							{ 1:{0,1,2,3,4,5,6,7,8},
								2:{0,1,2,3,4,5,6,7,8},
								3:{0,1,2,3,4,5,6,7,8},
								4:{0,1,2,3,4,5,6,7,8},
								5:{0,1,2,3,4,5,6,7,8},
								6:{0,1,2,3,4,5,6,7,8},
								7:{0,1,2,3,4,5,6,7,8},
								8:{0,1,2,3,4,5,6,7,8},
								9:{0,1,2,3,4,5,6,7,8}}
						'''
				for i in range((boxNumber//3)*3, (boxNumber//3)*3+3):
					for j in range((boxNumber%3)*3, (boxNumber%3)*3+3):
						pos = (i%3)*3 + j%3;
						if self.puzzle[i][j]!=0:
							possibilities[self.puzzle[i][j]] = {pos}
							for num in range(1,self.SIZE+1,1):
								if num!=self.puzzle[i][j] and pos in possibilities[num]:
									possibilities[num].remove(pos)
						row_this = self.get_row(i)
						col_this = self.get_col(j)
						for num in range(1,self.SIZE+1,1):
							if num in row_this or num in col_this:
								if pos in possibilities[num] and len(possibilities[num])!=1:
									possibilities[num].remove(pos)
				self.rcb_map['box'].append(possibilities)
		else:
			rowNumber=row
			rowPos=column
			self.rcb_map['row'][rowNumber][number]={rowPos}
			for num in range(1,self.SIZE+1,1):
				if num!=number and rowPos in self.rcb_map['row'][rowNumber][num]:
					self.rcb_map['row'][rowNumber][num].remove(rowPos)
			colNumber=column
			colPos=row
			self.rcb_map['column'][colNumber][number]={colPos}
			for num in range(1,self.SIZE+1,1):
				if num!=number and colPos in self.rcb_map['column'][colNumber][num]:
					self.rcb_map['column'][colNumber][num].remove(colPos)
			boxNumber = (row//3)*3+column//3
			boxPos = (row%3)*3 + column%3
			self.rcb_map['box'][boxNumber][number]={boxPos}
			for num in range(1,self.SIZE+1,1):
				if num!=number and boxPos in self.rcb_map['box'][boxNumber][num]:
					self.rcb_map['box'][boxNumber][num].remove(boxPos)
			

	def fill(self, row, col, num):
		self.puzzle[row][col]=num
		self.update_map(row, col, num)
		self.update_rcb_map(row, col, num)

	def complete_one_remaining(self):
		'''
		this function checks if only one block is empty in a row, col or a box, then fills it
		also, whenever any number is filled, it should repeat (loop) itself till that iteration where no new number is filled
		This function may be called many times by the solve_puzzle method
		'''
		expected_sum = (self.SIZE*(self.SIZE+1))//2
		# 1+2+3+...+n = n(n+1)/2

		# checking in rows
		for row in range(self.SIZE):
			count_zeroes=0
			for j in range(self.SIZE):
				if self.puzzle[row][j]==0:
					count_zeroes+=1
				if count_zeroes>1:
					break
			if count_zeroes==1:
				sum=0
				index=-1
				for j in range(self.SIZE):
					sum+=self.puzzle[row][j]
					if self.puzzle[row][j]==0:
						index=j
				self.fill(row, index, (expected_sum-sum))
				# self.puzzle[row][index]=(expected_sum-sum)
				# self.update_map(row,index,(expected_sum-sum))
				return True
				# because if all numbers present, sum should be expected_sum. So, expected_sum-sum gives the missing number
		# checking in columns
		for col in range(self.SIZE):
			count_zeroes=0
			for j in range(self.SIZE):
				if self.puzzle[j][col]==0:
					count_zeroes+=1
				if count_zeroes>1:
					break
			if count_zeroes==1:
				sum=0
				index=-1
				for j in range(self.SIZE):
					sum+=self.puzzle[j][col]
					if self.puzzle[j][col]==0:
						index=j
				self.fill(index, col, (expected_sum-sum))
				# self.puzzle[index][col]=(expected_sum-sum)
				# self.update_map(index,col,(expected_sum-sum))
				return True
				# because if all numbers present, sum should be expected_sum. So, expected_sum-sum gives the missing number
		# checking in boxes
		for box in range(self.SIZE):
			count_zeroes=0
			for i in range((box//3)*3, (box//3)*3+3):
				for j in range((box%3)*3, (box%3)*3+3):
					if self.puzzle[i][j]==0:
						count_zeroes+=1
					if count_zeroes>1:
						break
			if count_zeroes==1:
				sum=0
				index1=-1
				index2=-1
				for k1 in range((box//3)*3, (box//3)*3+3):
					for k2 in range((box%3)*3, (box%3)*3+3):
						sum+=self.puzzle[k1][k2]
						if self.puzzle[k1][k2]==0:
							index1=k1
							index2=k2
				self.fill(index1, index2, (expected_sum-sum))
				# self.puzzle[index1][index2]=(expected_sum-sum)
				# self.update_map(index1,index2,(expected_sum-sum))
				return True
				# because if all numbers present, sum should be expected_sum. So, expected_sum-sum gives the missing number
		return False

	def check_with_map(self):
		''' checks the map, if a given block can have only one number, fill it and update the map here itself
		also, return True in that case'''
		for i in range(self.SIZE):
			for j in range(self.SIZE):
				if self.map[i][j]!={0} and len(self.map[i][j])==1:					
					for num in self.map[i][j]:
						break
					# above is a dirty way to extract element from a set
					self.fill(i, j, num)
					# self.puzzle[i][j] = num
					# self.update_map(i,j,num)
					return True
		return False

	def check_with_rcb_map(self):
		''' checks if a number can come at only one place in a row, column, or a box, and then fills the number
			then updates map and rcb_map through fill method only
			returns True if it finds a match (ie. only one possible location for a number in a row, column or box)
		'''
		for rowNumber in range(self.SIZE):
			for num in range(1,self.SIZE+1,1):
				if len(self.rcb_map['row'][rowNumber][num])==1:
					rowPos=0
					for j in self.rcb_map['row'][rowNumber][num]:
						rowPos=j
						break
					# quick and dirty way to extract element from a set that has a single element
					# also works for set with multiple elements (alternative to pop, which also deletes the element)
					# unlike pop, this method does not delete the element from the set
					if self.puzzle[rowNumber][rowPos]==0:
						self.fill(rowNumber, rowPos, num)
						return True
		for colNumber in range(self.SIZE):
			for num in range(1,self.SIZE+1,1):
				if len(self.rcb_map['column'][colNumber][num])==1:
					colPos=0
					for i in self.rcb_map['column'][colNumber][num]:
						colPos=i
						break
					# quick and dirty solution. Reason and description mentioned above
					if self.puzzle[colPos][colNumber]==0:
						self.fill(colPos, colNumber, num)
						return True
		for boxNumber in range(self.SIZE):
			for num in range(1,self.SIZE+1,1):
				if len(self.rcb_map['box'][boxNumber][num])==1:
					boxPos=0
					for i in self.rcb_map['box'][boxNumber][num]:
						boxPos=i
						break
					# quick and dirty solution. Reason and description mentioned above
					# save these logics as small functions somewhere later
					i = (boxNumber//3)*3+boxPos//3
					j = (boxNumber%3)*3+boxPos%3
					if self.puzzle[i][j]==0:
						self.fill(i, j, num)
						return True
		return False


	def solve(self):
		# initialize the map -- no need, since this is done in the constructor (init method)
		# self.update_map()
		# now, filling the numbers if only one number is missing in a row, column or box, and repeating till it cannot be done
		# pdb.set_trace()
		filled_one = self.complete_one_remaining()
		while (filled_one):
			filled_one = self.complete_one_remaining()
		#continue this function and think for what to do later		
		checked_with_map = self.check_with_map()
		while (checked_with_map):
			filled_one = self.complete_one_remaining()
			while (filled_one):
				filled_one = self.complete_one_remaining()
			checked_with_map = self.check_with_map()
		checked_with_rcb_map = self.check_with_rcb_map()
		while (checked_with_rcb_map):
			checked_with_map = self.check_with_map()
			while (checked_with_map):
				filled_one = self.complete_one_remaining()
				while (filled_one):
					filled_one = self.complete_one_remaining()
			checked_with_rcb_map = self.check_with_rcb_map()
		return

def main():
	# puzzle = input_puzzle(puzzle)
	# cannot be made function? (because python uses pass by value)
	SIZE=9
	puzzle1=[]
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
		puzzle1.append(a)

	sudoku = Sudoku(puzzle1,SIZE)

	print("The puzzle is")
	sudoku.display_puzzle()
	# print('\n') # \n\n for two new lines
	
	# sudoku.solve()
	# if (not is_valid_puzzle(puzzle)):
	# 	printf("Wrong puzzle")
	# 	exit()
	# print("The solved puzzle is")
	# sudoku.display_puzzle()

	# only during development phase
	# assert sudoku.is_valid_puzzle() == True

	# puzzle_Backup = puzzle

	# puzzle = solve_puzzle(puzzle)
	#the above call should solve the puzzle and return the puzzle object

if __name__ == '__main__':
	main()