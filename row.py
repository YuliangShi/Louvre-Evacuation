# row 
def Class Row:
	"""
	attributes:
		all individuals: all_indv
		first person: first

	"""
	def __init__(self, first, all_indv, block):
		self.block = block
		self.first = first
		self.all_indv = all_indv
		self.n_indv = len(all_indv)

	def remove_first(self):
		self.first = self.all_indv[1]
		self.all_indv = self.all_indv[1:]
