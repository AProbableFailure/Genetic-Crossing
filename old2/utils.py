def get_first_key(dictionary):
	for key in dictionary:
		return key
	raise IndexError

def to_tuple(lst):
    return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)