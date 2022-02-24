class ChromosomeSiblings:
    def __init__(self) -> None:
        self.chromosomes = [Chromosome(), Chromosome()]
    
    def add_genes(self, genes):
        for i in range(len(genes)): self.chromosomes[i].add_gene(genes[i])

    def set_chromosomes(self, genes):
        for i in range(len(genes)): self.chromosomes[i] = genes[i]

    def __getitem__(self, i):
        return self.chromosomes[i]

    def __setitem__(self, i, value):
        self.chromosomes[i] = value

    def __eq__(self, __o: object) -> bool:
        # print(self.chromosomes)
        return set(self.chromosomes) == set(__o.chromosomes)
    
    def __hash__(self) -> int:
        return hash(tuple(self.chromosomes))
    
    def __repr__(self) -> str:
        return str(self.chromosomes)

class Chromosome:
    """ Actually a pair of chromosomes """
    def __init__(self) -> None:
        self.genes = []

    def add_gene(self, gene):
        self.genes.append(gene)

    def __getitem__(self, i):
        return self.genes[i]
    
    def __setitem__(self, i, value):
        self.genes[i] = value

    def __eq__(self, __o: object) -> bool:
        return self.genes == __o.genes

    def __hash__(self) -> int:
        return hash(tuple(self.genes))
    
    def __repr__(self):
        return str(self.genes)