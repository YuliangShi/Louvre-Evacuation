# initialization
clock_max = 2000
dt = 0.01
all_intersections = []
blocks = [for _ in range(N_blocks)]
network = [[], []]
pass
###########################################

for clock in range(1, clock_max):
	t = clock * dt

	for b in blocks:
		for r in b.all_rows:
			for each in r.all_indv:
				position = each.move()
				if True:
					pass
				else:
					pass

	for each in intersections:
		pass_code = each.pass_code()
		final_move = each.final_move(pass_code)

	## plot
	pass