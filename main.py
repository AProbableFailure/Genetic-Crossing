from genetics import *
from organism import Organism
from utils import OrderedSet


def main():

	g = Genome(
		[
			[0.0, 3.0, 4.2, 7.1],
			[0, 1, 2, 3],
			None
			# [4, 5, 6, 7],
		],
		[
			[0.0, 2.1, 2.4],
			[0, 1, 0],
			[1, 0, 1]
		]
	)

	g1 = Genome(
		[
			[0, 1, 2],
			[0, 1, 2],
			[3, 4, 5]
		]
	)

	g2 = Genome(
		[
			[0, 1, 2],
			[3, 4, 5],
			None
			#[0, 1, 2]
		]
	)

	print(hash(g1))
	print(hash(g2))
	print(g1 == g2)
	print(g2.genome)
	print(hash(g1) == hash(g2))
	print()

	os1 = OrderedSet(0, 0, 1, 1)
	os2 = OrderedSet(0, 1, 1, 1)
	os3 = OrderedSet(0, 1, 0, 1)
	print(os1 == os2)
	print(os1 == os3)
	print(hash(os1))
	print(hash(os2))
	print(hash(os3))
	print(os1)

	o1 = Organism(g)
	o2 = Organism(g)
	print()
	print(o1 == o2)

	# g = Genome(
		# siblings(
			# loci(0.0, 3.0, 4.2, 7.1),
			# chromosome(0, 1, 2, 3),
			# chromosome(0, 1, 2, 3)
		# ),
		# siblings(
			# loci(0.0, 2.1, 2.4),
			# chromosome(0, 0, 0),
			# chromosome(0, 0, 0)
		# )
	# )


if __name__ == "__main__":
	main()