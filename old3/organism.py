from species import C_elegans


class Organism:
	def __init__(self, genome, species = C_elegans(), parents = set()):
		self.genome = genome
		self.parents = parents
		self.species = species

	def sex(self):
		return self.species.sex_determination(self)
