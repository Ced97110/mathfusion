import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
c1 = (22, 44); r1 = 16
pts = [(c1[0] + r1*math.sin(math.radians(30*i)), c1[1] + r1*math.cos(math.radians(30*i))) for i in range(12)]
for i in range(1, 6): line(ax, [pts[i], pts[i+6]], 'fixe', lw=0.5, dash=True)
line(ax, [pts[0], pts[6]], 'sujet', lw=1.2)
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], 1.6, 'sujet' if i in (0, 6) else 'fixe')
text(ax, pts[0][0], pts[0][1] + 5, '0', 'sujet', 's')
text(ax, pts[6][0], pts[6][1] - 5, '6', 'sujet', 's')
c2 = (66, 44); r2 = 13
for j in range(6):
    a = math.radians(60*j)
    disc(ax, c2[0] + r2*math.sin(a), c2[1] + r2*math.cos(a), 2.2, 'autre')
arrow(ax, (41, 44), (50, 44), 'varie')
text(ax, 45.5, 48, r'$\nu$', 'varie', 'm')
text(ax, 22, 70, r'$G=\mathbb{Z}/12\mathbb{Z}$', 'sujet', 'm', weight='bold')
text(ax, 66, 70, r'$G/K$', 'autre', 'm', weight='bold')
text(ax, 22, 13, '12 éléments', 'sujet', 's')
text(ax, 66, 13, '6 paquets', 'autre', 's')
text(ax, 44, 4, r'sous-groupes de $G/K$ ?', 'varie', 'm', weight='bold')
save(fig, '48-089')
