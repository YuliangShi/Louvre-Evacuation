import random
import numpy.linalg as LA
import numpy as np


# intersection
class Intersection:
    """
    Attributes:
        position: position
    """

    def __init__(self, position, all_blocks, length, exit=False):
        self.position = np.array([position[0] * 35.4, position[1] * 35.4, position[2]])  # center of the intersection
        self.length = length * 35.4

        self.exit = exit

        self.all_blocks = all_blocks
        self.capacity = self.length * self.length * 0.4

        self.wait_time = 10  # waiting time in the intersection

        self.people = []

        self.in_blocks = []
        self.out_blocks = []
        self.in_rows = []
        self.out_rows = []

        self.n_in_rows = 0
        self.n_out_rows = 0

        for each in self.all_blocks:

            default = [each.A[0] - each.B[0], each.A[1] - each.B[1], each.A[1]]

            if LA.norm(each.A - self.position) < LA.norm(each.B - self.position):
                if each.dirc == default[:-1]:
                    self.in_blocks.append(each)
                    self.in_rows += each.all_rows
                    self.n_in_rows += each.n_r
                else:
                    self.out_blocks.append(each)
                    self.out_rows += each.all_rows
                    self.n_out_rows += each.n_r
            else:
                if each.dirc == default[:-1]:
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

    def final_move(self, dt):
        # for people in the rows towards the intersection
        if len(self.people) < self.capacity:
            for row in self.in_rows:
                for ppl in row.all_indv:
                    if ppl.is_in_block():
                        break
                    self.capacity += 1
                    row.remove_first()
                    ppl.wait_time = self.wait_time
                    ppl.v = 0
                    ppl.p = self.position
                    ppl.block = self
                    ppl.row = None

        # for people already in the intersection
        if not self.exit:
            count = 0
            for ppl in self.people:
                ppl.wait_time -= dt
                if ppl.wait_time <= 0:
                    self.capacity -= 1
                    index = count
                    select_row = self.out_rows[index]
                    ppl.change_row(select_row)
                    ppl.p = select_row.mid_pt_pos - (self.len / 2) * ppl.block.dirc  # endpoint
                    if count == self.n_out_row:
                        count = 0
                    else:
                        count += 1

    def verts_for_plot(self):
        verts = [
            tuple((self.position + np.array([(self.length / 2), (self.length / 2), 0]))[:2]),
            tuple((self.position + np.array([-(self.length / 2), (self.length / 2), 0]))[:2]),
            tuple((self.position + np.array([-(self.length / 2), -(self.length / 2), 0]))[:2]),
            tuple((self.position + np.array([(self.length / 2), -(self.length / 2), 0]))[:2]),
            tuple((self.position + np.array([(self.length / 2), (self.length / 2), 0]))[:2])
        ]
        return verts, int(self.position[2])