# individual
def Class Individual:
	"""
	Attribute:
		maximum velocity: max_v
		current velocity: v
		corresponding block: block
		corresponding position: p

	Method:
		get current velocity: get_velocity
		change to another row: change_row (only to adjacent row)
		fall_over
	"""

	def __init__(self, position, init_velocity, max_velocity, row, block)
		self.row = row
		self.block = block
		self.v = init_velocity
		self.max_v = max_velocity
		self.p = position  # 3-D position

		self.fall_over = False

		self.evacuated = False

	def move(self, dt, dist):
		v = self.get_velocity(dist)
		self.position = v * dt + self.p  ###

	def get_velocity(self, dist, c=2):
		return min(self.max_v, dist * c) * self.block.dirc ###

	def change_row(self, new_row):
		self.row = new_row

	def fall_over(self):
		self.v = 0 
		self.fall_over = True
