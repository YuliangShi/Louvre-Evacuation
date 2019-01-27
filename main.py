from block import Block
from individual import Individual
from row import Row
from intersection import Intersection
import numpy as np
import numpy.linalg as LA

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# initialization

# maximum clock time and dt for each time step
clock_max = 100
dt = 1

# Codes for plot
codes_rect = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

codes_points = [
    # Path.MOVETO,
    # Path.LINETO,
    # Path.LINETO,
    # Path.LINETO,
    # Path.CLOSEPOLY,
]

# Data for plotting:
block_set_2_ = []
block_set_1_ = []
block_set_0 = []
block_set_1 = []
block_set_2 = []

all_block_to_plot = [
    block_set_2_,
    block_set_1_,
    block_set_0,
    block_set_1,
    block_set_2
]

ppl_2_ = []
ppl_1_ = []
ppl_0 = []
ppl_1 = []
ppl_2 = []

all_ppl_to_plot = [
    ppl_2_,
    ppl_1_,
    ppl_0,
    ppl_1,
    ppl_2
]

# Blocks and Intersections
block1 = Block(0, np.array([-20, 0, 0]), np.array([-10, 0, 0]), 10)
block2 = Block(0, np.array([10, 0, 0]), np.array([20, 0, 0]), 10)
all_blocks = [block1, block2]
inters1 = Intersection(np.array([0, 0, 0]), [block1, block2], 20, 20)
inters2 = Intersection(np.array([-30, 0, 0]), [block1], 20, 0, exit=True)
all_intersections = [inters1, inters2]

all_ppl = []
for b in all_blocks:
    for r in b.all_rows:
        for i in range(len(r.all_indv)):
            all_ppl.append(r.all_indv[i])

print(len(all_ppl))

time_to_plot = [i for i in range(clock_max // 4, clock_max + 1, clock_max // 4)]

# network = [[], []]
# pass
###########################################

for clock in range(1, clock_max):

    print("############################################")
    print()

    count = 0
    for each in all_ppl:
        print(each.p)
        if count == 10:
            break
        count += 1

    print()
    print("############################################")

    t = clock * dt

    for b in all_blocks:
        for r in b.all_rows:
            for i in range(len(r.all_indv)):
                cur = r.all_indv[i]
                dist = LA.norm(r.all_indv[i - 1].p - r.all_indv[i].p)
                cur.move(dt, dist)

    for each in all_intersections:
        each.final_move(dt)

    if clock in time_to_plot:
        for each_block in all_blocks:
            verts, floor = each_block.verts_for_plot()
            if verts:
                all_block_to_plot[floor + 2].append(verts)

        for each_inters in all_intersections:
            verts, floor = each_inters.verts_for_plot()
            if verts:
                all_block_to_plot[floor + 2].append(verts)

        print(all_block_to_plot[2])

        fig, ax = plt.subplots()
        for verts in all_block_to_plot[2]:
            path = Path(verts, codes_rect)
            patch = patches.PathPatch(path, facecolor='orange', lw=0.2)
            ax.add_patch(patch)
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)

        plt.show()
