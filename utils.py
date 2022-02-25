from collections import Counter

class OrderedSet:
	def __init__(self, *values) -> None:
		#self.values = values # tuple(v for v in values)
		# print(len(values))
		# self.values = tuple(v for v in values)
		self.ordered = tuple(v for v in values)
		# self.s = Counter(self.ordered)
		self.set = Counter(v if type(v) is not dict else frozenset(v.items()) for v in values)

	def __getitem__(self, index):
		return self.ordered[index]

	def __contains__(self, value):
		return value in self.ordered

	def __eq__(self, other: object) -> bool:
		# print(self.values)
		# print(Counter(self.values))
		# return Counter(self.values) == Counter(other.values)
		return self.set == other.set

	def __hash__(self) -> int:
		return hash(frozenset(self.set.items()))
		# return hash(frozenset(Counter(self.values).items()))
		# return hash(Counter(self.values))
	
	def __repr__(self) -> str:
		return "OrderedSet" + str(self.ordered)