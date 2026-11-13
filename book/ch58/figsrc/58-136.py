import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
u, O = 8.0, (10, 8)
P = lambda x, y: (O[0] + x * u, O[1] + y * u)
v1, v2, al, be = (1, 2), (0, 1), 2, 3
p1 = (al * v1[0], al * v1[1]); p2 = (be * v2[0], be * v2[1])
w = (p1[0] + p2[0], p1[1] + p2[1])
assert p1 == (2, 4) and p2 == (0, 3) and w == (2, 7)
for k in range(0, 8):
    line(ax, [P(0, k), P(3, k)], 'fixe', lw=0.3, dash=True)
for k in range(0, 4):
    line(ax, [P(k, 0), P(k, 8)], 'fixe', lw=0.3, dash=True)
arrow(ax, P(0, 0), P(*p1), 'sujet', lw=1.3)
arrow(ax, P(*p1), P(*w), 'autre', lw=1.3)
arrow(ax, P(0, 0), P(*w), 'resultat', lw=1.3)
disc(ax, *P(0, 0), 0.9, 'encre')
text(ax, P(0, 0)[0] + 3, P(0, 0)[1] - 3, r'$O$', 'encre', 's')
for (pt, y, role, lab) in [(p1, 40, 'sujet', r'$2\times(1,2)=(2,4)$'), ((0, 5.5), 52, 'autre', r'$3\times(0,1)=(0,3)$'), (w, 66, 'resultat', r'$w=(2,7)$')]:
    q = P(*pt) if role != 'autre' else P(2, 5.5)
    line(ax, [(q[0] + 1.5, q[1]), (38, y)], role, lw=0.5, dash=True)
    text(ax, 40, y, lab, role, 'm', ha='left', weight='bold' if role == 'resultat' else 'normal')
text(ax, 40, 60, 'combinaison de (1, 2) et (0, 1)', 'resultat', 's', ha='left')
save(fig, '58-136')
