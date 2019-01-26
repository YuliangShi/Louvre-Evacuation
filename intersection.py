import random 
import numpy.linalg as LA

# intersection
class Intersection:
	"""
	Atributes:
		position: position
		
	"""
	def __init__(self, position, length, all_blocks, capacity):
		self.position = position
		self.length = length
		self.all_blocks = all_blocks
		self.capacity = capacity
		
		self.in_blocks = []
		self.out_blocks = []
		self.in_rows = []
		self.out_rows = []

		self.n_in_rows = 0
		self.n_out_rows = 0
	
	def update(self):
		for each in self.all_blocks:

 			default = [each.A[0] - each.B[0], each.A[1] - each.B[1], each.A[1]]
# 			if each.A == self.position:
# 				if each.dirc == default:
# 					self.in_blocks.append(each)
# 					self.n_in_rows += each.n_r
# 				else:
# 					self.out_blocks.append(each)
# 					self.n_out_rows += each.n_r

# 			else:
# 				if each.dirc == default:
# 					self.out_blocks.append(each)
# 					self.n_out_rows += each.n_r
# 				else:
# 					self.in_blocks.append(each)
# 					self.n_in_rows += each.n_r
			if LA.norm(each.A - default) < LA.norm(each.B - default):
				if each.dirc == default[:-1]:
					self.in_blocks.append(each)
					self.in_rows += each.all_rows
					self.n_in_rows += each.n_r
				else:
					self.out_blocks.append(each)
					self.out_rows += each.all_rows
					self.n_out_rows += each.n_r
			else:
				if each.dirc == default:
					self.out_blocks.append(each)
					self.out_rows += each.all_rows
					self.n_out_rows += each.n_r
				else:
					self.in_blocks.append(each)
					self.in_rows += each.all_rows
					self.n_in_rows += each.n_r

	def get_out_blocks(self):
		return self.out_blocks
	
	def get_in_blocks(self):
		return self.in_blocks
	
	def final_move(self):
		

# 	def pass_code(self):
# 		if self.n_in_rows <= self.n_out_rows:
# 			return [i for i in range(n_in_rows)]
# 		to_return = [i for i in range(n_out_rows)]
# 		to_return = to_return + [random.randint(0, len(n_out_rows) - 1) for _ in range(n_in_rows - n_out_rows)]
# 		return to_return

# 	def final_move(self, pass_code, dt):
# 		for k in range(n_out_rows):
# 			indices = [i for i, x in enumerate(pass_code) if x == k]
# # 			choice = random.randint(0, len(indices) - 1)
# # 			for j in indices:
# # 				if j != choice:
# # 					pass_code[j] = -1
# 			# enumerate and move cars
# 			for each in indices:
# 				row = self.in_rows[each]
# 				for ppl in row.all_indv:
# 					vel = v.get_velocity
# 					dist = min(LA.norm(ppl.block.A - ppl.position), LA.norm(ppl.block.B - ppl.position))
# 					if vel * dt > dist:
# 						ppl.change_row(self.out_rows[k])
# 						ppl.block = k.block
# 						ppl.position = self.out_rows[k].last.postion + 

