from collections import Counter

from genetics import *

# USE ENUMERATE INSTEAD OF RANGE

class Worm:
    def __init__(self, n_number = 1, male = False, parents = (None, None), genome = None, count = 1) -> None:
        if genome is None:
            self.n_number = n_number
            self.genome = tuple(ChromosomeSiblings() for _ in range(n_number))
        else:
            self.n_number = len(genome)
            self.genome = genome
        self.male = male
        if self.male: self.genome[0][-1] = None
        self.parents = parents
        self.count = count
        self.id = None
    
    def add_genes(self, n, genes):
        # for i in range(len(gene)): self.genome[chromosome_n][i].append(gene[i])
        self.genome[n].add_genes(genes)
        return self

    def is_siblings(self, other):
        for my_parent in self.parents:
            is_same = False
            for their_parent in other.parents:
                is_same = is_same or my_parent is their_parent
            if not is_same: return False
        return True

    def __eq__(self, __o: object) -> bool:
        if self.n_number != __o.n_number: return False
        if not self.is_siblings(__o): return False
        # if (self.n_number != __o.n_number and 
            # not self.is_siblings(__o)): return False
        # if not self.is_siblings(__o): return False
        for c in range(self.n_number):
            if self.genome[c] != __o.genome[c]: return False
        return True

    def __hash__(self) -> int:
        if self.id is None:
            self.id = hash((self.n_number, frozenset(self.parents), self.genome))
        return self.id

    def __repr__(self) -> str:
        return "Genome: " + str(self.genome)

def add_worm(worm, worms):
    if worm in worms:
        worms[worms.index(worm)].count += worm.count
    else:
        worms.append(worm)

def cross(mom, dad):
    progeny = []
    for i in range(4**mom.n_number):
        genome = []
        for c in range(mom.n_number):
            pick_genes = lambda p, s: p.genome[c][0] if i & (1 << 2*c+s) else p.genome[c][1]
            # genome.append([pick_genes(mom, 0), pick_genes(dad, 1)])
            # print(pick_genes(mom,0))
            genome.append(ChromosomeSiblings())
            genome[c].set_chromosomes([pick_genes(mom, 0), pick_genes(dad, 1)])
        # add_worm(Worm(genome=genome, parents = (mom, dad), count = mom.count*dad.count), progeny)            
        add_worm(Worm(genome=tuple(genome), parents = (mom, dad)), progeny)
    return progeny