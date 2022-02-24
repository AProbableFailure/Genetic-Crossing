from enum import Enum

class Sex(Enum):
	Hermaphrodite = 1
	Male = 2
	Female = 3

def c_elegans_sex_variants(genome, sex = None, get_sex = False):
	if get_sex:
		if None in genome[0]:
			return Sex.Male
		else:
			return Sex.Hermaphrodite
	else:
		if sex == Sex.Male: genome[0][-1] = None

class Species:
	"""
	A class to store species configurations

	Attributes:
		name: Species's name
		ploidy: Number of chromosomes in a set (monoploid = 1, diploid = 2, triploid = 3, etc.).
		xnum: Number of unique chromosomes
		sex_variants: Mapping function used to alter the genomes of sex variants
	"""

	def __init__(self, name, ploidy, xnum, sex_variants):
		self.name = name
		self.ploidy = ploidy
		self.xnum = xnum
		self.sex_variants = sex_variants
