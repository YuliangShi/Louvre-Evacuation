from block import Block
from intersection import Intersection
import numpy as np

# floor0
blocka = Block(0, np.array([3.7, 3, 0]), np.array([5.3, 3, 1]), 0.8)
blockb = Block(0, np.array([8.5, 2.2, 0]), np.array([8.5, 3.2, 0]), 0.4)
blockc = Block(0, np.array([8.7, 3.4, 0]), np.array([10.2, 3.4, 0]), 0.4)
blockd = Block(0, np.array([10.4, 2.2, 0]), np.array([10.4, 3.2, 0]), 0.4)
blocke = Block(0, np.array([10.6, 3.4, 0]), np.array([12.1, 3.4, 0]), 0.4)
blockf = Block(0, np.array([13.9, 3.4, 0]), np.array([14.3, 3.4, 0]), 0.4)
blockg = Block(0, np.array([14.55, 3.35, 0]), np.array([17.55, 3.35, 0]), 0.5)
blockh = Block(0, np.array([17.8, 3.6, 0]), np.array([17.8, 6.6, 0]), 0.4)
blocki = Block(0, np.array([17.8, 3.6, 0]), np.array([17.8, 4.4, 0]), 0.3)
blockj = Block(0, np.array([17.8, 5.3, 0]), np.array([17.8, 8.35, 0]), 0.4)
blockk = Block(0, np.array([10.8, 8.1, 0]), np.array([12.3, 8.1, 0]), 0.5)
blockl = Block(0, np.array([10.8, 9.6, 0]), np.array([12.3, 9.6, 0]), 0.5)
blockm = Block(0, np.array([8.8, 9.6, 0]), np.array([10.3, 9.6, 0]), 0.5)
blockn = Block(0, np.array([8.8, 8.1, 0]), np.array([10.3, 8.1, 0]), 0.5)
blocko = Block(0, np.array([8.3, 9.35, 0]), np.array([8.3, 8.35, 0]), 0.5)
# floor1
blockp = Block(1, np.array([3.7, 2.2, 1]), np.array([8.3, 2.2, 1]), 0.4)
blockq = Block(1, np.array([8.5, 2.2, 1]), np.array([8.5, 3.2, 1]), 0.4)
blockr = Block(1, np.array([8.7, 3.4, 1]), np.array([10.2, 3.4, 1]), 0.4)
blocks = Block(1, np.array([8.7, 2.2, 1]), np.array([10.2, 2.2, 1]), 0.4)
blockt = Block(1, np.array([10.4, 2.2, 1]), np.array([10.4, 3.2, 1]), 0.4)
blocku = Block(1, np.array([10.6, 3.4, 1]), np.array([12.1, 3.4, 1]), 0.4)
blockv = Block(1, np.array([10.6, 2.2, 1]), np.array([12.1, 2.2, 1]), 0.4)
blockw = Block(1, np.array([13.9, 3.4, 1]), np.array([14.3, 3.4, 1]), 0.4)
blockx = Block(1, np.array([14.55, 3.35, 1]), np.array([17.55, 3.35, 1]), 0.5)
blocky = Block(1, np.array([18.05, 3.6, 1]), np.array([18.05, 6.6, 1]), 0.4)
blockz = Block(1, np.array([14.55, 3.6, 1]), np.array([14.55, 4.4, 1]), 0.3)
blockaa = Block(1, np.array([10.8, 9.6, 1]), np.array([12.3, 9.6, 1]), 0.5)
blockab = Block(1, np.array([10.8, 8.1, 1]), np.array([12.3, 8.1, 1]), 0.5)  # it is a stair
blockac = Block(1, np.array([8.8, 9.6, 1]), np.array([10.3, 9.6, 1]), 0.5)
blockad = Block(1, np.array([8.8, 8.1, 1]), np.array([10.3, 8.1, 1]), 0.5)
blockae = Block(1, np.array([6, 9.6, 1]), np.array([8.3, 9.6, 1]), 0.5)
blockaf = Block(1, np.array([8.3, 9.35, 1]), np.array([8.3, 8.35, 1]), 0.5)
blockag = Block(1, np.array([10.55, 9.35, 1]), np.array([10.55, 8.35, 1]), 0.5)

