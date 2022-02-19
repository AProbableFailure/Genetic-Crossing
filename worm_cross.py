from collections import Counter

def tuplize_list_of_list(l):
    return tuple(None if i is None else tuple(i) for i in l)

class Worm:
    def __init__(self, genome = None, male = False, parents = (None, None), count = 1, n_number = 6) -> None:
        self.n_number, self.genome = (n_number, [[[], []] for i in range(n_number)]) if genome is None else (len(genome), genome)
        if male: self.genome[0][-1] = None
        self.parents = parents
        self.count = count

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
            add_worm(Worm(genome=genome, parents = (mom, dad), count = mom.count*dad.count), progeny)
        return progeny

    def tuplized_genome(self):
        return tuple(tuple(None if j is None else tuple(j) for j in i) for i in self.genome)

    def __eq__(self, other: object) -> bool:
        if set(self.parents) != set(other.parents): return False
        if self.n_number != other.n_number: return False        
        for c in range(self.n_number):
            genome_set = lambda w: set(None if i is None else tuple(i) for i in w.genome[c])
            if genome_set(self) != genome_set(other): return False
        return True

    def __hash__(self) -> int:
        # print("HASH!")
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
    progeny = []

    for dad in dads:
        for mom in moms:
            if dad in parents and mom in parents: continue
            progeny += mom.cross(dad)
    
    return cross(progeny, f-1, virgins + parents)

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

    for child in progeny:
        # if child.genome == [[["dlg-1::mChr"], ["dlg-1::mChr"]], [["cdc-42::GFP"], ["cdc-42::GFP"]], [["him-5"], ["him-5"]]]:
        # if child.has_chromosome(0, [["dlg-1::mChr"], ["dlg-1::mChr"]]) and child.has_chromosome(1, [["cdc-42::GFP"], ["cdc-42::GFP"]]) and child.has_chromosome(2, [["him-5"], ["him-5"]]):
        # if child.has_genome([[["dlg-1::mChr"], ["dlg-1::mChr"]], [["cdc-42::GFP"], ["cdc-42::GFP"]], [["him-5"], ["+"]]]):
        # if child.is_homozygous(0, "dlg-1::mChr") and child.is_homozygous(1, "cdc-42::GFP") and child.is_homozygous(2, "him-5"):
        # if child.is_homozygous_multiple([0, 1, 2], ["dlg-1::mChr", "cdc-42::GFP", "him-5"]):
        if child.is_homozygous_multiple([["dlg-1::mChr"], ["cdc-42::GFP"], ["him-5"]]):
            print(child)
            for parent in child.parents:
                print(parent)

if __name__ == "__main__":
    main()