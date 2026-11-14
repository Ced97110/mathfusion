import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# |z| = racine(a² + b²) : 3 + 4i et −3 + 4i donnent 5
fig, ax = canvas(60)
ox, oy, u = 27, 8, 6
arrow(ax, (ox - 24, oy), (ox + 24, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 2), (ox, oy + 34), 'fixe', lw=0.9)
P = (ox + 3 * u, oy + 4 * u)
Q = (ox - 3 * u, oy + 4 * u)
for X, role in ((P, 'sujet'), (Q, 'autre')):
    line(ax, [(X[0], oy), X], 'fixe', lw=0.8, dash=True)
    line(ax, [(ox, oy), X], role, lw=1.8)
    disc(ax, X[0], X[1], 1.5, role)
text(ax, P[0], P[1] + 3.5, '3 + 4i', 'sujet', 'm', weight='bold')
text(ax, Q[0] + 1, Q[1] + 3.5, '−3 + 4i', 'autre', 'm', weight='bold')
text(ax, 38.5, 17.5, '5', 'sujet', 'm', weight='bold')
text(ax, 15.5, 17.5, '5', 'autre', 'm', weight='bold')
text(ax, ox - 2.5, oy - 3, 'O', 'fixe', 's')
box(ax, 54, 38, 32, 9, 'fixe', label='3² + 4² = 9 + 16', size='s')
box(ax, 54, 25, 32, 9, 'fixe', label='= 25', size='s')
box(ax, 54, 12, 32, 9, 'resultat', label='√25 = 5', size='s')
arrow(ax, (70, 38), (70, 34.8), 'varie', lw=0.9)
arrow(ax, (70, 25), (70, 21.8), 'varie', lw=0.9)
text(ax, 70, 5, '(−3)² = 9 : même 5', 'autre', 's')
save(fig, '39-055')
