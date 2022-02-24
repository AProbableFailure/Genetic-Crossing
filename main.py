from species import *
from organism import *

def main():
	print("Hello World!")

	c_elegans = Species(name = "C. elegans", 
						ploidy = 2, 
						xnum = 3, 
						sex_variants = c_elegans_sex_variants)

	w1 = Organism(c_elegans, Sex.Hermaphrodite)
	w1.add_genes(1, [0, 1])
	w2 = Organism(c_elegans, Sex.Hermaphrodite)
	w2.add_genes(1, [1, 0])
	w2.add_genes(0, [2, 3])
	print(w1 == w2)
	print(hash(w1))
	print(hash(w2))

	print(w1.genome.chromosomes)
	print(w1.sex())
	
	progeny = w1.cross_with(w2)
	print(len(progeny))

	s = set(progeny)

	for o in s:
		print(o.genome.chromosomes)

if __name__ == "__main__":
	main()