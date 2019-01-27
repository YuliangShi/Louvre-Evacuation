from individual import Individual
from numpy import random


# row
class Row:
    """
    attributes:
        all individuals: all_indv
        first person: first

    """

    def __init__(self, mid_pt_pos, block, n_indv, ave_init_v=1, epsilon=0.5):
        self.block = block
        self.len = self.block.length
        self.mid_pt_pos = mid_pt_pos

        self.n_indv = n_indv

        all_init_pos = sorted([random.uniform(-self.len / 2, self.len / 2) for _ in range(self.n_indv)])
        self.all_indv = [Individual(mid_pt_pos + all_init_pos[i] * self.block.dirc, all_init_pos[i],
                                    ave_init_v + random.uniform(-epsilon, epsilon), 3 * ave_init_v, self, self.block)
                         for i in range(self.n_indv)]
        self.first = self.all_indv[0]
        self.last = self.all_indv[-1]

    def remove_first(self):
        if len(self.all_indv) >= 2:
            self.first = self.all_indv[1]
            self.all_indv = self.all_indv[1:]
        else:
            self.first = None
            self.all_indv = []
        self.n_indv -= 1

    def add_last(self, new_indv):
        self.first = new_indv
        self.all_indv = self.all_indv.append(new_indv)
        self.n_indv += 1
