class Worm:
    def __init__(self, genome = None, male = False, parents = (None, None), count = 1, n_number = 6) -> None:
        # self.n_number = n_number
        # self.genome = [[[], []] for i in range(self.n_number)] if genome is None else genome

        # if genome is None:
            # self.n_number = n_number
            # self.genome = [[[], []] for _ in range(self.n_number)]
        # else:
            # self.n_number = len(genome)
            # self.genome = genome
        self.n_number, self.genome = (n_number, [[[], []] for i in range(n_number)]) if genome is None else (len(genome), genome)
        # self.genome, self.n_number = (genome, len(genome)) or ([[[], []] for i in range(n_number)], n_number)

        # self.genome = genome or [[[], []] for i in range(self.n_number)]
        if male: self.genome[0][-1] = None
            # print(self.genome)
        self.parents = parents
        self.count = count

    # def add_gene(self, chromosome, maternal_gene, paternal_gene):
    # def add_chromosomes(self, amount, siblings):
        # for _ in range(amount): self.genome.append([[] for _ in range(siblings)])
    # def remove_chromosome(self, chromosome):
        # del self.genome[chromosome]
    def add_gene(self, chromosome, gene):
        for i in range(len(gene)): self.genome[chromosome][i].append(gene[i])

    # def n_number(self): return len(self.genome)
    # def is_male(self): return len(self.genome[0]) == 1
    def is_male(self): return None in self.genome[0]
    def is_hermaphrodite(self): return not self.is_male()

    def cross(mom, dad):
        progeny = []
        for i in range(4**mom.n_number):
            genome = []
            for c in range(mom.n_number):
                pick_genes = lambda p, s: p.genome[c][0] if i & (1 << 2*c+s) else p.genome[c][1]
                genome.append([pick_genes(mom, 0), pick_genes(dad, 1)])
            add_worm(Worm(genome=genome, parents = (mom, dad), count = mom.count*dad.count), progeny)
        return progeny

    def __eq__(self, other: object) -> bool:
        if self.n_number != other.n_number: return False        
        # if set(self.parents) != set(other.parents): return False
        if self.parents not in (other.parents, reversed(other.parents)): return False
        for c in range(self.n_number):
            # print(self.genome[c])
            genome_set = lambda w: set(None if i is None else tuple(i) for i in w.genome[c])
            # def genome_set(w):
                # print(type(w.genome[c]))
                # {None if i is None else tuple(i) \
                    # for i \
                    # in w.genome[c]}
            if genome_set(self) != genome_set(other): return False
        return True

def add_worm(worm, worms):
    if worm in worms:
        worms[worms.index(worm)].count += worm.count
    else:
        worms.append(worm)
# def cross_couple(mom, dad):
    # progeny = []
    # for _ in range()

def main():
    worm = Worm(n_number=1, male = True)
    # print(worm.genome)
    # worm.add_chromosomes(2, 2)
    worm.add_gene(0, [0])
    worm2 = Worm()
    # worm2.add_chromosomes(2, 2)
    worm2.add_gene(0, [1, 0])
    # worm2.add_gene(0, [0, 1])
    print(worm.genome)
    print(worm2.genome)
    print(worm.is_male())
    print()
    progeny = worm.cross(worm)
    print(len(progeny))
    for worm in progeny:
        print(worm.genome)
        print(worm.count)

if __name__ == "__main__":
    main()