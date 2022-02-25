# class SexDetermination(Enum):
from utils import to_tuple


class Genome:
	"""
	A class to manage and operate on an organism's chromosomes.

	Attributes:
		chromosomes: Chromosomes
	"""

	def __init__(self, species = None):
		#self.organism = organism
		# TODO: turn chromosomes into list of dictionaries for locus cM
		self.chromosomes = [] if species is None else [[[] for _ in range(species.ploidy)] for _ in range(species.xnum)]

	def __getitem__(self, index):
		return self.chromosomes[index]

	def __setitem__(self, index, value):
		self.chromosomes[index] = value

	# TODO: incorporate ploidy
	def make_haploids(self, seed):
		haploids = [[], []]
		for c in range(len(self.chromosomes)):
			haploids[0].append(self.chromosomes[c][0] if seed & (1 << c) else self.chromosomes[c][1])
			haploids[1].append(self.chromosomes[c][1] if seed & (1 << c) else self.chromosomes[c][0])
		return haploids

	def add_genes(self, n, genes):
		for i in range(len(genes)): self.chromosomes[n][i].append(genes[i])

	@staticmethod
	def make_from_haploids(h1, h2):
		genome = Genome()
		for c in range(len(h1)):
			genome.chromosomes.append([h1[c], h2[c]])
		return genome

	def __eq__(self, other: object):
		if len(self.chromosomes) != len(other.chromosomes): return False
		for c in range(len(self.chromosomes)):
			if set(to_tuple(self.chromosomes[c])) != set(to_tuple(other.chromosomes[c])):
				return False
		return True

	# HASH CONSIDERS ORDER, BUT IT SHOULDN'T
	def __hash__(self):
		lst = []
		for c in self.chromosomes:
			lst.append(frozenset(tuple(g) for g in c))
		return hash(tuple(lst))
		# return hash(tuple((frozenset(tuple(g) for g in c)) for c in self.chromosomes))
		# This works I think ^
		# print(self.chromosomes)
		#for 
		# return hash(frozenset(to_tuple(self.chromosomes)))