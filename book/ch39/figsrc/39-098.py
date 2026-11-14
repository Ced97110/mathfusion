import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

cx, cy, s = 44, 44, 22
fig, ax = canvas(88)
arrow(ax, (6, cy), (84, cy), 'fixe', lw=0.7)
arrow(ax, (cx, 12), (cx, 74), 'fixe', lw=0.7)
disc(ax, cx, cy, s, 'sujet', fill=False, lw=1.0)
# racines réelles : segment gris entre -1 et 1 sur l'axe
for (x, y, lab, ha, dx, dy) in [(1, 0, '1', 'left', 3.2, 3), (-1, 0, '−1', 'right', -3.2, 3),
                                (0, 1, r'$i$', 'left', 3, 1), (0, -1, r'$-i$', 'left', 3, -1)]:
    disc(ax, cx + x * s, cy + y * s, 1.4, 'sujet')
    text(ax, cx + x * s + dx, cy + y * s + dy, lab, 'sujet', 'm', ha=ha)
text(ax, 4, 84, r'$z^4=1$', 'encre', 'l', ha='left')
text(ax, 84, 84, 'module 1', 'sujet', 's', ha='right')
text(ax, cx - 2, 6, 'sur l’axe : 1 et −1 (réelles)', 'fixe', 's', ha='center')
text(ax, cx + 4, 78, r'$i$ et $-i$ : complexes', 'varie', 's', ha='left')
save(fig, '39-098')
