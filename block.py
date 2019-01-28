from row import Row
import numpy as np
import numpy.linalg as LA


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

    def __init__(self, floor, A, B, width, dirc=True, density="light"):
        self.floor = floor
        self.A = A
        self.B = B
        self.width = width
        self.length = LA.norm(A - B) * 35.4
        self.n_r = int(width / 0.05)

        if dirc:
            self.dirc = (A - B) / LA.norm(A - B)

        else:
            self.dirc = (B - A) / LA.norm(B - A)

        project_dirc = np.concatenate((self.dirc[0:2], np.array([0])))
        normal_vector = np.cross(project_dirc, np.array([0, 0, 1]))
        mid_pt = (A + B) / 2
        if density == "light":
            self.all_rows = [Row(mid_pt + (i - (self.n_r + 1) / 2) * 0.05 * normal_vector, self, n_indv=int(self.length * 2))
                             for i in range(self.n_r)]
        elif density == "medium":
            self.all_rows = [Row(mid_pt + (i - (self.n_r + 1) / 2) * 0.05 * normal_vector, self, n_indv=int(self.length * 9))
                             for i in range(self.n_r)]
        elif density == "heavy":
            self.all_rows = [Row(mid_pt + (i - (self.n_r + 1) / 2) * 0.05 * normal_vector, self, n_indv=int(self.length * 15))
                             for i in range(self.n_r)]

    # def change_dirc(self):
    # self.dirc = [-self.dirc[0], -self.dirc[1], -self.dirc[2]]
    # for each in self.all_rows:
    #     each.change_dirc
    # self.inters

    def is_stair(self):
        if (self.A - self.B)[-1]:
            return True
        return False

    def verts_for_plot(self):
        if self.is_stair():
            return None
        else:
            normal_vec = np.cross(np.array([0, 0, 1]), self.dirc)
            verts = [
                tuple((self.A + (self.width / 2) * normal_vec)[:2]),
                tuple((self.A - (self.width / 2) * normal_vec)[:2]),
                tuple((self.B - (self.width / 2) * normal_vec)[:2]),
                tuple((self.B + (self.width / 2) * normal_vec)[:2]),
                tuple((self.A + (self.width / 2) * normal_vec)[:2])
            ]