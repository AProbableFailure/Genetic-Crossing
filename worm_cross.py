from collections import Counter
from operator import attrgetter
import time

different_parents_is_different_worm = False

def tuplize_list_of_list(l):
    return tuple(None if i is None else tuple(i) for i in l)

class Worm:
    def __init__(self, genome = None, male = False, parents = (None, None), count = 1, n_number = 6, crosses_needed = 0) -> None:
        self.n_number, self.genome = (n_number, [[[], []] for i in range(n_number)]) if genome is None else (len(genome), genome)
        if male: self.genome[0][-1] = None
        self.parents = parents
        self.count = count
        self.hash_id = None
        self.crosses_needed = crosses_needed

    def add_gene(self, n, gene):
        for i in range(len(gene)): self.genome[n][i].append(gene[i])
    def has_chromosome(self, n, chromosome):
        return Counter(self.tuplized_genome()[n]) == Counter(tuplize_list_of_list(chromosome))
    def has_genome(self, genome):
        for c in range(len(genome)):
            if not self.has_chromosome(c, genome[c]): return False
        return True
    def is_homozygous(self, n, gene):
        for i in range(len(self.genome[n])):
            # if self.genome[n][i] is None: return False # can also be 'continue'
            if self.genome[n][i] is None or gene not in self.genome[n][i]: return False
        return True
    # def is_homozygous_multiple(self, ns, genes):
        # for i in range(len(ns)):
            # if not self.is_homozygous(ns[i], genes[i]): return False
        # return True
    def is_homozygous_multiple(self, genes):
        for i in range(len(genes)):
            for gene in genes[i]:
                if not self.is_homozygous(i, gene): return False
        return True


    #def has_gene(self, chromosome, gene):
        #for i in range(len(gene)): 
            #if gene[i] not in self.genome[chromosome][i]: return False
        #return True

    def is_male(self): return None in self.genome[0]
    def is_hermaphrodite(self): return not self.is_male()

    def generation(self):
        parents = [p for p in self.parents if p]
        if not parents: return 0
        else: return max(map(lambda w: w.generation(), parents)) + 1
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
            # add_worm(Worm(genome=genome, parents = (mom, dad), count = mom.count*dad.count), progeny)
            add_worm(Worm(genome=genome, parents = (mom, dad), crosses_needed=mom.crosses_needed+dad.crosses_needed + 1), progeny)
        return progeny

    def tuplized_genome(self):
        return tuple(tuple(None if j is None else tuple(j) for j in i) for i in self.genome)

    def set_genome(self):
        return tuple(frozenset(None if j is None else tuple(j) for j in i) for i in self.genome)

    def __hash__(self) -> int:
        # parents = frozenset(self.parents)# (frozenset(p) for p in self.parents)
        # return hash((parents, self.set_genome()))
        # self.hash_id = self.hash_id or hash((frozenset(self.parents), self.set_genome()))
        if self.hash_id is None:
            global different_parents_is_different_worm
            self.hash_id = hash((self.n_number, frozenset(self.parents) if different_parents_is_different_worm else self.generation(), self.set_genome()))
        return self.hash_id

    def __eq__(self, __o: object) -> bool:
        return hash(self) == hash(__o)

    # def __eq__(self, other: object) -> bool:
        # if set(self.parents) != set(other.parents): return False
        # if self.n_number != other.n_number: return False        
        # for c in range(self.n_number):
            # genome_set = lambda w: set(None if i is None else tuple(i) for i in w.genome[c])
            # if genome_set(self) != genome_set(other): return False
        # return True

    # def __hash__(self) -> int:
        # # print("HASH!")
        # return hash((self.parents, self.count, self.tuplized_genome()))

    def __str__(self) -> str:
        return "Generation: " + str(self.generation()) + "; Genome: " + str(self.genome) + "; Appears " + str(self.count) + " times"

def add_worm(worm, worms):
    if worm in worms:
        worms[worms.index(worm)].count += worm.count
    else:
        worms.append(worm)

