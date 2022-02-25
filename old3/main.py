from genetics import *
from organism import Organism

def main():
	print("Hello World!")
	# siblings = chromosome_siblings(
		# chromosome("cdc-42", "BioSensor"),
		# chromosome("+", "+")
	# )
	# print(siblings)

	g = Genome(
		chromosome(
			locus(0.0, "X", None)
		),
		chromosome(
			locus(0.0, "cdc-42", "+"),
			locus(1.0, "BioSensor", "+")
		)
	)
	o = Organism(g)
	
	print(o.genome == o.genome)

	print(hash(g))
	# print(None in list(o.genome[0].values())[0])
	print(o.sex())
	print(g.chromosomes)

if __name__ == "__main__":
	main()