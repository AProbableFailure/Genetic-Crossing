from collections import Counter
from enum import Enum

class Sex(Enum):
	Hermaphrodite = 1
	Male = 2
	Female = 3

class Genome:
	def __init__(self, *chromosomes):
		self.chromosomes = tuple(c for c in chromosomes)

	def __getitem__(self, index):
		return self.chromosomes[index]

	# def chromosome_set(self):
	# 	# print(self.chromosomes)
	# 	return tuple(dict(zip(c.keys(), map(frozenset, c.values()))) for c in self.chromosomes)

	# def switch_siblings(self):
		
	# Doesn't work
	def __eq__(self, other: object):
		if len(self.chromosomes) != len(other.chromosomes): return False
		# return {key: set(value) for key, value in self.chromosomes.items()} == 
		#return (dict(zip(self.chromosomes.keys(), map(set, self.chromosomes.values()))) 
		#		== dict(zip(other.chromosomes.keys(), map(set, other.chromosomes.values()))))
		# return self.chromosome_set() == other.chromosome_set()
		for c in range(len(self.chromosomes)):
			print(self.chromosomes[c])
			for g in range(len(self.chromosomes[c])):
				print(self.chromosomes[c].values())
			

	def __hash__(self) -> int:
		# print(tuple(tuple(c.values()) for c in self.chromosomes))
		return hash(tuple(tuple(c.values()) for c in self.chromosomes))
		# print(self.chromosomes)


	# def __eq__(self, other: object):
		# if len(self.chromosomes) != len(other.chromosomes): return False
		# for c in range(len(self.chromosomes)):
			# if set(to_tuple(self.chromosomes[c])) != set(to_tuple(other.chromosomes[c])):
				# return False
		# return True

	# # HASH CONSIDERS ORDER, BUT IT SHOULDN'T
	# def __hash__(self):
		# lst = []
		# for c in self.chromosomes:
			# lst.append(frozenset(tuple(g) for g in c))
		# return hash(tuple(lst))
		# # print(self.chromosomes)
		# #for 
		# # return hash(frozenset(to_tuple(self.chromosomes)))

def chromosome(*loci):
	r = {}
	for l in loci:
		r = r | l
	return r

def locus(cM, *alleles):
	return {round(cM, 3): tuple(a for a in alleles)}
	# return {round(cM, 3): Counter(a for a in alleles)}
	# r = {}
	# for a in alleles:
		# r[a] = cM
	# return r
	# return {(a for a in alleles): cM}
