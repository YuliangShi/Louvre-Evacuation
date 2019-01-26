from row import Row
import numpy as np


# block
class Block:
    """
    Hyper-parameter:
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

    def __init__(self, floor, A, B, width, length, dirc=True, density="light"):
        self.floor = floor
        self.A = A
        self.B = B
        self.width = width
        self.length = length
        self.n_r = int(width / 0.05)

        if dirc:
            self.dirc = (A - B) / np.linalg.norm(A - B)

        else:
            self.dirc = (B - A) / np.linalg.norm(B - A)

        project_dirc = np.concatenate((self.dirc[0:2], np.array([0])))
        normal_vector = np.cross(project_dirc, np.array([0, 0, 1]))
        mid_pt = (A + B) / 2
        if density == "light":
            self.all_rows = [Row(mid_pt + (i - (self.n_r + 1) / 2) * 0.05 * normal_vector, self, n_indv=length * 4)
                             for i in range(self.n_r)]
        elif density == "medium":
            self.all_rows = [Row(mid_pt + (i - (self.n_r + 1) / 2) * 0.05 * normal_vector, self, n_indv=length * 9)
                             for i in range(self.n_r)]
        elif density == "heavy":
            self.all_rows = [Row(mid_pt + (i - (self.n_r + 1) / 2) * 0.05 * normal_vector, self, n_indv=length * 15)
                             for i in range(self.n_r)]

        # self.inters = intersections

    # def change_dirc(self):
    # self.dirc = [-self.dirc[0], -self.dirc[1], -self.dirc[2]]
    # for each in self.all_rows:
    #     each.change_dirc
    # self.inters
