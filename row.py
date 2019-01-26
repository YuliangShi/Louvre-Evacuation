# row 
class Row:
    """
    attributes:
        all individuals: all_indv
        first person: first

    """

    def __init__(self, mid_pt_pos, block, n_indv):
        self.block = block
        self.len = self.block.length
        self.mid_pt_pos = mid_pt_pos


        self.n_indv = n_indv
        self.all_indv = []
        self.first = self.all_indv[0]
        self.last = self.all_indv[-1]

    def remove_first(self):
        self.first = self.all_indv[1]
        self.all_indv = self.all_indv[1:]
