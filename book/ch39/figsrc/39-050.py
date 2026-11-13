import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# plan complexe : 3, 2i et 3 + 2i
fig, ax = canvas(56)
ox, oy, u = 20, 10, 10
arrow(ax, (ox - 8, oy), (ox + 56, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 4), (ox, oy + 38), 'fixe', lw=0.9)
for k in (1, 2, 3):
    line(ax, [(ox + k * u, oy - 1), (ox + k * u, oy + 1)], 'fixe')
for k in (1, 2):
    line(ax, [(ox - 1, oy + k * u), (ox + 1, oy + k * u)], 'fixe')
P = (ox + 3 * u, oy + 2 * u)
line(ax, [(ox, P[1]), P], 'fixe', dash=True)
line(ax, [(P[0], oy), P], 'fixe', dash=True)
disc(ax, ox + 3 * u, oy, 1.2, 'fixe')
disc(ax, ox, oy + 2 * u, 1.2, 'fixe')
disc(ax, P[0], P[1], 1.6, 'sujet')
text(ax, ox + 3 * u, oy - 4, '3', 'fixe', 'm')
text(ax, ox + 3.5, oy + 2 * u + 3, '2i', 'fixe', 'm', ha='left')
text(ax, P[0] + 3, P[1] + 3, '3 + 2i', 'sujet', 'm', ha='left', weight='bold')
text(ax, P[0] + 3, P[1] - 3, '(3, 2)', 'sujet', 'm', ha='left')
text(ax, ox + 54, oy + 3.5, 'réels (b = 0)', 'fixe', 's', ha='right')
text(ax, ox - 3, oy + 36, 'nombres bi', 'fixe', 's', ha='right')
text(ax, ox - 2.5, oy - 3, 'O', 'fixe', 's')
save(fig, '39-050')
