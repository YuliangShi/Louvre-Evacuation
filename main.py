from block import Block
from individual import Individual
from row import Row
from intersection import Intersection
import numpy as np
import numpy.linalg as LA
import random

from FloorMap import blocklst, intersectionlst

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# initialization

# maximum clock time and dt for each time step
clock_max = 20
dt = 0.01

# Codes for plot
codes_rect = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
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
# block1 = Block(0, np.array([-50, 0, 0]), np.array([-1, 0, 0]), 10)
# block2 = Block(0, np.array([1, 0, 0]), np.array([50, 0, 0]), 10)
all_blocks = blocklst
# inters1 = Intersection(np.array([0, 0, 0]), [block1, block2], 2, 2)
# inters2 = Intersection(np.array([-51, 0, 0]), [block1], 2, 0, exit=True)
all_intersections = intersectionlst

all_ppl = []
for b in all_blocks:
    for r in b.all_rows:
        for i in range(len(r.all_indv)):
            all_ppl.append(r.all_indv[i])

sample_ppl = random.sample(all_ppl, len(all_ppl) // 200)

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
        # print(each.p)
        if count == 1:
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
            # print(each_block)

            verts, floor = each_block.verts_for_plot()

            if verts:
                all_block_to_plot[floor + 2].append(verts)

        for each_inters in all_intersections:
            verts, floor = each_inters.verts_for_plot()
            if verts:
                all_block_to_plot[floor + 2].append(verts)

        for each_p in sample_ppl:
            pos = each_p.p
            # print(pos)
            all_ppl_to_plot[int(pos[-1] + 2)].append(tuple(pos[:2]))

        # print(all_block_to_plot[2])

        fig, ax = plt.subplots()

        # print(all_block_to_plot[F + 2])
        for verts in all_block_to_plot[F + 2]:
            path = Path(verts, codes_rect)
            patch = patches.PathPatch(path, facecolor='orange', lw=0.2)
            ax.add_patch(patch)

        # # print(all_ppl_to_plot)
        # xs, ys = zip(*all_ppl_to_plot[2])
        # ax.plot(xs, ys, 'x', lw=2, color='black', ms=2)

        ax.set_xlim(50, 800)
        ax.set_ylim(0, 400)

        plt.show()
