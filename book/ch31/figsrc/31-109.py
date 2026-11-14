import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
O = (20, 34); r = 14
disc(ax, *O, r, 'fixe', fill=False)
line(ax, [(4, 34), (36, 34)], 'fixe'); line(ax, [O, (20, 20)], 'sujet', lw=1.4)
disc(ax, 20, 20, 1.3, 'sujet')
text(ax, 23.5, 16, '270°', 'sujet', 's'); text(ax, 16, 36.5, 'O', 'encre', 's'); text(ax, 15.5, 20, 'P', 'encre', 's')
text(ax, 20, 49, 'sin 270° = −1', 'sujet', 's')
box(ax, 44, 40, 42, 10, 'sujet', label='cos² 270° = 0', size='s')
box(ax, 44, 26, 42, 10, 'varie', label='1 − sin 270° = 1 − (−1) = 2', size='s')
box(ax, 44, 12, 42, 10, 'limite', label='0 ≠ 2 : pas une identité', size='s')
save(fig, '31-109')
