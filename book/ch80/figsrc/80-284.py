import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
u = 15; ox, oy = 12, 16
arrow(ax, (ox - 2, oy), (ox + 3.6 * u, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy - 2), (ox, oy + 3.6 * u), 'fixe', lw=0.8)
text(ax, ox + 3.6 * u + 1, oy - 3.5, '$x$', 'fixe', 's'); text(ax, ox - 4, oy + 3.6 * u, '$y$', 'fixe', 's')
for k in (1, 2, 3):
    line(ax, [(ox + k * u, oy - 1), (ox + k * u, oy + 1)], 'fixe')
    line(ax, [(ox - 1, oy + k * u), (ox + 1, oy + k * u)], 'fixe')
    text(ax, ox + k * u, oy - 4, str(k), 'fixe', 's'); text(ax, ox - 4, oy + k * u, str(k), 'fixe', 's')
line(ax, [(ox - 0.5 * u, oy - 0.5 * u), (ox + 2.8 * u, oy + 2.8 * u)], 'sujet', lw=1.2)
line(ax, [(ox - 0.5 * u, oy + 0.5 * u), (ox + 2.5 * u, oy + 3.5 * u)], 'autre', lw=1.2)
for k in range(3):
    disc(ax, ox + k * u, oy + k * u, 1.3, 'sujet'); disc(ax, ox + k * u, oy + (k + 1) * u, 1.3, 'autre')
text(ax, ox + 3.0 * u, oy + 2.2 * u, r'$D_1$ : $x-y=0$', 'sujet', 's', ha='left')
text(ax, ox + 1.8 * u, oy + 3.5 * u + 3, r'$D_2$ : $x-y=-1$', 'autre', 's', ha='left')
text(ax, 44, 3, 'aucun point commun', 'limite', 's')
save(fig, '80-284')
