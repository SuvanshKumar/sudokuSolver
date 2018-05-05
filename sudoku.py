# import pdb

class Sudoku:
	'''
SIZE	: number of blocks in one row, number of rows, cols and boxes (should be a perfect square, but not sure)
puzzle 	: SIZE X SIZE matrix of numbers (1 to SIZE for non-empty blocks, 0 for empty blocks)
map 	: defines for a given block (81 blocks in 9 by 9 sudoku), how many numbers are possible'''
	def __init__(self,puzzle=[],SIZE=9):
		self.puzzle=puzzle
		self.SIZE=SIZE
		self.map=[]
		self.update_map()

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
			if thisOcc>1:
				return False
		return True

	def is_valid_col(self,col=0):
		for num in range(1,self.SIZE+1):
			thisOcc=0
			for i in range(self.SIZE):
				if self.puzzle[i][col]==num:
					thisOcc+=1;
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

	def update_map(self, row=-1, col=-1, num=-1):
		if (row==-1 or col==-1 or num==-1):
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
			box = (i//3)*3+j//3
			for k1 in range((box//3)*3, (box//3)*3+3):
				for k2 in range((box%3)*3, (box%3)*3+3):
					if num in self.map[k1][k2]:
						self.map[k1][k2].remove(num)


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
				self.puzzle[row][index]=(expected_sum-sum)
				self.update_map(row,index,(expected_sum-sum))
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
				self.puzzle[index][col]=(expected_sum-sum)
				self.update_map(index,col,(expected_sum-sum))
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
				self.puzzle[index1][index2]=(expected_sum-sum)
				self.update_map(index1,index2,(expected_sum-sum))
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
					self.puzzle[i][j] = num
					self.update_map(i,j,num)
					return True
		return False


	def solve(self):
		# filling the numbers if only one number is missing in a row, column or box, and repeating till it cannot be done
		# pdb.set_trace()
		filled_one = self.complete_one_remaining()
		while (filled_one):
			filled_one = self.complete_one_remaining()
		#continue this function and think for what to do later
		self.update_map()
		checked_with_map = self.check_with_map()
		while (checked_with_map):
			filled_one = self.complete_one_remaining()
			while (filled_one):
				filled_one = self.complete_one_remaining()
			checked_with_map = self.check_with_map()

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
	print('\n') # \n\n for two new lines
	sudoku.solve()
	# if (not is_valid_puzzle(puzzle)):
	# 	printf("Wrong puzzle")
	# 	exit()
	print("The solved puzzle is")
	sudoku.display_puzzle()

	# only during development phase
	# assert sudoku.is_valid_puzzle() == True

	# puzzle_Backup = puzzle

	# puzzle = solve_puzzle(puzzle)
	#the above call should solve the puzzle and return the puzzle object

if __name__ == '__main__':
	main()