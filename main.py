from block import BLock
from idividual import Individual
from row import Row
from intersection import Intersection

## initialization

# maximum clock time and dt for each time step
clock_max = 2000
dt = 0.01

# 
temp_inters =

blocks = [Block(0, (-1, 0, 0), (0, 0, 0), 10, intersections)]
all_intersections = [Intersection((0, 0, 0), )]
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
        final_move = each.final_move(pass_code, dt)

    ## plot
    pass
