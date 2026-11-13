import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(50)
O = (44, 24); r = 14
disc(ax, *O, r, 'fixe', fill=False)
line(ax, [(26, 24), (62, 24)], 'fixe')
disc(ax, 58, 24, 1.6, 'limite'); disc(ax, 30, 24, 1.6, 'limite')
text(ax, 44, 44, 'sin = 0 : P sur l’axe horizontal', 'limite', 's')
text(ax, 64, 30, '0° et 360°', 'limite', 's'); text(ax, 64, 18, '0 et 2π', 'limite', 's')
text(ax, 22, 30, '180°', 'limite', 's'); text(ax, 22, 18, 'π', 'limite', 's')
save(fig, '31-104')
