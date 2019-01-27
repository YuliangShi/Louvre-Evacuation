import numpy as np


# individual
class Individual:
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

    def __init__(self, position, init_length, init_velocity, max_velocity, row, block):
        self.row = row
        self.block = block
        self.v = init_velocity
        self.max_v = max_velocity
        self.len = init_length
        self.p = position  # 3-D position

        self.fall_over = False

        self.evacuated = False

        self.wait_time = 0

    def move(self, dt, dist):
        v, change_len = self.get_velocity(dist)
        self.p = v * dt + self.p
        self.len += change_len

    def get_velocity(self, dist, c=1.5):
        if 0.5 <= dist <= 8:
            return dist * c * self.block.dirc, dist * c
        else:
            return 0, 0

    def change_row(self, new_row):
        self.row = new_row
        self.block = self.row.block

    def fall_over(self):
        self.v = 0
        self.fall_over = True

    def is_in_block(self):
        if self.len > self.block.length / 2:
            return False
        else:
            return True

