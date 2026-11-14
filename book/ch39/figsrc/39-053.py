import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# module de 3 + 4i : hypoténuse d'un triangle de côtés 3 et 4
fig, ax = canvas(64)
ox, oy, u = 14, 8, 10
arrow(ax, (ox - 6, oy), (ox + 56, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 3), (ox, oy + 50), 'fixe', lw=0.9)
P = (ox + 3 * u, oy + 4 * u)
line(ax, [(ox, oy), (P[0], oy)], 'fixe', lw=1.2)
line(ax, [(P[0], oy), P], 'fixe', lw=1.2)
line(ax, [(P[0] - 2, oy), (P[0] - 2, oy + 2), (P[0], oy + 2)], 'fixe', lw=0.7)
line(ax, [(ox, oy), P], 'sujet', lw=2.0)
disc(ax, P[0], P[1], 1.7, 'sujet')
text(ax, P[0] + 3, P[1] + 2, '3 + 4i', 'sujet', 'm', ha='left', weight='bold')
text(ax, ox + 1.5 * u, oy - 3.5, '3', 'fixe', 'm')
text(ax, P[0] + 2.5, oy + 2 * u, '4', 'fixe', 'm', ha='left')
text(ax, ox + 22, oy + 36, '|z| = r = 5', 'sujet', 'm', ha='right', weight='bold')
text(ax, ox - 3, oy - 3, 'O', 'fixe', 's')
save(fig, '39-053')
