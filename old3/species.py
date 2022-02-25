
# def c_elegans_sex_determination(organism):
# 	if None in organism.genome[0]

# c_elegans = Species()

class Species:
	# def __init__(self, sex_determination) -> None:
	def __init__(self, ploidy, xnum) -> None:
		self.ploidy = ploidy
		self.xnum = xnum
		# self.sex_determination = sex_determination

class C_elegans(Species):
	def __init__(self) -> None:
		super().__init__(ploidy = 2, xnum = 3)

	def sex_determination(self, organism):
		if None in list(organism.genome[0].values())[0]: return "Male"
		else: return "Hermaphrodite"