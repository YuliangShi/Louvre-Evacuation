from block import Block
from intersection import Intersection
import numpy as np


# def __init__(self, floor, A, B, width, dirc=True)
# def __init__(self, position, all_blocks,width):

block1 = Block(1, np.array([3.7, 2, 1]), np.array([8.3, 2, 1]), 0.4)
block2 = Block(1, np.array([8.5, 2.2, 1]), np.array([8.5, 3.2, 1]), 0.4)
block3 = Block(1, np.array([8.7, 3.4, 1]), np.array([10.2, 3.4, 1]), 0.4)
block4 = Block(1, np.array([8.7, 2.2, 1]), np.array([10.2, 2.2, 1]), 0.4)
block5 = Block(1, np.array([10.4, 2.2, 1]), np.array([10.4, 3.2, 1]), 0.4)
block6 = Block(1, np.array([10.6, 3.4, 1]), np.array([12.1, 3.4, 1]), 0.4)
block7 = Block(1, np.array([10.6, 2.2, 1]), np.array([12.1, 2.2, 1]), 0.4)
block8 = Block(1, np.array([13.9, 3.4, 1]), np.array([14.3, 3.4, 1]), 0.4)
block9 = Block(1, np.array([14.55, 3.35, 1]), np.array([17.55, 3.35, 1]), 0.5)
block10 = Block(1, np.array([17.8, 3.35, 1]), np.array([17.8, 6.55, 1]), 0.4)
block11 = Block(1, np.array([17.8, 3.6, 1]), np.array([17.8, 4.4, 1]), 0.3)
block12 = Block(1, np.array([10.8, 9.6, 1]), np.array([12.3, 9.6, 1]), 0.5)
block13 = Block(1, np.array([10.8, 8.1, 1]), np.array([12.3, 8.1, 2]), 0.5) # it is a stair
block14 = Block(1, np.array([8.8, 9.6, 1]), np.array([10.3, 9.6, 1]), 0.5)
block15 = Block(1, np.array([8.8, 8.1, 1]), np.array([10.3, 8.1, 1]), 0.5)
block16 = Block(1, np.array([6, 9.6, 1]), np.array([8.3, 9.6, 1]), 0.5)
block17 = Block(1, np.array([8.3, 9.35, 1]), np.array([8.3, 8.35, 1]), 0.5)
block18 = Block(1, np.array([10.55, 9.35, 1]), np.array([10.55, 8.35, 1]), 0.5)

# block for stairs
block19 = Block(0.5, np.array([8.3, 3.4, 1]), np.array([8.7, 3.4, 0]), 0.2)
block20 = Intersection(np.array([13, 2.9, 1]), [block6, block7, block8], 1.6)

intersectiona = Intersection(np.array([8.5, 2, 1]), [block1, block2, block4], 0.4)
intersectionb = Intersection(np.array([8.5, 3.4, 1]), [block2, block3], 0.4)  # stairs
intersectionc = Intersection(np.array([10.4, 3.4, 1]), [block3, block5, block6], 0.4)
intersectiond = Intersection(np.array([10.4, 2, 1]), [block4, block5, block7], 0.4)
intersectione = Intersection(np.array([13, 2.9, 1]), [block6, block7, block8], 1.6)  # stairs
intersectionf = Intersection(np.array([14.55, 3.35, 1]), [block8, block9, block11], 0.5)
intersectiong = Intersection(np.array([17.8, 3.35, 1]), [block9, block10], 0.5) # stairs
intersectionh = Intersection(np.array([13.3, 8.85, 1]), [block12, block13], 2)
intersectioni = Intersection(np.array([10.55, 9.6, 1]), [block12, block14, block18], 0.5) # stairs
intersectionj = Intersection(np.array([10.55, 8.1, 1]), [block13, block15, block18], 0.5)
intersectionk = Intersection(np.array([8.3, 8.1, 1]), [block15,block17], 0.5)
intersectionl = Intersection(np.array([8.55, 9.6, 1]), [block14, block16, block17], 0.5)
intersectionm = Intersection(np.array([17.8, 4.8, 1]), [block11], 0.8)  # stairs
intersectionn = Intersection(np.array([8.3, 2, 1]), [block1], 0.4)  # stairs
intersectiono = Intersection(np.array([17.8, 6.8, 1]), [block10], 0.5)  # stairs


blocklst = [block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,
            block13,block14,block15,block16,block17,block18]
intersectionlst = [intersectiona,intersectionb,intersectionc,intersectiond,
                intersectione, intersectionf, intersectiong, intersectionh,
                intersectioni, intersectionj, intersectionk, intersectionl,
                intersectionm,intersectionn,intersectiono]
