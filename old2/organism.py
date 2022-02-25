from genome import *

class Organism:
	"""
	Class representing individual organisms of a species

	Attributes:
		chance: Chance of genotype appearing within siblings
		species: Species
		sex: Sex
		parents: Mother and father
	"""
	def __init__(self, species, sex = None, parents = (None, None), genome = None):
		self.chance = 1
		self.species = species
		if genome is None: 
			self.genome = Genome(self.species)
			self.species.sex_variants(self.genome, sex)
		else: self.genome = genome
		self.parents = parents
		self.id = None

	def sex(self):
		"""Returns the sex of the organism"""
		return self.species.sex_variants(self.genome, get_sex = True)

	def add_genes(self, n, gene):
		"""
		Adds genes to the end of sibling chromosomes.
		
		Args:
			n: Chromosome number
			gene: List of genes indexed by the sibling they correspond with
		"""
		self.genome.add_genes(n, gene)

	def cross_with(self, other):
		"""
		Creates a list of organisms that are the genetic progeny of two mates.

		Args:
			other: The organism 'self' is mating with.
		
		Returns:
			A list of organisms.
		"""
		organisms = []
		for i in range(2**(self.species.xnum - 1)):
			for my_haploid in self.genome.make_haploids(i):
				for j in range(2**(other.species.xnum - 1)):
					for their_haploid in other.genome.make_haploids(j):
						organisms.append(Organism(self.species, parents = (self, other), genome = Genome.make_from_haploids(my_haploid, their_haploid)))
		return organisms

	def is_siblings(self, other):
		for my_parent in self.parents:
			is_same = False
			for their_parent in other.parents:
				is_same = is_same or my_parent is their_parent
			if not is_same: return False
		return True

	def __eq__(self, other: object):
		return (self.species == other.species 
				and self.is_siblings(other)
				and self.genome == other.genome)
	
	def __hash__(self) -> int:
		if self.id is None:
			self.id = hash((self.species, frozenset(self.parents), self.genome))
		# print(None)
		return self.id