# block for floor -1
blockao = Block(-1, np.array([8.8, 9.6, -1]), np.array([10.3, 9.6, -1]), 0.5)
blockap = Block(-1, np.array([10.8, 9.6, -1]), np.array([12.3, 9.6, -1]), 0.5)
blockaq = Block(-1, np.array([8.8, 8.1, -1]), np.array([10.3, 8.1, -1]), 0.5)
blockar = Block(-1, np.array([10.8, 8.1, -1]), np.array([12.3, 8.1, -1]), 0.5)
blockas = Block(-1, np.array([17.8, 3.6, -1]), np.array([17.8, 4.4, -1]), 0.3)
blockat = Block(-1, np.array([14.95, 4.8, -1]), np.array([16, 4.4, -1]), 0.8)
blockau = Block(-1, np.array([8.7, 3.4, -1]), np.array([10.2, 3.4, -1]), 0.4)
blockav = Block(-1, np.array([8.5, 2.2, -1]), np.array([8.5, 3.2, -1]), 0.4)
blockaw = Block(-1, np.array([10.4, 2.2, -1]), np.array([10.4, 3.2, -1]), 0.4)
blockax = Block(-1, np.array([10.6, 3.4, -1]), np.array([12.1, 3.4, -1]), 0.4)
blockay = Block(-1, np.array([10.6, 2.2, -1]), np.array([12.1, 2.2, -1]), 0.4)
blockaz = Block(-1, np.array([10.55, 9.35, -1]), np.array([10.55, 8.35, -1]), 0.5)

# block for floor 2
blockbg = Block(2, np.array([8.3, 9.35, 2]), np.array([8.3, 8.35, 2]), 0.5)
blockbh = Block(2, np.array([8.8, 9.6, 2]), np.array([10.3, 9.6, 2]), 0.5)
blockbi = Block(2, np.array([8.8, 8.1, 2]), np.array([10.3, 8.1, 2]), 0.5)
blockbj = Block(2, np.array([10.55, 9.35, 2]), np.array([10.55, 8.35, 2]), 0.5)
blockbk = Block(2, np.array([10.8, 9.6, 2]), np.array([12.3, 9.6, 2]), 0.5)
blockbl = Block(2, np.array([10.8, 8.1, 2]), np.array([12.3, 8.1, 2]), 0.5)
blockbm = Block(2, np.array([17.8, 5.3, 2]), np.array([17.8, 8.35, 2]), 0.4)
blockbn = Block(2, np.array([17.8, 3.6, 2]), np.array([17.8, 4.4, 2]), 0.3)
blockbo = Block(2, np.array([14.55, 3.35, 2]), np.array([17.55, 3.35, 2]), 0.5)
blockbp = Block(2, np.array([17.8, 3.6, 2]), np.array([17.8, 6.6, 2]), 0.4)

# block for stairs from floor 1 to floor 0
# stair in inter16 and 1
blockah = Block(0.5, np.array([8.3, 3.4, 1]), np.array([8.7, 3.4, 0]), 0.2)
# stair in inter19 and 3
blockai = Block(0.5, np.array([12.2, 2.9, 1]), np.array([13.8, 3.4, 0]), 0.2)
# stair in inter21 and 5
blockaj = Block(0.5, np.array([17.8, 3.35, 1]), np.array([18.3, 3.35, 0]), 0.2)
# stair in inter23 and 9
blockak = Block(0.5, np.array([10.3, 9.6, 1]), np.array([10.8, 9.6, 0]), 0.2)
# stair in inter27 and 7
blockal = Block(0.5, np.array([17.4, 4.8, 1]), np.array([18.2, 4.8, 0]), 0.2)
# stari in inter28 and 0
blockam = Block(0.5, np.array([8.1, 2, 1]), np.array([8.5, 2, 0]), 0.2)
# stari in inter29 and 6
blockan = Block(0.5, np.array([17.55, 6.8, 1]), np.array([18.05, 6.8, 0]), 0.2)

