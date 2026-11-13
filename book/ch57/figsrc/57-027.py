import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 25, 53, '1er nombre', 'fixe', 's'); text(ax, 40, 53, '2e nombre', 'fixe', 's')
rows = [(38, 'v', ('2', '1'), 'sujet'), (26, '+ w', ('−1', '2'), 'autre'), (12, '= v + w', ('1', '3'), 'resultat')]
for y, lab, (a, b), role in rows:
    box(ax, 1, y, 14, 9, role, label=lab, size='s')
    box(ax, 18, y, 14, 9, role, label=a, size='l')
    box(ax, 33, y, 14, 9, role, label=b, size='l')
text(ax, 25, 6.5, '2 + (−1) = 1', 'resultat', 's')
text(ax, 40.5, 6.5, '1 + 2 = 3', 'resultat', 's')
u = 9; ox, oy = 62, 14
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-1, 0), P(2.4, 0), 'fixe', lw=0.6); arrow(ax, P(0, 0), P(0, 3.6), 'fixe', lw=0.6)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(-1, 2), 'autre', lw=1.5)
arrow(ax, P(0, 0), P(1, 3), 'resultat', lw=1.7)
save(fig, '57-027')
