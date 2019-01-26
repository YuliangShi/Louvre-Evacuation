# block
def Class Block:
	"""
	Hyperparameter:
		floor: floor
		position of end A: A
		position of end B: B
		width: width
		capacity (number of rows): n_r
	Attribute:
		evacuating direction: dirc
		all rows: all_rows
		intersections: inters
	Methods:
		change_dirc: change evacuating direction of the block
		get_ave_speed: get average speed over all rows
	"""
	def __init__(self, floor, A, B, width, intersections, dirc=True):
		self.floor = floor
		self.start = start
		self.end = end
		self.width = width
		self.n_r = int(width / 0.9)

		if dirc:
			self.dirc = [A[0] - B[0], A[1] - B[1], A[2] - B[2]]

		else:
			self.dirc = [B[0] - A[0], B[1] - A[1], A[2] - B[2]]

		self.all_rows = [Row for _ in range(self.n_r)]

		self.inters = intersections
	

	def change_dirc(self):
		self.dirc = [-self.dirc[0], -self.dirc[1], -self.dirc[2]] 
		for each in self.all_rows:
			each.change_dirc
		self.inters