# block for stairs from floor 0 to floor -1
# stair in inter11 and 35
blockba = Block(-0.5, np.array([8.3, 9.6, 0]), np.array([8.8, 9.6, -1]), 0.2)
# stair in inter10 and  14
blockbb = Block(-0.5, np.array([10.3, 8.1, 0]), np.array([10.8, 8.1, -1]), 0.2)
# stair in inter1 and 32
blockbc = Block(-0.5, np.array([8.3, 3.4, 0]), np.array([8.7, 3.4, -1]), 0.2)
# stair in inter2 and 30
blockbd = Block(-0.5, np.array([10.2, 3.4, 0]), np.array([10.6, 3.4, -1]), 0.2)
# stair in inter3 and 33
blockbe = Block(-0.5, np.array([12.2, 2.9, 0]), np.array([13.8, 2.9, -1]), 0.2)
# stair in inter7 and 34
blockbf = Block(-0.5, np.array([14.15, 4.8, 0]), np.array([14.95, 4.8, -1]), 0.2)

# block for stairs from floor 2 to floor 1
# stair in inter39 and 23
blockbq = Block(1.5, np.array([10.3, 9.6, 2]), np.array([10.8, 9.6, 1]), 0.2)
# stair in inter40 and 24
blockbr = Block(1.5, np.array([10.3, 8.1, 2]), np.array([10.8, 8.1, 1]), 0.2)
# stair in inter42 and 27
blockbs = Block(1.5, np.array([14.15, 4.8, 2]), np.array([14.95, 4.8, 1]), 0.2)
# stair in inter44 and 21
blockbt = Block(1.5, np.array([17.8, 3.35, 2]), np.array([18.3, 3.35, 1]), 0.2)


# floor -1
intersection13 = Intersection(np.array([10.55, 9.6, -1]), [blockao,blockap], 0.5)
intersection14 = Intersection(np.array([10.55, 8.1, -1]), [blockaq,blockar,blockbb], 0.5)
intersection30 = Intersection(np.array([10.4, 3.4, -1]), [blockau,blockax,blockaw,blockbd], 0.4)
intersection31 = Intersection(np.array([10.4, 2, -1]), [blockaw,blockay], 0.4)
intersection32 = Intersection(np.array([8.5, 3.4, -1]), [blockav, blockau,blockbc], 0.4)
intersection33 = Intersection(np.array([13, 2.9, -1]), [blockax, blockay,blockbe], 1.6)
intersection34 = Intersection(np.array([14.55, 4.8, -1]), [blockas, blockat,blockbf], 0.8)
intersection35 = Intersection(np.array([8.55, 9.6, -1]), [blockao,blockba], 0.5)
intersection36 = Intersection(np.array([5.7, 3, -1]), [blocka], 0.8)
# floor 0
intersection0 = Intersection(np.array([8.3, 2.5, 0]), [blocka,blockam], 0.8)
intersection1 = Intersection(np.array([8.5, 3.4, 0]), [blockb, blockc, blockah, blockbc], 0.4)  # stairs for floor 1
intersection2 = Intersection(np.array([10.4, 3.4, 0]), [blockc, blockd, blocke, blockbd], 0.4)
intersection3 = Intersection(np.array([13, 2.9, 0]), [blocke, blockf, blockai, blockbe], 1.6)
intersection4 = Intersection(np.array([14.55, 3.35, 0]), [blockf, blocki, blockg], 0.5)
intersection5 = Intersection(np.array([18.05, 3.35, 0]), [blockg, blockh, blockaj], 0.5)
intersection6 = Intersection(np.array([18.05, 6.8, 0]), [blockh, blockan], 0.5)
intersection7 = Intersection(np.array([14.55, 4.8, 0]), [blockj, blocki, blockal, blockbf], 0.8)
intersection8 = Intersection(np.array([13.3, 8.85, 0]), [blockl, blockk, blockj], 2)
intersection9 = Intersection(np.array([10.55, 9.6, 0]), [blockl, blockm, blockak], 0.5)
intersection10 = Intersection(np.array([10.55, 8.1, 0]), [blockn, blockk, blockbb], 0.5)
intersection11 = Intersection(np.array([8.55, 9.6, 0]), [blockm, blocko, blockba], 0.5)
intersection12 = Intersection(np.array([8.3, 8.1, 0]), [blockn, blocko], 0.5)

