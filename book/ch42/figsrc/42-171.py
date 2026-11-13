import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
o = (44, 12); u = 7
P = lambda x, y, z: iso(x, y, z, o, u)
for end, lab, pos, ha in (((4.4, 0, 0), 'x : est', (4, 0), 'left'), ((0, 4.4, 0), 'y : nord', (-4, 0), 'right'), ((0, 0, 5.2), 'z : hauteur', (-3, 0), 'right')):
    arrow(ax, P(0, 0, 0), P(*end), 'fixe')
    q = P(*end); text(ax, q[0] + pos[0], q[1] + pos[1], lab, 'fixe', 's', ha=ha)
pts = [(0, 0, 0), (3, 0, 0), (3, 2, 0), (3, 2, 3)]
for p, q in zip(pts, pts[1:]): arrow(ax, P(*p), P(*q), 'varie', lw=1.3)
line(ax, [P(3, 2, 0), P(3, 2, 0)], 'fixe')
q = P(3, 2, 3); disc(ax, *q, 2.4, 'sujet')
text(ax, q[0] + 4, q[1] + 3, r'$(x,\,y,\,z)$', 'sujet', 'm', ha='left')
text(ax, 44, 4, r'$\mathbb{R}^{3}$ : triplets de réels', 'resultat', 'm')
save(fig, '42-171')
