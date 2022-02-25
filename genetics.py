from utils import OrderedSet


class Genome:
	def __init__(self, *siblings) -> None:
		self.genome = tuple(make_siblings(*s) for s in siblings)

	def __eq__(self, other: object) -> bool:
		return self.genome == other.genome

	def __hash__(self) -> int:
		return hash(self.genome)

def make_siblings(loci, *chromosomes):
	return OrderedSet(*[{loci[i]: c[i] for i in range(len(loci))} if c is not None else None for c in chromosomes])