import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# un nombre sur une droite, deux parties dans le plan
fig, ax = canvas(80)
f = numberline(ax, 8, 48, 70, 0, 4, labels=False, arrow_right=True)
disc(ax, f(3), 70, 1.6, 'fixe')
text(ax, f(3), 65, '3', 'fixe', 'm')
text(ax, 70, 70, 'droite :\n1 nombre', 'fixe', 'm')
ox, oy, u = 20, 10, 10
arrow(ax, (ox - 8, oy), (ox + 56, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 3), (ox, oy + 40), 'fixe', lw=0.9)
P = (ox + 3 * u, oy + 2 * u)
line(ax, [(ox, oy), (P[0], oy)], 'varie', lw=1.8)
line(ax, [(P[0], oy), P], 'autre', lw=1.8)
text(ax, ox + 1.5 * u, oy - 3.5, 'a = 3', 'varie', 'm')
text(ax, P[0] + 2.5, oy + u, 'b = 2', 'autre', 'm', ha='left')
disc(ax, P[0], P[1], 1.7, 'sujet')
text(ax, P[0] - 2.5, P[1] + 3.5, '3 + 2i = (3, 2)', 'sujet', 'm', ha='right', weight='bold')
text(ax, 66, 44, 'plan :\n2 nombres', 'fixe', 'm')
save(fig, '39-051')