# def cross(virgins, f, hermaphrodite_parents = [], male_parents = []):
    # if f == 0:
        # return hermaphrodite_parents + male_parents + virgins

    # males = []
    # hermaphrodites = []
    # progeny = []

    # for worm in virgins:
        # males.append(worm) if worm.is_male() else hermaphrodites.append(worm)
    
    # for egg in hermaphrodites:
        # for sperm in hermaphrodites + males:
            # progeny += egg.cross(sperm)

    # intergenerational_progeny = []
    # for virgin_egg in hermaphrodites:
        # for parent_sperm in hermaphrodite_parents + male_parents:
            # intergenerational_progeny += virgin_egg.cross(parent_sperm)
    
    # for parent_egg in hermaphrodite_parents:
        # for virgin_sperm in hermaphrodites + males:
            # for child in parent_egg.cross(virgin_sperm):
                # add_worm(child, intergenerational_progeny)

    # return cross(progeny + intergenerational_progeny, f-1, hermaphrodites + hermaphrodite_parents, males + male_parents)

# def cross(virgins, f, moms = [], dads = []):
    # if f == 0:
        # # for worm in virgins:
        # #     parents.append()
        # # All parents can give sperm
        # # virigns is of a new generation, so none of them will the same to the one prior
        # return dads + virgins

    # virgins_dads = virgins
    # virgins_moms = [w for w in virgins if w.is_hermaphrodite()]
    # progeny = []

    # for dad in virgins_dads:
        # for mom in virgins_moms:
            # progeny += mom.cross(dad)

    # # intergeneration_progeny = []
    # # for dad in dads:
        # # for mom in virgins_moms:
            # # progeny += mom.cross(dad)
    
    # # for dad in virgins_dads:
        # # for mom in moms:
            # # progeny += mom.cross(dad)

    # return cross(progeny, f-1, moms + virgins_moms, dads + virgins_dads)   


def cross(virgins, f, parents = set()):
    if f == 0:
        for worm in virgins:
            parents = list(parents)
            add_worm(worm, parents)
        return parents

    # all_worms = parents | (virgins if virgins is set else set(virgins))
    all_worms = parents | set(virgins)
    dads = all_worms# virgins + parents
    moms = {x for x in all_worms if x.is_hermaphrodite()}
    progeny = []

    for dad in dads:
        for mom in moms:
            # if dad in parents and mom in parents: continue
            if {mom, dad} <= parents: continue
            progeny += mom.cross(dad)
    
    return cross(progeny, f-1, all_worms)

def worm_with_quickest_path(worms, conditional):
    return min([worm for worm in worms if conditional(worm)], key=attrgetter('crosses_needed'))


def main():
    dad = Worm(n_number=3, male = True)
    dad.add_gene(0, ["dlg-1::mChr"])
    dad.add_gene(1, ["+", "+"])
    dad.add_gene(2, ["him-5", "him-5"])

    mom = Worm(n_number=3)
    mom.add_gene(0, ["+", "+"])
    mom.add_gene(1, ["cdc-42::GFP", "cdc-42::GFP"])
    mom.add_gene(2, ["+", "+"])

    progeny = cross([mom, dad], 3)
    print(len(progeny))

    for child in progeny:
        # if child.genome == [[["dlg-1::mChr"], ["dlg-1::mChr"]], [["cdc-42::GFP"], ["cdc-42::GFP"]], [["him-5"], ["him-5"]]]:
        # if child.is_homozygous_multiple([["dlg-1::mChr"], ["cdc-42::GFP"], ["him-5"]]):
        if child.generation() == 2:
            print(child)
            # for parent in child.parents:
            #     print(parent)
            # print()

        # if child.generation() == 2: 
            # print(child)
            # for parent in child.parents:
                # print(parent)
            # print()

    ###########################

    # dad = Worm(n_number=2, male = True)
    # dad.add_gene(0, ["dlg-1"])
    # dad.add_gene(1, ["+", "+"])

    # mom = Worm(n_number=2)
    # mom.add_gene(0, ["+", "+"])
    # mom.add_gene(1, ["cdc-42", "cdc-42"])

    # start = time.time()
    # progeny = cross([mom, dad], 3)
    # end = time.time()
    # print(end - start)

    # # print(min([worm for worm in progeny if worm.is_homozygous_multiple([["dlg-1"], ["cdc-42"]])], key=attrgetter('crosses_needed')))
    # print(worm_with_quickest_path(progeny, lambda w: w.is_homozygous_multiple([["dlg-1"], ["cdc-42"]])))

    # # for child in progeny:
        # # if child.is_homozygous_multiple([["dlg-1"], ["cdc-42"]]):
            # # print(child)
            # # for parent in child.parents:
                # # print(parent)
            # # print()

if __name__ == "__main__":
    main()