from utils import *

class Organism:
	def __init__(self, genome, parents = OrderedSet(None, None)) -> None:
		self.genome = genome
		self.parents = parents

	def sex(self):
		# raise NotImplementedError("Please Implement this method")
		if None in self.genome[0]:
			return "Male"
		else:
			return "Hermaphrodite"

# class C_elegans(Organism):
	# def sex(self):
		# if None in self.genome[0]:
			# return "Male"
		# else:
			# return "Hermaphrodite"