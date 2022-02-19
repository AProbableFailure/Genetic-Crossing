class Worm:
    def __init__(self, genome = None, male = False, parents = (None, None), count = 1, n_number = 6) -> None:
        self.n_number, self.genome = (n_number, [[[], []] for i in range(n_number)]) if genome is None else (len(genome), genome)
        if male: self.genome[0][-1] = None
        self.parents = parents
        self.count = count

    def add_gene(self, chromosome, gene):
        for i in range(len(gene)): self.genome[chromosome][i].append(gene[i])

    def is_male(self): return None in self.genome[0]
    def is_hermaphrodite(self): return not self.is_male()

    def generation(self):
        parents = [p for p in self.parents if p]
        if not parents: return 0
        else: return (sum(map(lambda w: w.generation(), parents))/len(parents)) + 1
        # if None in self.parents:
        #     if self.parents == (None, None): return 0
        # else: return max(self.parents[0].generation, self.parents[1].generation()) + 1

    def cross(mom, dad):
        progeny = []
        for i in range(4**mom.n_number):
            genome = []
            for c in range(mom.n_number):
                pick_genes = lambda p, s: p.genome[c][0] if i & (1 << 2*c+s) else p.genome[c][1]
                genome.append([pick_genes(mom, 0), pick_genes(dad, 1)])
            add_worm(Worm(genome=genome, parents = (mom, dad), count = mom.count*dad.count), progeny)
        return progeny

    def tuplized_genome(self):
        return tuple(tuple(None if j is None else tuple(j) for j in i) for i in self.genome)

    def __eq__(self, other: object) -> bool:
        # print(tuple(reversed(other.parents)))
        # if self.parents not in (other.parents, tuple(reversed(other.parents))): return False
        if set(self.parents) != set(other.parents): return False
        if self.n_number != other.n_number: return False        
        for c in range(self.n_number):
            genome_set = lambda w: set(None if i is None else tuple(i) for i in w.genome[c])
            if genome_set(self) != genome_set(other): return False
        return True

    def __hash__(self) -> int:
        return hash((self.parents, self.count, self.tuplized_genome()))

    def __str__(self) -> str:
        return "Generation: " + str(self.generation()) + "; Genome: " + str(self.genome) + "; Appears " + str(self.count) + " times"

def add_worm(worm, worms):
    if worm in worms:
        worms[worms.index(worm)].count += worm.count
    else:
        worms.append(worm)

def cross(virgins, f, parents = []):
    if f == 0:
        for worm in virgins:
            add_worm(worm, parents)
        return parents

    dads = virgins + parents
    moms = [x for x in virgins + parents if x.is_hermaphrodite()]
    # print(len(dads))
    # print(len(moms))
    progeny = []

    for dad in dads:
        for mom in moms:
            if dad in parents and mom in parents: continue
            # print("Mom: " + str(mom.genome))
            # print("Dad: " + str(dad.genome))
            progeny += mom.cross(dad)
            # print(progeny)
    
    return cross(progeny, f-1, virgins + parents)

def main():
    worm = Worm(n_number=1)
    # print(worm.genome)
    # worm.add_chromosomes(2, 2)
    worm.add_gene(0, [0, 1])
    worm2 = Worm(n_number = 1, male=True)
    # worm2.add_chromosomes(2, 2)
    worm2.add_gene(0, [1])
    # worm2.add_gene(0, [0, 1])
    print(worm.genome)
    print(worm2.genome)
    print(worm.is_male())
    print()
    # print(worm2.tuplized_genome())
    # progeny = worm.cross(worm)
    progeny = cross([worm], 2)
    print(len(progeny))
    for worm in progeny:
        print(worm)
        # if worm.generation() == 2: 
            # print(worm)
            # for parent in worm.parents:
                # print(parent)
            # print()
        # print(worm.count)
        pass
    
    # worm3 = Worm(n_number=1)
    # worm3.add_gene(0, [0, 1])
    # progeny3 = worm3.cross(worm3)
    # print(progeny3[0] in progeny)
    # for worm in progeny3:
    #     print(worm.genome)
    #     print(worm.count)

if __name__ == "__main__":
    main()