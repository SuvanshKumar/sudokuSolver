

class GameTree:
	'''This is the abstract Tree representation of a game. A node in the tree represents a state in the game. Contains
	a reference to the root of the tree, which is the initial state of the game. It is not meant to be initialized,
	and a subclass should be made to create on instance of the GameTree'''

	def __init__(self, node):
		raise NotImplementedError


	def get_children(self, node):
		raise NotImplementedError


class SudokuTree(GameTree):

	def __init__(self, node):
		raise NotImplementedError


class Node:
	'''This is the node, a point in the GameTree. Each node contains a pointer to the parent node.
	'''

	def __init__(self, node):
		raise NotImplementedError