# floor 1
intersection15 = Intersection(np.array([8.5, 2, 1]), [blockp, blockq, blocks], 0.4)
intersection16 = Intersection(np.array([8.5, 3.4, 1]), [blockq, blockr, blockah], 0.4)  # stairs
intersection17 = Intersection(np.array([10.4, 3.4, 1]), [blockr, blockt, blocku], 0.4)
intersection18 = Intersection(np.array([10.4, 2, 1]), [blocks, blockt, blockv], 0.4)
intersection19 = Intersection(np.array([13, 2.9, 1]), [blocku, blockv, blockw, blockai], 1.6)  # stairs
intersection20 = Intersection(np.array([14.55, 3.35, 1]), [blockw, blockx, blockz], 0.5)
intersection21 = Intersection(np.array([18.05, 3.35, 1]), [blockx, blocky, blockaj, blockbt], 0.5)  # stairs
intersection22 = Intersection(np.array([13.3, 8.85, 1]), [blockaa, blockab], 2)
intersection23 = Intersection(np.array([10.55, 9.6, 1]), [blockaa, blockac, blockag, blockak, blockbq], 0.5)  # stairs
intersection24 = Intersection(np.array([10.55, 8.1, 1]), [blockab, blockad, blockag, blockbr], 0.5)
intersection25 = Intersection(np.array([8.3, 8.1, 1]), [blockad, blockaf], 0.5)
intersection26 = Intersection(np.array([8.55, 9.6, 1]), [blockac, blockae, blockaf], 0.5)
intersection27 = Intersection(np.array([14.55, 4.8, 1]), [blockz, blockal, blockbs], 0.8)  # stairs
intersection28 = Intersection(np.array([8.3, 2, 1]), [blockp, blockam], 0.4)  # stairs
intersection29 = Intersection(np.array([17.8, 6.8, 1]), [blocky, blockan], 0.5)  # stairs

# floor 2
intersection37 = Intersection(np.array([8.55, 9.6, 2]), [blockbh, blockbg], 0.5)
intersection38 = Intersection(np.array([8.3, 8.1, 2]), [blockbg, blockbi], 0.5)
intersection39 = Intersection(np.array([10.55, 9.6, 2]), [blockbh, blockbj,blockbk, blockbq], 0.5)
intersection40 = Intersection(np.array([10.55, 8.1, 2]), [blockbi, blockbj, blockbl, blockbr], 0.5)
intersection41 = Intersection(np.array([13.3, 8.85, 2]), [blockbk, blockbl, blockbm], 2)
intersection42 = Intersection(np.array([14.55, 4.8, 2]), [blockbm, blockbh, blockbs], 0.8)
intersection43 = Intersection(np.array([14.55, 3.35, 2]), [blockbh,blockbo], 0.5)
intersection44 = Intersection(np.array([18.05, 3.35, 2]), [blockbo, blockbp, blockbt], 0.5)

blocklst = [blocka, blockb, blockc, blockd, blocke, blockf, blockg, blockh,
            blocki, blockj, blockk, blockl, blockm, blockn, blocko, blockp,
            blockq, blockr, blocks, blockt, blocku, blockv, blockw, blockx,
            blocky, blockz, blockaa, blockab, blockac, blockad, blockae, blockaf,
            blockag, blockah, blockai, blockaj, blockak, blockal, blockam, blockan,
            blockao, blockap, blockaq, blockar, blockas, blockat, blockau, blockav,
            blockaw, blockax, blockay, blockaz, blockba, blockbb, blockbc, blockbd,
            blockbe, blockbf, blockbg, blockbh, blockbi, blockbj, blockbk, blockbl,
            blockbm, blockbn, blockbo, blockbp, blockbq, blockbr, blockbs, blockbt]

intersectionlst = [intersection0, intersection1, intersection2, intersection3, intersection4,
                   intersection5, intersection6, intersection7, intersection8, intersection9,
                   intersection10, intersection11, intersection12, intersection13, intersection14,
                   intersection15, intersection16, intersection17, intersection18, intersection19,
                   intersection20, intersection21, intersection22, intersection23, intersection24,
                   intersection25, intersection26, intersection27, intersection28, intersection29,
                   intersection30, intersection31, intersection32, intersection33, intersection34,
                   intersection35, intersection36, intersection37, intersection38, intersection39,
                   intersection40, intersection41, intersection42, intersection43, intersection44]
