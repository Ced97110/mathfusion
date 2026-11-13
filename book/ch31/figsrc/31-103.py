import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
O = (22, 30); r = 16
disc(ax, *O, r, 'fixe', fill=False)
line(ax, [(4, 30), (40, 30)], 'fixe'); line(ax, [(22, 10), (22, 50)], 'fixe', dash=True)
disc(ax, 22, 46, 1.6, 'limite'); disc(ax, 22, 14, 1.6, 'limite')
text(ax, 22, 51.5, '90° et 450°', 'limite', 's'); text(ax, 22, 8.5, '270°', 'limite', 's')
for i, a in enumerate((90, 270, 450)):
    text(ax, 66, 44 - i * 8, f'cos {a}° = 0', 'encre', 's')
text(ax, 66, 18, 'sec : 1/0 impossible', 'limite', 's')
save(fig, '31-103')
