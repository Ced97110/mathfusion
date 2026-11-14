import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
u = 5; ly = 8; E = (20, ly); F = (E[0] + 5 * u, ly)
A = (E[0], ly + 8 + 5 * u * math.sqrt(3)); B = (F[0], ly + 8)
line(ax, [(8, ly), (62, ly)], 'fixe', lw=1.0)
line(ax, [A, E], 'fixe', dash=True); line(ax, [B, F], 'fixe', dash=True)
line(ax, [A, B], 'sujet', lw=2.0)
line(ax, [E, F], 'resultat', lw=2.6)
for p, sx in ((E, 1), (F, -1)):
    line(ax, [(p[0] + sx * 2, p[1]), (p[0] + sx * 2, p[1] + 2), (p[0], p[1] + 2)], 'fixe', lw=0.7)
for s, p, dx, dy in (('A', A, -3, 0), ('B', B, 3, 1), ('E', E, -2.5, -3), ('F', F, 2.5, -3)):
    text(ax, p[0] + dx, p[1] + dy, s, 'encre', 'm')
text(ax, 62, ly + 2.5, 'l', 'fixe', 'm', ha='left')
text(ax, 47, 42, 'bâton AB : 10 m', 'sujet', 'm', ha='left')
text(ax, 47, 33, 'fils à angle droit', 'fixe', 's', ha='left')
text(ax, 47, 24, 'projection EF : 5 m', 'resultat', 's', ha='left')
save(fig, '26-094')
